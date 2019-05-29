# 旺苍在线
TASK_NAME = 'bbs_scgywc'

# 起始URL
START_URL = 'http://www.scgywc.com/forum/'

# 控制域，必须为list格式
DOMAIN = ['scgywc']
# 请求头
HEADERS = {
    'Host': 'www.scgywc.com',
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
        "title": "substring-after(normalize-space(.//*[@class='topic_title']),'主题:')",
        "news_date": "substring-after(normalize-space(.//*[@id='topic_o'][1]//*[contains(text(),'发表于')]),'发表于：')",
        "source": "",
        "author": "normalize-space(.//*[@id='topic_o'][1]//*[@class='topic_name'])",
        "navigation": "normalize-space(.//*[@class='nav_c'])",
        "content": ".//*[@id='topic_o'][1]//*[@class='topic_c']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/thread-\d*-1-\d*\.s*html*'

# 响应时间
# TIMEOUT = 20


