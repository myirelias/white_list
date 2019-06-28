# 人民论坛网
TASK_NAME = 'rmlt'

# 起始URL
START_URL = 'http://www.rmlt.com.cn/'

# 控制域，必须为list格式
DOMAIN = ['rmlt']
# 请求头
HEADERS = {
    'Host': 'www.rmlt.com.cn',
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
        "title": "normalize-space(.//*[@class='article-title'])",
        "news_date": "normalize-space(.//*[@class='date'])",
        "source": "normalize-space(.//*[@class='source'])",
        "author": "",
        "navigation": "normalize-space(.//*[contains(@class,'crumb')])",
        "content": ".//*[contains(@class,'article-content')]/descendant::text()",
        "editor": "translate(substring(normalize-space(.//*[@class='editor']),7,20),']','')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='picture-header']/h1)",
        "news_date": "normalize-space(.//*[@class='post-time'])",
        "source": "normalize-space(.//*[@class='source'])",
        "author": "",
        "navigation": "normalize-space(.//*[@class='crumb'])",
        "content": ".//*[contains(@class,'photo-description')]/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[@class='editor']),'责任编辑：')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='videoshow-title'])",
        "news_date": "normalize-space(.//*[contains(@class,'date')])",
        "source": "substring-after(normalize-space(.//*[contains(text(),'来源')]),'来源：')",
        "author": "",
        "navigation": "normalize-space(.//*[contains(@class,'crumb')])",
        "content": ".//*[@class='tv-cont']/descendant::p/text()",
        "editor": "substring-after(normalize-space(.//*[contains(text(),'责任编辑')]),'责任编辑：')",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{4}/\d{4}/\d*\.s*html*'

