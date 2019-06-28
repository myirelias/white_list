# 太平洋汽车网
TASK_NAME = 'pcauto'

# 起始URL
START_URL = 'https://www.pcauto.com.cn/'

# 控制域，必须为list格式
DOMAIN = ['pcauto']
# 请求头
HEADERS = {
    'Host': 'www.pcauto.com.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
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
        "title": "normalize-space(.//h1[@class='tit'])",
        "news_date": "normalize-space(.//*[@id='pubtime_baidu'])",
        "source": "substring-after(normalize-space(.//*[@id='source_baidu']),'来源：')",
        "author": "substring-after(normalize-space(.//*[@id='author_baidu']),'作者：')",
        "navigation": "normalize-space(.//*[@class='pos-mark'])",
        "content": ".//*[contains(@class,'artText')]/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='title'])",
        "news_date": "normalize-space(.//*[@class='muted update'])",
        "source": "",
        "author": "",
        "navigation": "",
        "content": ".//*[@class='content']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\w*/\d*/\d*\.s*html*'

