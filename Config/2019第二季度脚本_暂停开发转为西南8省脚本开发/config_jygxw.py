# 嘉峪关新闻网
TASK_NAME = 'jygxw'

# 起始URL
START_URL = 'http://www.jygxw.com/'

# 控制域，必须为list格式
DOMAIN = ['jygxw']
# 请求头
HEADERS = {
    'Host': 'www.jygxw.com',
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
        "title": "normalize-space(.//*[@class='content_con']/h1)",
        "news_date": "normalize-space(.//*[@class='content_con']/h3/span[2])",
        "source": "substring-after(normalize-space(.//*[contains(text(),'来源')]),'来源：')",
        "author": "substring-before(substring-after(normalize-space(.//*[@class='editor']),'作者：'),'责任编辑')",
        "navigation": "normalize-space(.//*[@class='content_tit'])",
        "content": ".//*[@class='content_editor']/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[@class='editor']),'责任编辑：')",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{4}-\d{2}/\d{2}/[\d_]*\.s*html*'


