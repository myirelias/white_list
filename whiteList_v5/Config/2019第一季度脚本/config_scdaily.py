# 四川日报
TASK_NAME = 'scdaily'

# 起始URL
START_URL = 'https://www.scdaily.cn/'

# 控制域，必须为list格式
DOMAIN = ['scdaily']
# 请求头
HEADERS = {
    'Host': 'www.scdaily.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'If-Modified-Since': 'Thu, 21 Feb 2019 05:41:25 GMT',
    'If-None-Match': '"e4af6815a8c9d41:0"',
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
        "title": "normalize-space(.//*[@id='webreal_scol_title'])",
        "news_date": "normalize-space(.//*[@id='pubtime_baidu'])",
        "source": "substring(normalize-space(.//*[@id='source_baidu']),4,20)",
        "author": "substring(normalize-space(.//*[@id='author_baidu']),4,50)",
        "navigation": ".//*[@id='col3nav']/descendant::a/text()",
        "content": ".//*[@id='cbw_zw_text']/descendant::text()",
        "editor": "substring(normalize-space(.//*[@id='editor_baidu']),4,20)",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='news']//h1)",
        "news_date": "substring-after(normalize-space(.//*[contains(text(),'showdate')]/parent::p),')')",
        "source": "",
        "author": "",
        "navigation": "normalize-space(.//*[@class='flex-between']/li[2])",
        "content": ".//*[@class='news']/descendant::text()",
        "editor": "",
        "tags": ""
    },
    {
        "title": "normalize-space(.//*[@id='frameContent']/h3)",
        "news_date": "normalize-space(.//*[@class='tit3']/i)",
        "source": "normalize-space(.//*[@class='tit3']/b)",
        "author": "",
        "navigation": "",
        "content": ".//*[@id='frameContent']/descendant::text()",
        "editor": "",
        "tags": ""
    },

]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d*/\d*\.[s]*htm[l]*'

