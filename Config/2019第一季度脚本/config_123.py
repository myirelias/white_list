# 云掌财经
TASK_NAME = '123'

# 起始URL
START_URL = 'http://www.123.com.cn/'

# 控制域，必须为list格式
DOMAIN = ['123']
# 请求头
HEADERS = {
    'Host': 'www.123.com.cn',
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
        "title": ".//*/h1/text()",
        "news_date": "substring-before(.//*[contains(text(),'来源')],'来源')",
        "source": "substring-after(.//*[contains(text(),'来源')],'来源：')",
        "author": "",
        "navigation": "string(.//*[@class='channel-site'])",
        "content": ".//*[@id='gb_article_body']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "string(.//*[@class='name'])",
        "news_date": ".//*[starts-with(@class,'bottom')]//*[@class='fl']/text()",
        "source": "",
        "author": "",
        "navigation": "string(.//*[contains(@class,'position')])",
        "content": ".//*[@class='text']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "string(.//*[@class='zl-title'])",
        "news_date": "substring-after(.//*[starts-with(@class,'times')],'●')",  # 这个分隔符 第一次用
        "source": "substring-before(.//*[starts-with(@class,'times')],'●')",
        "author": "",
        "navigation": "string(.//*[contains(@class,'position')])",
        "content": ".//*[@class='kline_text']/descendant::p/text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },

]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d*[-]*\d*\.[s]*htm[l]*'

