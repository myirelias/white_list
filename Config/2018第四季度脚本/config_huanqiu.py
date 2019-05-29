# 环球网
TASK_NAME = 'huanqiu'

# 起始URL
START_URL = 'http://www.huanqiu.com/'

# 控制域，必须为list格式
DOMAIN = ['huanqiu']
# 请求头
HEADERS = {
    'Host': 'www.huanqiu.com',
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
#     "tags": "",
# },
XPATHER_NEWS_LIST = [
    {
        "title": ".//*[@class='tle']/text()",
        "news_date": ".//*[@class='la_t_a']/text()",
        "source": ".//*[@class='la_t_b']/descendant::text()",
        "author": "",
        "navigation": "string(.//*[@class='nav_left'])",
        "content": ".//*[@class='la_con']/descendant::text()",
        "editor": ".//*[@class='la_e_a']/text()",
        "tags": ".//*[@name='keywords']/@content",
    },
    {
        "title": "normalize-space(.//h1[@class='hd'])",
        "news_date": "normalize-space(.//*[@class='time'])",
        "source": "normalize-space(.//*[@class='from'])",
        "author": "",
        "navigation": "normalize-space(.//*[@class='breadCrumb'])",
        "content": ".//*[@id='img_txt']/descendant::text()",
        "editor": "normalize-space(.//*[@class='user'])",
        "tags": ".//*[@name='keywords']/@content",
    },
    {
        "title": "normalize-space(.//*[@class='conText']/h1)",
        "news_date": "normalize-space(.//*[@id='pubtime_baidu'])",
        "source": "normalize-space(.//*[@id='source_baidu'])",
        "author": "",
        "navigation": "normalize-space(.//*[@class='topPath'])",
        "content": ".//*[@id='text']/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[@id='editor_baidu']),'：')",
        "tags": ".//*[@name='keywords']/@content",
    },


]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{4}-\d{2}/\d+.[s]*htm[l]*'

