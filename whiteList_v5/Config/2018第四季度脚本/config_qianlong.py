# 千龙网
TASK_NAME = 'qianlong'

# 起始URL
START_URL = 'http://www.qianlong.com/'

# 控制域，必须为list格式
DOMAIN = ['qianlong']
# 请求头
HEADERS = {
    'Host': 'travel.qianlong.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://travel.qianlong.com/',
    'Cookie': 'Hm_lvt_b11cd5ab92cec77fc45294d9db6d5cd8=1524186307; Hm_lpvt_b11cd5ab92cec77fc45294d9db6d5cd8=1524187033; __cfduid=d8016af11b94cfe095e74d763870ff7d81524186724; vjuids=481725d20.162e09cb260.0.50fca7d3230b6; vjlast=1524186788.1524186788.30; __asc=d73b5e27162e09eec04864d8543; __auc=d73b5e27162e09eec04864d8543',
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
#     "tags": "",
# },
XPATHER_NEWS_LIST = [
    {
        "title": "string(.//*[@class='row title'])",
        "news_date": ".//*[@class='pubDate']/text()",
        "source": "string(.//*[@class='source'])",
        "author": "",
        "navigation": "",
        "content": ".//*[@class='article-content']/descendant::text()",
        "editor": "substring-after(.//*[contains(text(),'编辑')],'编辑：')",
        "tags": ".//*[@name='keywords']/@content",
    },
    {
        "title": "normalize-space(.//*[contains(@class,'media-heading')])",
        "news_date": "substring-after(normalize-space(.//*[contains(text(),'创建时间')]),'创建时间：')",
        "source": "",
        "author": "",
        "navigation": "",
        "content": ".//*[contains(@class,'article-content')]/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content",
    },
    {
        "title": "normalize-space(.//*[@class='row title']//h1)",
        "news_date": "normalize-space(.//*[@class='pubDate'])",
        "source": "normalize-space(.//*[@class='source'])",
        "author": "",
        "navigation": "",
        "content": ".//*[@class='article-content']/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[@class='editor']),'编辑：')",
        "tags": ".//*[@name='keywords']/@content",
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{4}/\d{4}/\d+\.[s]*htm[l]*'
