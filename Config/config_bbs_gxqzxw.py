# 钦州930
TASK_NAME = 'bbs_gxqzxw'

# 起始URL
START_URL = 'http://930.gxqzxw.com/'

# 控制域，必须为list格式
DOMAIN = ['gxqzxw']
# 请求头
HEADERS = {
    'Host': '930.gxqzxw.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
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
        "title": "normalize-space(.//*[@class='bbsbt'])",
        "news_date": "substring-before(substring-after(normalize-space(.//*[@class='bbsx'][1]//*[contains(text(),'发表于')]),'发表于'),'|')",
        "source": "",
        "author": "normalize-space(.//*[@class='bbsu'][1]//*[@class='np_uon'])",
        "navigation": "substring-after(normalize-space(.//*[@class='path']),'当前位置:')",
        "content": ".//*[@class='bbsx'][1]//*[@class='jsl_bbs_c_txt']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/view\.asp\?id=\d*'

# 响应时间
# TIMEOUT = 20


