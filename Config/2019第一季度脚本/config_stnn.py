# 贵州网
TASK_NAME = 'stnn'

# 起始URL
START_URL = 'http://www.stnn.cc/'

# 控制域，必须为list格式
DOMAIN = ['stnn']
# 请求头
HEADERS = {
    'Host': 'www.stnn.cc',
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
        "title": "normalize-space(.//*[@class='article-title'])",
        "news_date": "normalize-space(.//*[@class='date'])",
        "source": "normalize-space(.//*[@class='source'])",
        "author": "",
        "navigation": "substring-after(normalize-space(.//*[@class='crumb']),'首页')",
        "content": ".//*[starts-with(@class,'article-content')]/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='picture-header']/h1)",
        "news_date": "normalize-space(.//*[@class='post-time'])",
        "source": "",
        "author": "",
        "navigation": "normalize-space(.//*[@class='crumb'])",
        "content": ".//*[contains(@class,'photo-description')]/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{4}/\d{4}/\d*\.[s]*htm[l]*'

