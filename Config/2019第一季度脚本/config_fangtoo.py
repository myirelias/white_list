# 房途网
TASK_NAME = 'fangtoo'

# 起始URL
START_URL = 'http://www.fangtoo.com/'

# 控制域，必须为list格式
DOMAIN = ['fangtoo']
# 请求头
HEADERS = {
    'Host': 'www.fangtoo.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'If-Modified-Since': 'Tue, 26 Feb 2019 06:20:30 GMT',
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
        "title": "normalize-space(.//*[@class='main-text-cnt']/h1)",
        "news_date": "substring(normalize-space(.//*[contains(@class,'time-source')]),1,20)",
        "source": "substring-before(substring-after(normalize-space(.//*[contains(@class,'time-source')]),'来源：'),'编辑')",
        "author": "",
        "navigation": "normalize-space(.//*[@class='urhere'])",
        "content": ".//*[@class='main-text']/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[contains(@class,'time-source')]),'编辑：')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='title'])",
        "news_date": "normalize-space(.//*[@class='info']/span[1])",
        "source": "normalize-space(.//*[@class='info']/span[3])",
        "author": "",
        "navigation": "normalize-space(.//*[@class='channel-name'])",
        "content": ".//article/descendant::p/text()",
        "editor": "substring-after(normalize-space(.//*[@class='info']/span[2]),'编辑：')",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d*-\d*-\w*\d*\.[s]*htm[l]*'

