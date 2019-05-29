# 光明网
TASK_NAME = 'gmw'

# 起始URL
START_URL = 'http://www.gmw.cn/'

# 控制域，必须为list格式
DOMAIN = ['gmw']

# 请求头
HEADERS = {
    'Host': 'www.gmw.cn',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:52.0) Gecko/20100101 Firefox/52.0',
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
#     "tags": "",
# },
XPATHER_NEWS_LIST = [
    {
        "title": ".//*[@id='articleTitle']/text()",
        "news_date": ".//*[@id='pubTime']/text()",
        "source": "substring-after(.//*[@id='source'],'来源：')",
        "author": "",
        "navigation": "normalize-space(.//*[@id='contentBreadcrumbs2'])",
        "content": ".//*[@id='contentMain']/descendant::text()",
        "editor": ".//*[@id='contentLiability']/text()",
        "tags": ".//*[@name='keywords']/@content",
    },
    {
        "title": "normalize-space(.//*[@class='picContentHeading'])",
        "news_date": "normalize-space(.//*[@id='pubTime'])",
        "source": "substring-after(normalize-space(.//*[@id='source']),'来源：')",
        "author": "",
        "navigation": "normalize-space(.//*[@class='picContent-breadCrumbs2'])",
        "content": ".//*[@class='ArticleContentBox']/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[contains(text(),'责任编辑')]),'编辑：')",
        "tags": ".//*[@name='keywords']/@content",
    },
    {
        "title": "normalize-space(.//*[@class='hd']//h1)",
        "news_date": "",
        "source": "",
        "author": "",
        "navigation": "",
        "content": ".//*[@class='bd']/descendant::text()",
        "editor": "translate(substring-after(.//*[@id='contentLiability'],'编辑:'),']','')",
        "tags": ".//*[@name='keywords']/@content",
    },
    {
        "title": "normalize-space(.//*[@class='main_article']/h1)",
        "news_date": "substring-after(normalize-space(.//*[contains(text(),'发布时间')]),'发布时间：')",
        "source": "substring-after(normalize-space(.//*[contains(text(),'来源')]),'来源：')",
        "author": "",
        "navigation": "normalize-space(.//*[@class='bread_crumb'])",
        "content": ".//*[@class='article_detail']/descendant::text()",
        "editor": "translate(substring-after(normalize-space(.//*[contains(text(),'责任编辑')]),'责任编辑:'),']','')",
        "tags": ".//*[@name='keywords']/@content",
    },
    {
        "title": "normalize-space(.//*[@class='main']//h3)",
        "news_date": "substring-after(normalize-space(.//*[@class='xinxi']//*[contains(text(),'时间')]),'时间：')",
        "source": "substring-after(normalize-space(.//*[@class='xinxi']//*[contains(text(),'来源')]),'来源：')",
        "author": "substring-after(normalize-space(.//*[@class='xinxi']//*[contains(text(),'作者')]),'作者：')",
        "navigation": "normalize-space(.//*[@class='position'])",
        "content": ".//*[@class='content']/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[contains(text(),'责任编辑')]),'责任编辑：')",
        "tags": ".//*[@name='keywords']/@content",
    },
]

# 正则匹配规则
REGEX_URL = r'/\d{4}-\d{2}/\d{2}/\w+_\d+.htm'
