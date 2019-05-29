# 广西论坛
TASK_NAME = 'bbs_gxbbs'

# 起始URL
START_URL = 'http://www.gxbbs.cc/forum.php'

# 控制域，必须为list格式
DOMAIN = ['gxbbs']
# 请求头
HEADERS = {
    'Host': 'www.gxbbs.cc',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://www.gxbbs.cc/',
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
        "title": "translate(normalize-space(.//*[@class='title-cont']),'[复制链接]','')",
        "news_date": "substring-after(normalize-space(.//*[@class='post first shadow']//*[contains(text(),'发表于')]),'发表于:')",
        "source": "",
        "author": ".//*[@class='post first shadow']//*[@class='name']/@title",
        "navigation": "normalize-space(.//*[@class='nvhm']/parent::div)",
        "content": ".//*[@class='post first shadow']//*[contains(@id,'postmessage')]/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/thread[\d-]*\.s*html*'


