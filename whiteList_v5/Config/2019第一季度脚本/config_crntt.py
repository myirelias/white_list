# 中评网
TASK_NAME = 'crntt'

# 起始URL
START_URL = 'http://www.crntt.com/'

# 控制域，必须为list格式
DOMAIN = ['crntt']
# 请求头
HEADERS = {
    'Host': 'www.crntt.com',
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
        "title": ".//*[@width='738']/descendant::tr[4]/descendant::text()|.//*[@id='doc_tb']/descendant::tr[1]/descendant::text()",  #
        "news_date": "substring-after(.//*[@width='738']/descendant::tr[5],'com')",
        "source": "substring-before(.//*[@width='738']/descendant::tr[5],' ')",
        "author": "",
        "navigation": "",
        "content": ".//*[@id='zoom']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d*\.[s]*htm[l]*|docid=\d*'

