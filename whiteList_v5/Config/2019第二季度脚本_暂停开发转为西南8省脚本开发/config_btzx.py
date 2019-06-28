# 兵团在线
TASK_NAME = 'btzx'

# 起始URL
START_URL = 'http://www.btzx.com.cn/'

# 控制域，必须为list格式
DOMAIN = ['btzx']
# 请求头
HEADERS = {
    'Host': 'www.btzx.com.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'http://www.btzx.com.cn/',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Content-Length': '0',
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
        "title": "normalize-space(.//*[@class='content_title'])",
        "news_date": "normalize-space(.//*[@class='content_date'])",
        "source": "substring(normalize-space(.//*[@class='content_from']),4,50)",
        "author": "",
        "navigation": "",
        "content": ".//*[@class='content']//*[@class='con']/descendant::text()",
        "editor": "substring(normalize-space(.//*[@class='content_edit']),4,50)",
        "tags": ".//*[contains(@name,'eywords')]/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'(/\d*){3}/[\w\d]*\.s*html*'

