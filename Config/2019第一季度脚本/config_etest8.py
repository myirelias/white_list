# 易考吧
TASK_NAME = 'etest8'

# 起始URL
START_URL = 'http://www.etest8.com/'

# 控制域，必须为list格式
DOMAIN = ['etest8']
# 请求头
HEADERS = {
    'Host': 'www.etest8.com',
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
        "title": "normalize-space(.//*[@id='neirongtitle']/h1)",
        "news_date": "substring(substring-before(normalize-space(.//*[@id='nrfrom']),'【'),7,20)",
        "source": "substring(substring-before(normalize-space(.//*[@id='nrfrom']),'【'),4,5)",
        "author": "",
        "navigation": "substring(normalize-space(.//*[contains(text(),'您现在的位置')]),8,200)",
        "content": ".//*[@class='cont']/descendant::p/text()",
        "editor": "substring-before(substring(normalize-space(.//*[contains(text(),'编辑')]),4,20),'【')",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d*\.s*html*'

