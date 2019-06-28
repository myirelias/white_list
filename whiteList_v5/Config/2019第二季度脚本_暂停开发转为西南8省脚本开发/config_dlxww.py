# 大连新闻网
TASK_NAME = 'dlxww'

# 起始URL
START_URL = 'http://www.dlxww.com/'

# 控制域，必须为list格式
DOMAIN = ['dlxww']
# 请求头
HEADERS = {
    'Host': 'www.dlxww.com',
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
        "title": "normalize-space(.//*[@class='page_content']/descendant::h1[1])",
        "news_date": "substring(normalize-space(.//*[@class='page_tools']),1,16)",
        "source": "substring(normalize-space(.//*[@class='page_tools']),18,50)",
        "author": "",
        "navigation": "normalize-space(.//*[@class='dqwz'])",
        "content": ".//*[@class='page_maincontent']/descendant::text()",
        "editor": "",
        "tags": ""
    },
    {
        "title": "normalize-space(.//*[@class='bigbiaoti'])",
        "news_date": "substring(concat(2,substring-after(normalize-space(.//*[@class='cx1']),'2')),1,10)",
        "source": "substring-before(substring-after(normalize-space(.//*[@class='cx1']),'来源：'),2)",
        "author": "",
        "navigation": "",
        "content": ".//*[@id='table14']/tbody/tr[2]/td/table/tbody/tr[last()]/descendant::text()",
        "editor": "",
        "tags": ""
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{4}-\d{2}/\d{2}/\w*_\d*\.s*html*'


