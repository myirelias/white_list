# !/usr/bin/env python
# coding=utf-8

import datetime
import json
import os
import re
import time
from imp import reload
from multiprocessing import Process
import pika
from ControlNode.control_data import ControlData
from ControlNode.control_task import ControlTask


class ControlManager(object):
    """
    控制管理器，负责调度任务管理器和数据管理器
    必须参数：taskname, domain, start, url_end, regex_url, mq_maxsize
    非必须参数：
    """

    def __init__(self, taskname, domain, start, url_end, regex_url, mq_maxsize, **kw):
        self.redis_host = kw.get('REDIS_HOST', 'localhost')
        self.redis_port = kw.get('REDIS_HOST', 6379)
        self.taskname = taskname
        self.domain = domain
        self.start_url = start
        self.url_end = url_end
        self.regex_url = regex_url
        self.mq_maxsize = mq_maxsize
        self.task_queue = '{}_{}'.format(taskname, 'task')
        self.result_queue = '{}_{}'.format(taskname, 'result')
        print('controlmanager init finsh')

    def manager_publish_task(self):
        """
        任务发布
        :param
        :return:
        """
        task_manager = ControlTask(taskname=self.taskname, redis_host=self.redis_host, redis_port=self.redis_port)
        # 启动时候提供起始url：start_url, 如果task,result,continue队列都没有任务才发布
        if not task_manager.task_query_redis('{}_{}'.format(self.taskname, 'task')):
            task_manager.task_redis_del(key='{}_old_list0'.format(self.taskname))
            task_manager.task_check(self.start_url, domain=self.domain)
        # 启动后一直循环执行
        while True:
            if not task_manager.task_query_redis('{}_{}'.format(self.taskname, 'task')) and not task_manager.new_urls:
                task_manager.task_redis_del(key='{}_old_list0'.format(self.taskname))
                current_task = {'type': 'unstatic',
                                'url': self.start_url}
                task_manager.task_push_redis(self.task_queue, json.dumps(current_task))
                time.sleep(10)
            while task_manager.task_has_new():  # 只要存在新增任务则会往对应队列里面推送
                # 待处理的数据大于一百条的时候先去处理
                if task_manager.task_query_redis(self.result_queue) >= 1000:
                    break
                static_task, unstatic_task = task_manager.task_static_unstatic(self.regex_url)
                all_task = []
                for eachtask in static_task:
                    try:
                        if eachtask.split('.')[-1] in self.url_end:
                            continue
                    except:
                        continue
                    current_task = {'type': 'static',
                                    'url': eachtask}
                    all_task.append(json.dumps(current_task))
                for eachtask in unstatic_task:
                    try:
                        if eachtask.split('.')[-1] in self.url_end:
                            continue
                    except:
                        continue
                    current_task = {'type': 'unstatic',
                                    'url': eachtask}
                    all_task.append(json.dumps(current_task))
                task_manager.task_push_redis(self.task_queue, all_task)
            n = 500
            # 下面是对结果(redis-result)进行处理
            while n:
                n -= 1
                result = task_manager.task_pop_redis(self.result_queue)
                if not result:
                    break
                deal_result = self._manager_deal_result(result)
                # 后续返回结果处理
                if not deal_result:
                    continue
                if deal_result.get('push_data'):
                    self._manager_save_data(deal_result['push_data'])
                elif deal_result.get('push_task'):
                    task_manager.task_check(deal_result['push_task'], domain=self.domain)

    def _manager_deal_result(self, data):
        """
        处理结果
        :return:
        """
        try:
            result_dict = json.loads(data)
        except Exception as e:
            print(e)
            return
        content = result_dict.get('content')
        urls = result_dict.get('urls')
        if content:
            pushdata = json.dumps(content)
            # 返回待存储数据
            return {'push_data': pushdata}
        if urls:
            # v4版本此处控制数量，v5取消
            # -----------BEGIN--------------注意此处--------------BEGIN--------------
            current_url = result_dict.get('url')
            current_urllist = []
            root_url = ''
            # 拼接根url
            if len(current_url.split('/')) > 3:
                root_url = '/'.join(current_url.split('/')[:3])

            for eachurl in urls:
                newurl = ''
                if eachurl:
                    # 无需拼接
                    if eachurl.startswith(('http', 'HTTP')):
                        newurl = eachurl
                    # 默认无效链接
                    elif eachurl.startswith(('#', 'mailto', 'javascript')):
                        continue
                    # 如果以..开头，则要到父级url
                    elif eachurl.startswith('..'):
                        if len(current_url.split('/')) > 4:
                            newurl = '/'.join(current_url.split('/')[0:-2]) + re.sub(re.compile('(\.\.[/]*)+'), '/',
                                                                                     eachurl)
                        elif len(current_url.split('/')) <= 4:
                            if root_url:
                                new_eachurl = re.sub(re.compile('(\.\.[/]*)+'), '/', eachurl)
                                newurl = root_url + new_eachurl
                    # 如果以/开头，则要到根url
                    elif eachurl.startswith('/'):
                        if root_url:
                            newurl = root_url + eachurl
                    # 如果以./开头，则就替换当前位置
                    elif eachurl.startswith('./'):
                        if current_url.endswith('/'):
                            newurl = current_url + eachurl[2::]
                        else:
                            current_url_copy = current_url
                            if len(current_url.split('/')) < 4:
                                continue
                            newurl = current_url_copy.replace(current_url.split('/')[-1], eachurl[2::])
                    # 同./
                    elif eachurl.startswith('.'):
                        if current_url.endswith('/'):
                            newurl = current_url + eachurl[1::]
                        else:
                            current_url_copy = current_url
                            newurl = current_url_copy.replace(current_url.split('/')[-1], eachurl[1::])
                    else:
                        if current_url.endswith('/'):
                            newurl = current_url + eachurl
                        else:
                            current_url_copy = current_url
                            newurl = current_url_copy.replace(current_url.split('/')[-1], eachurl)
                    if newurl:
                        current_urllist.append(newurl)
            # -----------END----------------注意此处--------------END----------------
            return {'push_task': current_urllist}

    def _manager_save_data(self, data, **kw):
        """
        存储数据
        配置参数：
        dbname: 数据库名称 colname:集合名称
        :return:
        """
        data_manager = ControlData()
        # 从数据队列中取之并进行存储
        try:
            save_data = json.loads(data)
            if save_data.get('title'):
                data_manager.data_save_db(data=save_data, dbname=kw.get('dbname', 'db_public_opinion'),
                                               colname=kw.get('colname', 'col_' + self.taskname))
            else:
                save_invalid = {'invalid_url': save_data.get('url'),
                                'get_time': save_data.get('get_time')}
                data_manager.data_save_db(data=save_invalid, dbname=kw.get('invalid_dbname', 'db_public_invalid'),
                                               colname=kw.get('colname', 'col_' + self.taskname))
        except Exception as e:
            print(e)
            return

    @staticmethod
    def _manager_reload_config():
        """
        动态加载动态文件,暂时停用
        :return:
        """
        with open(os.path.join(os.path.abspath('..'), 'config.ini'), 'r', encoding='UTF-8') as f:
            with open(os.path.join(os.path.abspath('..'), 'config.py'), 'w', encoding='UTF-8') as fn:
                fn.write(f.read())

        import config as setting
        reload(setting)

#
# if __name__ == '__main__':
#     manager = ControlManager('chinanews', 'chinanews.com', 'http://www.chinanews.com/', ['mp3', 'm4'],
#                              r'/\d{4}/\d{2}-\d{2}/\d+.[s]*htm[l]*', 10000)
#     # 创建3个进程，分别进行任务发布，结果处理以及数据存储
#     manager.manager_publish_task()
