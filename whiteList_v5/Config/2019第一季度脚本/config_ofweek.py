# 维科网
TASK_NAME = 'ofweek'

# 起始URL
START_URL = 'https://www.ofweek.com/'

# 控制域，必须为list格式
DOMAIN = ['ofweek']
# 请求头
HEADERS = {
    'Host': 'www.ofweek.com',
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
        "title": "normalize-space(.//*[@class='article_left']//h1)",
        "news_date": "normalize-space(.//*[@class='sdate'])",
        "source": "substring(normalize-space(.//*[@id='laiyuan_mp']),4,200)",
        "author": "",
        "navigation": "substring(normalize-space(.//*[@class='position gray']),6,200)",
        "content": ".//*[@class='article_con']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='Keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d*-\d*/\w*[-\d]*\.s*html*'

