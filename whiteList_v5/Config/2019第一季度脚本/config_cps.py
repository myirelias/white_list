# 安防网
TASK_NAME = 'cps'

# 起始URL
START_URL = 'http://www.cps.com.cn/'

# 控制域，必须为list格式
DOMAIN = ['cps']
# 请求头
HEADERS = {
    'Host': 'www.cps.com.cn',
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
        "title": "string(.//*[@class='view-detail']/h2)",
        "news_date": "substring-before(.//*[@class='view-detail']/h3,'来源')",
        "source": "substring-after(.//*[contains(text(),'来源')],':')",
        "author": "substring-after(.//*[contains(text(),'作者')],'：')",
        "navigation": "string(.//*[@class='c-path'])",
        "content": ".//*[@class='view-detail']/descendant::p/text()",
        "editor": "substring-after(.//*[contains(text(),'编辑')],':')",
        "tags": ".//*/head/title/text()"
    },
    {
        "title": "string(.//*[@class='h1_h1'])",
        "news_date": ".//*[@class='news-t3']/span[1]/text()",
        "source": "substring-after(.//*[contains(text(),'来源')],':')",
        "author": "substring-after(.//*[contains(text(),'作者')],':')",
        "navigation": "string(.//*/h3)",
        "content": ".//*[@class='news-t4']/descendant::text()",
        "editor": "substring-after(.//*[contains(text(),'责任编辑')],':')",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{4,8}[/]*\d{0,4}/\d*\.[s]*htm[l]*'

