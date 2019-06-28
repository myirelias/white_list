# 我爱卡网
TASK_NAME = '51credit'

# 起始URL
START_URL = 'https://www.51credit.com/'

# 控制域，必须为list格式
DOMAIN = ['51credit']
# 请求头
HEADERS = {
    'Host': 'www.51credit.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
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
        "title": "normalize-space(.//*[@class='title-big'])",
        "news_date": "normalize-space(.//*[@class='autho-l']/span[2])",
        "source": "normalize-space(.//*[@class='autho-l']/span[1])",
        "author": "",
        "navigation": "normalize-space(.//*[@class='crumbs-nav'])",
        "content": ".//*[@class='content']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='cont']/h2)",
        "news_date": "substring(.//*[contains(text(),'发布时间')],6,50)",
        "source": "",
        "author": "",
        "navigation": "normalize-space(.//*[@class='pos'])",
        "content": ".//*[@class='cont']/descendant::p/text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[contains(@class,'con_box')]//*[@class='tc'])",
        "news_date": "substring(normalize-space(.//*[@class='con_time tc']),1,12)",
        "source": "substring(substring-after(normalize-space(.//*[@class='con_time tc']),'来源：'),1,5)",
        "author": "",
        "navigation": "normalize-space(.//*[contains(@class,'con_Breadcrumbs')])",
        "content": ".//*[contains(@class,'con_content')]/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[@class='con_time tc']),'小编：')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='cd_con']//*[@class='tc'])",
        "news_date": "substring-after(normalize-space(.//*[@class='time tc']),'发布时间：')",
        "source": "substring(substring-after(normalize-space(.//*[@class='time tc']),'来源：'),1,6)",
        "author": "",
        "navigation": "substring-after(normalize-space(.//*[@class='cd_hxnav']),'当前位置：')",
        "content": ".//*[@class='cd_conbox']/descendant::text()",
        "editor": "substring-before(substring-after(normalize-space(.//*[@class='time tc']),'小编：'),'发布时间')",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d*\.s*html*'

