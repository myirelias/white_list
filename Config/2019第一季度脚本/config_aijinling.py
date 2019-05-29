# 金陵热线
TASK_NAME = 'aijinling'

# 起始URL
START_URL = 'http://www.aijinling.com/'

# 控制域，必须为list格式
DOMAIN = ['aijinling']
# 请求头
HEADERS = {
    'Host': 'www.aijinling.com',
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
        "title": "normalize-space(.//*[@class='titBox']/h1)",
        "news_date": "normalize-space(.//*[@class='txtinfo']/span[1])",
        "source": "normalize-space(.//*[@class='txtinfo']/span[2])",
        "author": "",
        "navigation": "normalize-space(.//*[@class='crumbs'])",
        "content": ".//*[@class='content']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='am-article-title blog-title'])",
        "news_date": "substring(normalize-space(.//*[contains(text(),'来源')]/parent::h4),1,20)",
        "source": "substring-after(normalize-space(.//*[contains(text(),'来源')]/parent::h4),'来源:')",
        "author": "",
        "navigation": "",
        "content": ".//*[contains(@class,'blog-content')]/descendant::text()",
        "editor": "translate(substring(normalize-space(.//*[contains(text(),'责任编辑')]),7,50),')','')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='title'])",
        "news_date": "substring-after(normalize-space(.//*[contains(text(),'时间')]/parent::span),'时间:')",
        "source": "substring-after(normalize-space(.//*[contains(text(),'来源')]/parent::span),'来源:')",
        "author": "",
        "navigation": "substring-after(normalize-space(.//*[@class='n-text']),'当前位置：')",
        "content": ".//*[@class='content']/descendant::text()",
        "editor": "translate(substring-after(normalize-space(.//*[contains(text(),'责任编辑')]),'责任编辑：'),')','')",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\w*\d*/*\d*\.s*html*|/[\d-]*/\.s*html*'

