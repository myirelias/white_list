# 比特网
TASK_NAME = 'chinabyte'

# 起始URL
START_URL = 'http://www.chinabyte.com/'

# 控制域，必须为list格式
DOMAIN = ['chinabyte']
# 请求头
HEADERS = {
    'Host': 'www.chinabyte.com',
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
        "title": "normalize-space(.//*[@class='hot_art']/h1)",
        "news_date": "normalize-space(.//*[@class='utime'])",
        "source": "substring(normalize-space(.//*[@class='classify']),4,50)",
        "author": "substring(normalize-space(.//*[@class='author']),4,50)",
        "navigation": "normalize-space(.//*[@class='sec_nav'])",
        "content": ".//*[@class='art_txt']/descendant::p/text()",
        "editor": "normalize-space(.//*[@id='editor_baidu'])",
        "tags": ""
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d*/\d*\.s*html*'


