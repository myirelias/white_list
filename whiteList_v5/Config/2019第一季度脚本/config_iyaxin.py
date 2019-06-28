# 亚心网
TASK_NAME = 'iyaxin'

# 起始URL
START_URL = 'http://www.iyaxin.com/'

# 控制域，必须为list格式
DOMAIN = ['iyaxin']
# 请求头
HEADERS = {
    'Host': 'www.iyaxin.com',
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
        "title": ".//*[@class='htitle']/text()",
        "news_date": ".//*[@id='pubtime_baidu']/text()",
        "source": "substring-after(.//*[@id='source_baidu'],'来源：')",
        "author": "substring-after(.//*[@id='author_baidu'],'作者：')",
        "navigation": "string(.//*[@class='nav'])",
        "content": ".//*[@class='article-detail']/descendant::p/text()",
        "editor": "substring-after(.//*[@id='editor_baidu'],'：')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": ".//*[@id='thread_subject']/text()",
        "news_date": "substring-after(.//*[starts-with(@id,'authorposton')],'发表于')",
        "source": "",
        "author": "string(.//*[@class='authi'])",
        "navigation": "string(.//*[@class='nvhm']/parent::div)",
        "content": "string(.//*[starts-with(@id,'postmessage')])",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d*[/]*\d*[/]*\w*[-]*\d*[-]*\d*[-]*\d*\.[s]*htm[l]*'

