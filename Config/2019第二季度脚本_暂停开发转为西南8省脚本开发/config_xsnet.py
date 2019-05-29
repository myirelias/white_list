# 萧山网
TASK_NAME = 'xsnet'

# 起始URL
START_URL = 'http://www.xsnet.cn/'

# 控制域，必须为list格式
DOMAIN = ['xsnet']
# 请求头
HEADERS = {
    'Host': 'www.xsnet.cn',
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
        "title": "normalize-space(.//*[@class='con_title'])",
        "news_date": "normalize-space(.//*[@class='time'])",
        "source": "substring-after(normalize-space(.//*[@class='confrom']),'来源：')   ",
        "author": "substring-before(substring-after(normalize-space(.//*[contains(@class,'con_edit')]),'作者：'),'编辑')",
        "navigation": "normalize-space(.//*[@class='navigate']/*[@class='rute'])",
        "content": ".//*[@class='xs_content']/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[contains(@class,'con_edit')]),'编辑：')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='article']/h2)",
        "news_date": "normalize-space(.//*[@class='publish-time'])",
        "source": "normalize-space(.//*[@class='border'])",
        "author": "",
        "navigation": "",
        "content": ".//*[@class='thread-model-txt']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d*[_/]\d*/\d*\.s*html*|/forum/index/detail/id/\d*\.s*html*'


