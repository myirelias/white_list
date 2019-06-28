# 江西省人民政府
TASK_NAME = 'jiangxi'

# 起始URL
START_URL = 'http://www.jiangxi.gov.cn/'

# 控制域，必须为list格式
DOMAIN = ['jiangxi']
# 请求头
HEADERS = {
    'Host': 'www.jiangxi.gov.cn',
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
        "title": "normalize-space(.//*[contains(@class,'con-title')])",
        "news_date": "substring-after(.//*[contains(text(),'发布时间')],'发布时间：')",
        "source": "substring-after(.//*[contains(text(),'来源')],'来源：')",
        "author": "",
        "navigation": "substring-after(normalize-space(.//*[@class='bt-position']),'当前位置：')",
        "content": ".//*[@id='zoom']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='Keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[contains(@class,'orig-title')])",
        "news_date": "substring-after(normalize-space(.//*[contains(text(),'日期')]),'日期：')",
        "source": "substring-after(normalize-space(.//*[contains(text(),'来源')]),'来源：')",
        "author": "",
        "navigation": "normalize-space(.//*[@class='path'])",
        "content": ".//*[contains(@class,'article_content')]/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[contains(text(),'编辑')]),'编辑：')",
        "tags": ".//*[@name='Keywords']/@content"
    },
    {
        "title": "normalize-space(.//h1[@class='text-center'])",
        "news_date": "substring-after(normalize-space(.//*[contains(text(),'发布时间')]),'发布时间：')",
        "source": "",
        "author": "",
        "navigation": "substring-after(normalize-space(.//*[@class='path']),'当前位置：')",
        "content": ".//*[contains(@class,'article-box')]/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='Keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d*/\d*/\d*/\w*_\d*_\d*\.[s]*htm[l]*'

