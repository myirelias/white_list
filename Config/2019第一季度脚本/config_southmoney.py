# 财知道
TASK_NAME = 'southmoney'

# 起始URL
START_URL = 'http://www.southmoney.com/'

# 控制域，必须为list格式
DOMAIN = ['southmoney']
# 请求头
HEADERS = {
    'Host': 'www.southmoney.com',
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
        "title": "string(.//*[@class='artTitle'])",
        "news_date": "substring(.//*[@class='artDate'],1,16)",
        "source": "substring-after(.//*[@class='artDate'],'来源：')",
        "author": "",
        "navigation": "substring(.//*[contains(@class,'breadcrumb ')],9,100)",
        "content": ".//*[@class='articleCon']/descendant::p/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='KEYWords']/@content"
    },
    {
        "title": "normalize-space(.//*[contains(@class,'disbt')]//*[@class='fz26'])",
        "news_date": "normalize-space(.//*[contains(@class,'disbt')]//*[@class='mgr20'])",
        "source": "",
        "author": "",
        "navigation": "normalize-space(.//*[contains(@class,'nav')]//*[@class='active'])",
        "content": ".//*[@class='articleDetails']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@id='articleTitle'])",
        "news_date": "normalize-space(.//*[@id='articleTime'])",
        "source": "normalize-space(.//*[@id='articleSource'])",
        "author": "",
        "navigation": "substring-after(normalize-space(.//*[contains(text(),'您现在的位置')]),'现在的位置：')",
        "content": ".//*[@class='content']/descendant::p/text()",
        "editor": "",
        "tags": ".//*[@name='KEYWords']/@content"
    },
    {
        "title": "normalize-space(.//*[contains(@class,'newsPage-box-title')])",
        "news_date": "normalize-space(.//*[@class='time'])",
        "source": "normalize-space(.//*[@class='name'])",
        "author": "",
        "navigation": "",
        "content": ".//*[@class='newsPage-box-cont']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d*[/]*\d*\.[s]*htm[l]*'

