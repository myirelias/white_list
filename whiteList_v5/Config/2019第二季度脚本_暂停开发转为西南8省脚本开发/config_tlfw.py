# 吐鲁番新闻网
TASK_NAME = 'tlfw'

# 起始URL
START_URL = 'http://www.tlfw.net/'

# 控制域，必须为list格式
DOMAIN = ['tlfw']
# 请求头
HEADERS = {
    'Host': 'www.tlfw.net',
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
        "title": "normalize-space(.//*[@id='ArticleTit'])",
        "news_date": "substring(normalize-space(.//*[@id='ArtFrom']),1,12)",
        "source": "substring-after(normalize-space(.//*[@id='ArtFrom']),'来源：')",
        "author": "substring-before(substring-after(normalize-space(.//*[@id='ArtFrom']),'作者：'),'编辑')",
        "navigation": "substring-after(normalize-space(.//*[@id='contentnav']),'当前位置：')",
        "content": ".//*[@id='PrintTxt']/descendant::text()",
        "editor": "substring-before(substring-after(normalize-space(.//*[@id='ArtFrom']),'编辑：'),'来源')",
        "tags": ""
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/Info\.aspx\?ModelId=\d*&Id=\d*'


