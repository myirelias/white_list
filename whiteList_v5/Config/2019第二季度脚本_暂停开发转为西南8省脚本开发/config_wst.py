# 无锡二泉网
TASK_NAME = 'wst'

# 起始URL
START_URL = 'http://www.wst.cn/'

# 控制域，必须为list格式
DOMAIN = ['wst']
# 请求头
HEADERS = {
    'Host': 'www.wst.cn',
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
        "title": "normalize-space(.//*[contains(@class,'content_left')]/h1)",
        "news_date": "substring-after(normalize-space(.//*[@class='lab']),'更新时间：')",
        "source": "",
        "author": "",
        "navigation": "",
        "content": ".//*[@class='main']/descendant::text()",
        "editor": "",
        "tags": ""
    },
    {
        "title": "substring-before(normalize-space(.//*[@id='Article']/h1),'2')",
        "news_date": "concat(2,substring(substring-after(normalize-space(.//*[@id='Article']/h1),'2'),1,20))",
        "source": "substring-before(substring-after(normalize-space(.//*[@id='Article']/h1),'来源：'),'点击')",
        "author": "",
        "navigation": "normalize-space(.//*[@class='crumbs'])",
        "content": ".//*[@class='content']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@id='thread_subject'])",
        "news_date": ".//*[@id='postlist']/*[contains(@id,'post_')][1]//*[@class='pti']//*[starts-with(@id,'authorposton')]/span/@title",
        "source": "",
        "author": "normalize-space(.//*[@id='postlist']/*[contains(@id,'post_')][1]//*[@class='pi']/*[@class='authi'])",
        "navigation": "normalize-space(.//*[@class='nvhm']/parent::div)",
        "content": ".//*[@id='postlist']/*[contains(@id,'post_')][1]//*[@class='pcb']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/thread[\d-]*\.s*html*|/\d{4}/news_\d*/\d*\.s*html*|/\d{4}/\d{2}/\d*\.s*html*'


