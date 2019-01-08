"""
启动任务
"""
import os
os.chdir(os.path.split(os.path.realpath(__file__))[0])
from multiprocessing import Process, Pool
from ControlNode.control_manager import ControlManager
from SpiderNode.spider_schedule import SpiderSchedule
import sys

if __name__ == '__main__':
    # 参数
    try:
        taskname = eval(sys.argv[1])
        if not isinstance(taskname, str):
            raise ValueError('arg=>taskname must be str')
    except Exception as e:
        print(e)
    # 导包进来
    try:
        exec('from Config.config_{} import *'.format(taskname))
        exec('from Config.configuration import *')
    except:
        print('not found {}.config file'.format(taskname))
    manager = ControlManager(TASK_NAME, DOMAIN, START_URL, URL_END, REGEX_URL, MQ_MAXSIZE)
    # 创建3个进程，分别进行任务发布，结果处理以及数据存储
    proc_task = Process(target=manager.manager_publish_task)  # 此处填写启动url
    proc_task.start()
    # 启动爬虫节点
    spider = SpiderSchedule(TASK_NAME, HEADERS, XPATHER_NEWS_LIST, XPATHER_HREF, SPIDERS)
    proc_spider = Process(target=spider.schedule_start)
    proc_spider.start()

