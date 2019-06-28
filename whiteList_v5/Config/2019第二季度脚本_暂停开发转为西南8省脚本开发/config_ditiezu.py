# 地铁族
TASK_NAME = 'ditiezu'

# 起始URL
START_URL = 'http://www.ditiezu.com/'

# 控制域，必须为list格式
DOMAIN = ['ditiezu']
# 请求头
HEADERS = {
    'Host': 'www.ditiezu.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
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
        "title": "normalize-space(.//*[@id='thread_subject'])",
        "news_date": ".//*[@id='postlist']/div[contains(@id,'post')][1]//*[contains(text(),'发表于')]/span/@title",
        "source": "",
        "author": "normalize-space(.//*[@id='postlist']/div[contains(@id,'post')][1]//*[contains(@class,'authi')]//*[@class='xw1'])",
        "navigation": "normalize-space(.//*[@class='nvhm']/parent::div)",
        "content": ".//*[@id='postlist']/div[contains(@id,'post')][1]//*[contains(@id,'postmessage')]/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/thread[\d-]*\.s*html*'

