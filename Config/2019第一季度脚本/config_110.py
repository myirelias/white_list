# 110法律咨询网
TASK_NAME = '110'

# 起始URL
START_URL = 'http://www.110.com/'

# 控制域，必须为list格式
DOMAIN = ['110']
# 请求头
HEADERS = {
    'Host': 'www.110.com',
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
        "title": "normalize-space(.//*[@class='lbox01']//*[@class='tit01'])",
        "news_date": "substring(normalize-space(.//*[contains(text(),'时间')]),4,16)",
        "source": "substring-before(substring-after(normalize-space(.//*[contains(text(),'来源')]),'来源:'),'点击')",
        "author": "",
        "navigation": "substring(normalize-space(.//*[@class='showpath']),6,50)",
        "content": ".//*[@class='con']/descendant::p/text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content",
    },
    {
        "title": "normalize-space(.//*[@class='main']//*/h1)",
        "news_date": "substring(normalize-space(.//*[contains(text(),'发布日期')]),6,14)",
        "source": "",
        "author": "substring-after(normalize-space(.//*[contains(text(),'作者')]),'作者：')",
        "navigation": "substring(normalize-space(.//*[@class='showpath']),6,50)",
        "content": ".//*[@class='left_con']/descendant::text()|.//*[@class='xwz']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content",
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\w*-\d*\.[s]*htm[l]*|/\d{4,8}/\d*\.[s]*htm[l]*'

