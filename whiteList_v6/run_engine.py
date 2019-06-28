# !/usr/bin/env python
# coding=UTF-8

import sys
import logging
import re
import datetime
import threading
import time
from whole_spider import SpiderCrawl, SpiderAnalysis
from whole_middleware import RedisMiddleware
from whole_pipeline import ControlData

try:
    taskname = eval(sys.argv[1])
    if not isinstance(taskname, str):
        raise ValueError('arg=>taskname must be str')
except Exception as e:
    print(e)
# taskname = 'banyuetan'

## 导包进来
try:
    exec('from Config.config_{} import *'.format(taskname))
    exec('from Config.configuration import *')
except:
    print('not found {}.config file'.format(taskname))

# taskname = ''
# redis_host = ''
# redis_port = 0
# redis_psw = ''
# mongo_host = ''
# mongo_port = 0
# current_headers = ''
# spider_count = 3
# dbname = ''
# colname = ''


class WholeEngine:
    """
    引擎类
    """

    def __init__(self):
        self.redis_tool = RedisMiddleware(TASK_NAME, REDIS_PARAMS)
        self.crawler = SpiderCrawl()
        self.analysis = SpiderAnalysis()
        self.pipe = ControlData(MONGO_HOST, MONGO_PORT)
        self.list_queue = '{}:redis_list'.format(TASK_NAME)  # 列表队列
        self.news_queue = '{}:redis_news'.format(TASK_NAME)  # 新闻队列
        self.bloome_list_queue = '{}:redis_list0'.format(TASK_NAME)  # 列表去重过滤器
        fmt = '%(asctime)s-%(levelname)s-%(lineno)s:%(message)s'
        logging.basicConfig(level=logging.INFO, filename='./LOGDATA/{}_抓取日志.log'.format(TASK_NAME), format=fmt)
        self.count = 0
        try:
            self.time_out = TIME_OUT
        except:
            self.time_out = 5
        try:
            self.pagecode = PAGE_CODE
        except:
            self.pagecode = 'utf-8'

    def _engine_listen_redis(self):
        """
        监控消息队列是否为空
        当两个消息队列为空时
        重置list的过滤器并记录本轮抓取完成
        :return:
        """
        print('监听器启动')
        while 1:
            res_list_queue = self.redis_tool.redis_query(self.list_queue)
            res_news_queue = self.redis_tool.redis_query(self.news_queue)
            if not res_list_queue and not res_news_queue:
                # print('监听器发现队列均无数据，删除过滤器，发布起始url')  # 当两个队列均无数据 1.第一次抓取 2.上轮抓取已完成
                self.redis_tool.redis_del(self.bloome_list_queue)  # 删除列表过滤器
                logging.info("{} 循环 {}".format(TASK_NAME, self.count))  # 记录日志信息
                self.count += 1
                self.redis_tool.redis_push(self.list_queue, START_URL)  # 发布起始url到队列中
            time.sleep(60)

    def _engine_spider_list(self):
        """
        列表爬虫
        会生成列表url以及新闻url
        :return:
        """
        while 1:
            try:
                time.sleep(SLEEP_TIME)
                url = self.redis_tool.redis_brpop(self.list_queue, timeout=0)  # 阻塞等待redis列表中的任务
                current_url = str(url, encoding='utf-8')
                print(f'[{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}]list爬虫{threading.current_thread().name} 接收到任务 {current_url}')
                current_headers = HEADERS
                current_headers['Proxy-Switch-Ip'] = 'yes'
                content = self.crawler.crawl_get_content(current_url, headers=current_headers,
                                                         proxies=self._schedule_use_proxy(), timeout=self.time_out, retry=2,
                                                         pagecode=self.pagecode)  # 请求任务页面
                res_list = self.analysis.spider_content_data(content=content,
                                                             xpather=XPATHER_HREF)  # 解析出页面上所有的链接
                clean_urls = self._engine_urls_cleanout(res_list, current_url)  # 页面所有链接进行整理拼接
                self._engine_urls_distinction(clean_urls)  # 所有链接进行列表、新闻区分并做去重校验后新增链接推送至各自队列
            except:
                continue

    def _eneine_spider_news(self):
        """
        新闻爬虫
        只产生页面数据
        :return:
        """
        while 1:
            try:
                url = self.redis_tool.redis_brpop(self.news_queue, timeout=0)  # 阻塞等待redis列表中的任务
                current_url = str(url, encoding='utf-8')
                print(f'[{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}]news爬虫{threading.current_thread().name} 接收到任务 {current_url}')
                current_headers = HEADERS
                current_headers['Proxy-Switch-Ip'] = 'yes'
                content = self.crawler.crawl_get_content(current_url, headers=current_headers,
                                                         proxies=self._schedule_use_proxy(), timeout=self.time_out, retry=2,
                                                         pagecode=self.pagecode)
                res_dict = {}
                for eachxpath in XPATHER_NEWS_LIST:
                    res_dict = self.analysis.spider_content_data(content=content, xpather=eachxpath)
                    if res_dict.get('title'):
                        break
                res_dict['news_url'] = current_url
                self._engine_save_data(res_dict)
            except:
                continue

    def _engine_urls_cleanout(self, urls, current_url):
        """
        url清洗工具, 需要提供urls列表，已经获取到该列表的当前页面链接
        对页面返回的url进行拼接处理
        :return:
        """
        clean_urls = []
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
                        recount = len(re.findall(re.compile('\.\./'), eachurl)) - 1
                        try:
                            newurl = '/'.join(current_url.split('/')[0:-2 - recount]) + re.sub(
                                re.compile('(\.\.[/]*)+'), '/',
                                eachurl)
                        except:
                            newurl = '/'.join(current_url.split('/')[0:-2]) + re.sub(re.compile('(\.\.[/]*)+'), '/',
                                                                                     eachurl)
                    elif len(current_url.split('/')) <= 4:
                        if root_url:
                            new_eachurl = re.sub(re.compile('(\.\.[/]*)+'), '/', eachurl)
                            newurl = root_url + new_eachurl
                # 如果以//开头 直接拼接http
                elif eachurl.startswith('//'):
                    newurl = '{}:{}'.format(START_URL.split(':')[0], eachurl)
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
                    newurl = newurl.split("#")[0]  # 页内跳转的参数直接去掉
                    clean_urls.append(newurl)
        # -----------END----------------注意此处--------------END----------------
        return clean_urls

    def _engine_urls_distinction(self, urls):
        """
        用于区分列表url和新闻url
        :return:
        """
        if not isinstance(urls, list):
            urls = [urls]
        new_news_list = []
        new_list_list = []
        for each_url in urls:
            # 匹配新闻的正则表达式
            for eachdomain in DOMAINS:  # 多个domain循环
                if eachdomain not in each_url:  # 若个任务连接不在domain内，则切换下一个domain
                    continue
                else:  # 若任务连接在domain内，则break跳出循环，for...else中的内容不会执行，则此任务链接会被进行后续处理
                    break
            else:
                continue
            try:
                if each_url.split('.')[-1] in URL_END:
                    continue
            except:
                continue
            if self._task_regex(each_url, REGEX_URL):
                new_news_list.append(each_url)
                continue
            elif REGEX_LIST != '.*':
                # 被限制的列表url正则表达式，如果不匹配则是未被限制，默认抓取
                if not self._task_regex(each_url, REGEX_LIST):
                    new_list_list.append(each_url)
                continue
            else:
                new_list_list.append(each_url)
        new_list_list.extend(new_news_list)  # 所有新闻页面也会去抓取一次里面所有链接
        for each_data in set(new_list_list):
            if not self.redis_tool.bloom_list.isContains(each_data):
                self.redis_tool.redis_push(self.list_queue, each_data)
                self.redis_tool.bloom_list.insert(each_data)
        for each_data in set(new_news_list):
            if not self.redis_tool.bloom_urls.isContains(each_data):
                self.redis_tool.redis_push(self.news_queue, each_data)
                self.redis_tool.bloom_urls.insert(each_data)

    @staticmethod
    def _task_regex(data, regexer):
        """
        正则过滤url,按照静态新闻页面和非静态新闻页面划分
        :param data: 需要过滤的url
        :return: 静态 True 非静态 False
        """
        pattern = re.compile(regexer, re.S)
        res = re.search(pattern, data)
        if res:
            return True

        return False

    def _engine_save_data(self, save_data, dbname='', colname=''):
        """
        数据存储
        将页面数据推送至数据库进行存储
        :return:
        """
        try:
            # 保证取数据的时候抓取时间为当前时间
            save_data['crawl_date'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if save_data.get('title'):
                self.pipe.data_save_db(data=save_data, dbname=DBNAME_SUCCESS, colname='{}_news'.format(TASK_NAME))
            else:
                save_invalid = {'news_url': save_data.get('news_url'),
                                'crawl_date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
                self.pipe.data_save_db(data=save_invalid, dbname=DBNAME_FAIL, colname='{}_news_failed'.format(TASK_NAME))
        except Exception as e:
            print(e)
            return

    def _schedule_use_proxy(self):
        """
        使用代理ip
        :return: 代理ip
        """
        proxy_meta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {"host": PROXY_INFO.get("PROXY_HOST"),
                                                                     "port": PROXY_INFO.get("PROXY_PORT"),
                                                                     "user": PROXY_INFO.get("PROXY_USER"),
                                                                     "pass": PROXY_INFO.get("PROXY_PASS")}
        proxies = {"http": proxy_meta,
                   "https": proxy_meta}

        return proxies

    def run_engine(self):
        """
        启动方法
        :return:
        """
        th_listen = threading.Thread(target=self._engine_listen_redis)
        th_listen.start()
        th_spider_list = threading.Thread(target=self._engine_spider_list)
        th_spider_list.start()
        th_list = []
        for i in range(SPIDER_COUNT):
            th_spider_news = threading.Thread(target=self._eneine_spider_news)
            th_spider_news.start()
            th_list.append(th_spider_news)
        th_list.append(th_listen)
        th_list.append(th_spider_list)
        for each_th in th_list:
            each_th.join()


if __name__ == '__main__':
    proc = WholeEngine()
    proc.run_engine()