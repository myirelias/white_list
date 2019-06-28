# 新疆兴农网
TASK_NAME = 'xjxnw'

# 起始URL
START_URL = 'http://www.xjxnw.gov.cn/'

# 控制域，必须为list格式
DOMAIN = ['xjxnw']
# 请求头
HEADERS = {
    'Host': 'www.xjxnw.gov.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Cookie': '14_vq=13',
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
        "title": "normalize-space(.//*[@class='container']/descendant::h3)",
        "news_date": "substring(normalize-space(.//*[@class='m-b-sm']),1,19)",
        "source": "substring-before(substring(normalize-space(.//*[@class='m-b-sm']),19,50),' ')",
        "author": "",
        "navigation": "normalize-space(.//*[@class='p-sm m-t-xs b-b b-light'])",
        "content": ".//*[@class='m-lg']/descendant::text()",
        "editor": "",
        "tags": ""
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{4}-\d{2}-\d{2}/\d*\.[s]*htm[l]*'

