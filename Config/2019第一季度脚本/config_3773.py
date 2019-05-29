# 老钱庄
TASK_NAME = '3773'

# 起始URL
START_URL = 'http://www.3773.com.cn/'

# 控制域，必须为list格式
DOMAIN = ['3773']
# 请求头
HEADERS = {
    'Host': 'www.3773.com.cn',
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
        "title": "normalize-space(.//*[@class='titbox2']/h1)",
        "news_date": "substring(substring-after(normalize-space(.//*[contains(text(),'来源')]),'['),1,9)",
        "source": "substring-before(substring-after(normalize-space(.//*[contains(text(),'来源')]),'来源:'),'[')",
        "author": "",
        "navigation": "normalize-space(.//*[@class='location'])",
        "content": ".//*[@id='ArticleCnt']/descendant::p/text()",
        "editor": "",
        "tags": ".//*[@name='Keywords']/@content"
    },
    {
        "title": "normalize-space(.//h1|.//title)",
        "news_date": "substring(normalize-space(.//*[contains(text(),'来源')]/parent::td),12,20)",
        "source": "substring-after(.//*[contains(text(),'来源')],'来源:')",
        "author": "",
        "navigation": "normalize-space(.//*[@class='LinkPath']/parent::td)",
        "content": ".//*[@id='ArticleCnt']/descendant::p/text()",
        "editor": "",
        "tags": ".//*[@name='Keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d*\.s*html*'

