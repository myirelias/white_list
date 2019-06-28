# 贵阳新闻
TASK_NAME = 'gywb'

# 起始URL
START_URL = 'http://www.gywb.cn/'

# 控制域，必须为list格式
DOMAIN = ['gywb']
# 请求头
HEADERS = {
    'Host': 'www.gywb.cn',
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
        "title": "normalize-space(.//*[contains(@class,'g-content-t')])",
        "news_date": "substring-after(normalize-space(.//*[@id='pubtime_baidu']),'发布时间：')",
        "source": "substring-after(normalize-space(.//*[@id='source_baidu']),'来源：')",
        "author": "",
        "navigation": "normalize-space(.//*[@class='breadcrumb'])",
        "content": ".//*[@class='g-content-c']/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[@id='editor_baidu']),'责任编辑：')",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{4}-\d{2}/\d*/content_\d*\.s*html*'

