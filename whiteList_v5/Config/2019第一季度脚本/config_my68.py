# 财知道
TASK_NAME = 'my68'

# 起始URL
START_URL = 'http://www.my68.com/'

# 控制域，必须为list格式
DOMAIN = ['my68']
# 请求头
HEADERS = {
    'Host': 'www.my68.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0'
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
        "title": "string(.//*[@class='article-head']/h1)",
        "news_date": "substring-after(.//*[contains(@class,'icon-time')]/parent::span,'：')",
        "source": "substring-after(.//*[contains(@class,'icon-source')]/parent::span,'来源：')",
        "author": "",
        "navigation": "string(.//*[@class='crumbs'])",
        "content": ".//*[@class='article-article']/descendant::text()",
        "editor": "substring-after(.//*[contains(@class,'icon-user')]/parent::span,'责编：')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "string(.//*[@class='lblTitle'])",
        "news_date": "",
        "source": "",
        "author": "",
        "navigation": "",
        "content": ".//*[@class='description']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": ".//head/title/text()",
        "news_date": "string(.//*[@class='body_z']/p[2])",
        "source": "string(.//*[@class='body_z']/p[1])",
        "author": "",
        "navigation": "string(.//*[@class='location'])",
        "content": ".//*[@class='body_article']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='body_paper']/h1)",
        "news_date": "normalize-space(.//*[@class='body_z']/p[2])",
        "source": "normalize-space(.//*[@class='body_z']/p[1])",
        "author": "",
        "navigation": "normalize-space(.//*[@class='location'])",
        "content": ".//*[@class='body_article']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\w*[_]*\d*\.[s]*htm[l]*'

