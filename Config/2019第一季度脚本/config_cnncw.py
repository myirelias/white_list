# 南充新闻网
TASK_NAME = 'cnncw'

# 起始URL
START_URL = 'http://www.cnncw.cn/'

# 控制域，必须为list格式
DOMAIN = ['cnncw']
# 请求头
HEADERS = {
    'Host': 'www.cnncw.cn',
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
# },normalize-space(.//*[@id='88']/tbody/tr[1]/td/div)
XPATHER_NEWS_LIST = [
    {
        "title": "normalize-space(.//*[@class='article-content-title'])",
        "news_date": "normalize-space(.//*[starts-with(@class,'date')])",
        "source": "normalize-space(.//*[starts-with(@class,'source')])",
        "author": "",
        "navigation": "normalize-space(.//*[@class='column m-crumb'])",
        "content": ".//*[contains(@class,'article-detail-inner')]/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@id='88']/tbody/tr[1]/td/div)",
        "news_date": "substring-before(normalize-space(.//*[contains(text(),'来源')]),'来源')",
        "source": "substring-after(normalize-space(.//*[contains(text(),'来源')]),'来源：')",
        "author": "",
        "navigation": "substring-after(normalize-space(.//*[contains(text(),'您的位置')]),'您的位置：')",
        "content": ".//*[@id='88']/tbody/tr[3]/td/div/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{4}/\d{4}/\d*\.s*html*'

