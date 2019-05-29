# 东方财富网
TASK_NAME = 'eastmoney'

# 起始URL
START_URL = 'http://www.eastmoney.com/'

# 控制域，必须为list格式
DOMAIN = ['eastmoney']
# 请求头
HEADERS = {
    'Host': 'www.eastmoney.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Cookie': '_adsame_fullscreen_17327=1; st_pvi=98002142143784; st_sp=2019-01-16%2009%3A45%3A02; st_si=25826600301580; st_sn=2; st_psi=20190116094515859-112101300783-2928608358; st_asi=delete; qgqp_b_id=19664d47fd0cff3cc1d49877d850287a',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'If-Modified-Since': 'Wed, 16 Jan 2019 01:44:01 GMT',
    'If-None-Match': 'W/"5c3e8c61-7c1c2"',
    'Cache-Control': 'max-age=0',
}

# xpath规则
XPATHER_HREF = ".//*/@href"
# 字段模版
# {
#     "title": "",
#     "news_date": "",
#     "source": "",
#     "author": "",
#     "navigation": "",
#     "content": "",
#     "editor": "",
#     "tags": ""
# },
XPATHER_NEWS_LIST = [
    {
        "title": ".//*[@class='articleTitle']/text()",
        "news_date": ".//*[@class='time']/text()",
        "source": "",
        "author": ".//*[@tracker-eventcode='blog_artiUserName']/text()",
        "navigation": "string(.//*[@class='menu'])",
        "content": ".//*[@class='articleBody']/descendant::text()",
        "editor": "",
        "tags": ".//*/head/title/text()"
    },
    {
        "title": ".//*/h1/text()",
        "news_date": ".//*[@class='time-source']//*[@class='time']/text()",
        "source": ".//*[contains(@class,'data-source')]/descendant::text()|.//*[starts-with(@class,'source')]/img/@alt",
        "author": "substring-after(.//*[@class='author'],'：')",
        "navigation": "string(.//*[@id='Column_Navigation'])",
        "content": ".//*[@class='Body']/descendant::text()",
        "editor": "substring-after(.//*[@class='res-edit'],'责任编辑：')",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\w*[_]*\d*\.[s]*htm[l]*'

