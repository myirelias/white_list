# 中国文化传媒网
TASK_NAME = 'ccdy'

# 起始URL
START_URL = 'http://www.ccdy.cn/'

# 控制域，必须为list格式
DOMAIN = ['ccdy']
# 请求头
HEADERS = {
    'Host': 'www.ccdy.cn',
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
        "title": "normalize-space(.//h1)",
        "news_date": "normalize-space(.//*[@class='info']/span[1])",
        "source": "substring(normalize-space(.//*[contains(text(),'文章来源')]),6,50)",
        "author": "",
        "navigation": "substring(normalize-space(.//*[@class='main']),6,50)",
        "content": ".//*[@class='TRS_Editor']//*[not(@id='_Custom_V6_Style_')]/descendant::text()",
        "editor": "substring(normalize-space(.//*[contains(text(),'责任编辑')]),6,50)",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{4,8}/\w*\d*_\d*\.[s]*htm[l]*'

