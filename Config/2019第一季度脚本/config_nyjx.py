# 中国农业机械网
TASK_NAME = 'nyjx'

# 起始URL
START_URL = 'http://www.nyjx.cn/'

# 控制域，必须为list格式
DOMAIN = ['nyjx']
# 请求头
HEADERS = {
    'Host': 'www.nyjx.cn',
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
        "title": "string(.//*[@class='article-title']/h1)",
        "news_date": ".//*[contains(@class,'article-time')]/span[1]/text()",
        "source": "substring(normalize-space(.//*[contains(text(),'来源')]),4,20)",
        "author": "substring(normalize-space(.//*[contains(text(),'作者')]),4,20)",
        "navigation": "substring(normalize-space(.//*[@class='current-path']),6,50)",
        "content": ".//*[@class='article-conte-infor']/descendant::text()",
        "editor": "substring(normalize-space(.//*[contains(text(),'编辑')]),4,20)",
        "tags": "string(.//head/title)"
    },
    {
        "title": "string(.//*[@id='ArticleTit'])",
        "news_date": "substring(normalize-space(.//*[@id='ArtFrom']),10,21)",
        "source": "substring-before(normalize-space(substring-after(.//*[@id='ArtFrom'],'来源:')),'【')",
        "author": "",
        "navigation": "substring-after(.//*[@id='position'],'所在的位置：')",
        "content": ".//*[@id='ArticleCnt']/descendant::p/text()",
        "editor": "",
        "tags": "string(.//head/title)"
    },
    {
        "title": "string(.//*[contains(text(),'信息标题')]/following-sibling::td[1])",
        "news_date": "string(.//*[contains(text(),'发布日期')]/following-sibling::td[1])",
        "source": "string(.//*[contains(text(),'信息类型')]/following-sibling::td[1])",
        "author": "",
        "navigation": "substring-after(.//*[@class='current-path'],'当前位置：')",
        "content": ".//*[@class='article-conte-infor']/descendant::text()",
        "editor": "",
        "tags": "string(.//head/title)"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{4}/\d{2}/\d{2}/\w*\d*\.[s]*htm[l]*'

