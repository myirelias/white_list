# 北国网
TASK_NAME = 'lnd'

# 起始URL',
START_URL = 'http://www.lnd.com.cn/'

# 控制域，必须为list格式
DOMAIN = ['lnd']
# 请求头
HEADERS = {
    'Host': 'www.lnd.com.cn',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:52.0) Gecko/20100101 Firefox/52.0',
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
        "title": ".//*[contains(@class,'newstittle')]/text()",
        "news_date": ".//*[@class='newsly']/descendant::span[2]/text()",
        "source": ".//*[@class='grey']/text()",
        "author": ".//*[@class='newsly']/descendant::span[4]/text()",
        "navigation": ".//*[@class='newsly']/descendant::font/text()",
        "content": ".//*[@class='news']/descendant::text()",
        "editor": ".//*[@class='newsly']/descendant::span[5]/text()",
        "tags": ".//*[@name='Keywords']/@content",
    },
    {
        "title": ".//*/h1[@class='p_center']/text()",
        "news_date": ".//*[@id='pubtime_baidu']/text()",
        "source": "substring-after(.//*[@id='source_baidu'],'来源：')",
        "author": "substring-after(.//*[@id='author_baidu'],'作者：')",
        "navigation": "string(.//*[@class='nfd'])",
        "content": ".//*[@class='news']/descendant::text()",
        "editor": "substring-after(.//*[@id='editor_baidu'],'编辑：')",
        "tags": ".//*[@name='Keywords']/@content",
    }
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{4}-\d{2}/\d{2}/\w+_\d+\.[s]*htm[l]*'
