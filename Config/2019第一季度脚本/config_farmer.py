# 中国农业新闻网
TASK_NAME = 'farmer'

# 起始URL
START_URL = 'http://www.farmer.com.cn/'

# 控制域，必须为list格式
DOMAIN = ['farmer']
# 请求头
HEADERS = {
    'Host': 'www.farmer.com.cn',
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
        "title": "normalize-space(.//*[@class='wtitle'])",
        "news_date": "substring(normalize-space(.//*[@class='wlaiyuan']),1,16)",
        "source": "substring-after(normalize-space(.//*[@class='wlaiyuan']),'来源：')",
        "author": "substring-before(substring-after(normalize-space(.//*[@class='wlaiyuan']),'作者：'),'|')",
        "navigation": "normalize-space(.//*[@class='bread-crumbs-nav'])",
        "content": ".//*[@class='TRS_Editor']/descendant::text()",
        "editor": "substring-after(.//*[contains(text(),'责任编辑')],'责任编辑：')",
        "tags": ".//*[@name='Keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d*/\w*[\d-]*\.s*html*'

