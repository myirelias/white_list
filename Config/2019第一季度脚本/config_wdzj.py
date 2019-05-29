# 网贷之家
TASK_NAME = 'wdzj'

# 起始URL
START_URL = 'https://www.wdzj.com/'

# 控制域，必须为list格式
DOMAIN = ['wdzj']
# 请求头
HEADERS = {
    'Host': 'www.wdzj.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
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
        "title": "normalize-space(.//*[@class='page-title'])",
        "news_date": "normalize-space(.//*[@class='page-time']//*[contains(text(),'-')])",
        "source": "substring-before(substring-after(normalize-space(.//*[@class='page-time']),'来源：'),'|')",
        "author": "substring-before(substring-after(normalize-space(.//*[@class='page-time']),'作者：'),'|')",
        "navigation": "normalize-space(.//*[@class='page-breadcrumb'])",
        "content": ".//*[@class='page-content']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/[\d-]*\.[s]*htm[l]*'

