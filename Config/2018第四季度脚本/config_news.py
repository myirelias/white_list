# 新华网
TASK_NAME = 'news'

# 起始URL
START_URL = 'http://www.news.cn/'

# 控制域，必须为list格式
DOMAIN = ['news']
# 请求头
HEADERS = {
    'Host': 'www.news.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
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
        "title": ".//*[@class='h-title']/text()",
        "news_date": ".//*[@class='h-time']/text()",
        "source": "substring-after(.//*[@class='h-info'], '来源：')",
        "author": "",
        "navigation": "string(.//*[@class='news-position'])",
        "content": ".//*[@id='p-detail']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content",
    },
    {
        "title": ".//*[@id='title']/text()",
        "news_date": ".//*[@id='pubtime']/text()",
        "source": ".//*[@id='source']/text()",
        "author": "",
        "navigation": "",
        "content": ".//*[@id='content']/descendant::p/text()",
        "editor": "substring-after(.//*[@class='editor'],'编辑:')",
        "tags": ".//*[@name='keywords']/@content",
    },
    {
        "title": ".//*/h3/text()",
        "news_date": ".//*[@class='thedate2']/text()",
        "source": "",
        "author": "",
        "navigation": "",
        "content": ".//*[@class='txt_zw']/descendant::p/text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content",
    },
    {
        "title": "normalize-space(.//*[@class='tit'])",
        "news_date": "concat(2,substring-after(normalize-space(.//*[contains(@class,'source')]),'2'))",
        "source": "substring-before(normalize-space(.//*[contains(@class,'source')]),'2')",
        "author": "",
        "navigation": "normalize-space(.//*[contains(@class,'list-detail')]/h3[1])",
        "content": ".//*[@class='detailcon']/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[@class='author']),'：')",
        "tags": ".//*[@name='keywords']/@content",
    },

]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/[\w]*[_]*\d*[_]*\d*\.[s]*htm[l]*'

