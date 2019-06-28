# 北青网
TASK_NAME = 'ynet'

# 起始URL
START_URL = 'http://www.ynet.com/index.html'

# 控制域，必须为list格式
DOMAIN = ['ynet']
# 请求头
HEADERS = {
    'Host': 'www.ynet.com',
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
        "title": "normalize-space(.//*[@class='articleTitle']/h1)",
        "news_date": "substring(normalize-space(.//*[@class='sourceBox']),1,18)",
        "source": "normalize-space(.//*[@class='sourceMsg'])",
        "author": "normalize-space(.//*[@class='authorMsg'])",
        "navigation": "normalize-space(.//*[contains(@class,'detailSubNav')])",
        "content": ".//*[@id='articleBox']/descendant::p/text()",
        "editor": "substring(normalize-space(.//*[@class='authors']),6,50)",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{4}/\d{2}/\d{2}/[\d\w]*\.s*html*'

