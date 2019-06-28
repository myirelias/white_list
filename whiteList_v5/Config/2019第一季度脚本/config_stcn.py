# 证券时报网
TASK_NAME = 'stcn'

# 起始URL
START_URL = 'http://www.stcn.com/'

# 控制域，必须为list格式
DOMAIN = ['stcn']
# 请求头
HEADERS = {
    'Host': 'www.stcn.com',
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
        "title": "normalize-space(.//*[@class='intal_tit']/h2|.//h2/self::h2)",
        "news_date": "substring-before(normalize-space(.//*[@class='info']),'来源')",
        "source": "translate(substring-after(normalize-space(.//*[@class='info']),'来源：'),'作者：','')",
        "author": "substring-after(normalize-space(.//*[@class='info']),'作者：')",
        "navigation": "substring(normalize-space(.//*[@class='website']),8,100)",
        "content": ".//*[@class='txt_con']/descendant::text()|.//*[@class='text1']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    }
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d*/\d*/\d*\.[s]*htm[l]*'

