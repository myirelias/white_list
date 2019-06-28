# !/usr/bin/env python
# coding=UTF-8
"""
2019.03.18 页面编码出现问题，utf-8的页面中出现乱码，新增decode忽略异常编码机制
"""
import requests
from lxml import etree


class SpiderCrawl(object):
    """
    页面下载类
    """
    def __init__(self):
        self.session = requests.Session()

    def crawl_get_content(self, url, usesession=True, **kw):
        """
        get请求页面，并返回content,请使用params,proxies,timeout,pagecode, headers命名参数
        :param url: 请求地址
        :param usesession: 使用session标识，默认True
        :param kw: 关键字参数
        :return: 页面的content
        """

        retry = kw.get('retry', 5)  # 重试次数
        response = 'no_data'
        code_flag = False
        while retry:
            retry -= 1
            try:
                if usesession:  # 使用session请求
                    res = self.session.get(url, params=kw.get('params', ''), headers=kw.get('headers', ''),
                                           proxies=kw.get('proxies', ''), timeout=kw.get('timeout', 30))
                else:  # 不使用session请求
                    res = requests.get(url, params=kw.get('params', ''), headers=kw.get('headers', ''),
                                       proxies=kw.get('proxies', ''), timeout=kw.get('timeout', 30))
                if res.status_code == 200:  # 状态码为200则立刻终止，否则重试
                    if 'charset=utf-8' in res.text.lower():
                        response = res.content.decode(kw.get('pagecode', 'UTF-8'), 'ignore')
                    else:
                        response = res.content.decode(kw.get('pagecode', 'UTF-8'))
                    break
                else:
                    continue
            except UnicodeDecodeError:
                kw['pagecode'] = 'gbk'
                if code_flag:
                    try:
                        response = res.text
                    except:
                        pass
                code_flag = True
            except Exception as e:
                # print('[requests page error] %s' % e)
                continue

        return response

    def crawl_post_content(self, url, usesession=True, **kw):
        """
        post请求页面，并返回content，请使用data,proxies,timeout,pagecode, headers命名参数
        :param url: 请求地址
        :param usesession: 使用session请求，默认为True
        :param kw: 关键字参数
        :return: 返回页面content
        """

        retry = kw.get('retry', 5)
        response = 'no_data'
        while retry:
            retry -= 1
            try:
                if usesession:
                    res = self.session.post(url, data=kw.get('params', ''), headers=kw.get('headers', ''),
                                            proxies=kw.get('proxies', ''), timeout=kw.get('timeout', 30))
                else:
                    res = requests.post(url, data=kw.get('params', ''), headers=kw.get('headers', ''),
                                        proxies=kw.get('proxies', ''), timeout=kw.get('timeout', 30))
                if res.status_code == 200:
                    response = res.content.decode(kw.get('pagecode', 'UTF-8'))
                    break
                else:
                    continue
            except UnicodeDecodeError:
                kw['pagecode'] = 'gbk'
            except Exception as e:
                # print('[requests page error] %s' % e)
                continue

        return response


class SpiderAnalysis(object):
    """
    页面解析类
    """
    def __init__(self):
        pass

    @staticmethod
    def spider_content_data(**kwargs):
        """
        解析content中指定内容，必须传入 content 和 xpather
        :param kwargs: content 为需要解析的页面content, xpather 为xpath解析规则
        :return: 解析后的内容，若xpather为dict类型则返回dict类型，其余返回list
        """

        if 'content' not in kwargs or 'xpather' not in kwargs:
            print('must require enough args')
            return

        xpather = kwargs['xpather']
        content = kwargs['content']

        try:
            selector = etree.HTML(content)
        except:
            selector = content  # 针对需要解析多次的页面采取的方式，前面几次返回的是 etree的element对象，继续解析

        if isinstance(kwargs['xpather'], dict):  # 解析规则以dict的格式传过来的，这种规则默认解析结果为一条数据
            response = {}
            for eachkey in xpather:
                if not xpather[eachkey]:
                    continue
                try:
                    res = selector.xpath(xpather[eachkey])
                except Exception as e:
                    print(e)
                    return
                if eachkey == 'news_date':
                    response[eachkey] = ''.join(res).replace('\n', '').replace('\r', '').replace('\u3000', '')
                else:
                    response[eachkey] = ''.join(res).replace('\n', '').replace('\r', '').replace('\u3000', '').\
                        replace(' ', '')
        elif isinstance(kwargs['xpather'], str):  # 解析规则为str
            try:
                response = selector.xpath(kwargs['xpather'])
            except Exception as e:
                print(e)
                return
        else:
            print('xpather must be dict or string')
            return

        return response
