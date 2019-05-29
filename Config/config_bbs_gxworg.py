# 桂人网社区
TASK_NAME = 'bbs_gxworg'

# 起始URL
START_URL = 'https://www.gxworg.com/forum.php'

# 控制域，必须为list格式
DOMAIN = ['gxworg']
# 请求头
HEADERS = {
    'Host': 'www.gxworg.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
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
        "title": "normalize-space(.//*[@id='thread_subject'])",
        "news_date": "substring-after(normalize-space(.//*[@id='postlist']//*[contains(@id,'post_')][1]//*[@class='pti']//*[@class='authi']//*[contains(text(),'发表于')]),'发表于')",
        "source": "",
        "author": "normalize-space(.//*[@id='postlist']//*[contains(@id,'post_')][1]//*[@class='pti']//*[@class='authi']//*[@class='xi2'])",
        "navigation": "normalize-space(.//*[@class='nvhm']/parent::div)",
        "content": ".//*[@id='postlist']//*[contains(@id,'post_')][1]//*[@class='pct']//*[contains(@id,'postmessage')]/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='ph'])",
        "news_date": "substring-before(substring-after(normalize-space(.//*[contains(text(),'发布者')]),'发布时间:'),'|')",
        "source": "",
        "author": "substring-before(substring-after(normalize-space(.//*[contains(text(),'发布者')]),'发布者:'),'|')",
        "navigation": "normalize-space(.//*[@class='nvhm']/parent::div)",
        "content": ".//*[@id='ct']//*[contains(@id,'postmessage')]/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/thread-\d*-1(-\d)*\.s*html*'

# 响应时间
TIMEOUT = 20


