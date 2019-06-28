# 来宾社区
TASK_NAME = 'bbs_laibin'

# 起始URL
START_URL = 'https://www.laibin.cc/forum.php'

# 控制域，必须为list格式
DOMAIN = ['laibin']
# 请求头
HEADERS = {
    'Host': 'www.laibin.cc',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.laibin.cc/',
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
        "news_date": "normalize-space(.//*[@id='postlist']/*[contains(@id,'post_')][1]//*[contains(@id,'authorposton')])",
        "source": "",
        "author": "normalize-space(.//*[@id='postlist']/*[contains(@id,'post_')][1]//*[contains(@class,'xi2')])",
        "navigation": "substring-after(normalize-space(.//*[@class='z']//*[contains(text(),'您的位置')]/parent::div),'您的位置：')",
        "content": ".//*[@id='postlist']/*[contains(@id,'post_')][1]//*[@class='pcb']//*[contains(@id,'postmessage')]/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\w*/[\w\d]*/$|forum\.php\?mod=viewthread&tid=\d*.*?page=1'

# 响应时间
# TIMEOUT = 20


