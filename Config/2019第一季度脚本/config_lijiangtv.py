# 巴中传媒网
TASK_NAME = 'lijiangtv'

# 起始URL
START_URL = 'https://www.lijiangtv.com/'

# 控制域，必须为list格式
DOMAIN = ['lijiangtv']
# 请求头
HEADERS = {
    'Host': 'www.lijiangtv.com',
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
        "title": "normalize-space(.//*[@id='title'])",
        "news_date": "substring(normalize-space(.//*[@id='ct']//*[@class='xg1']),1,15)",
        "source": "substring-before(substring-after(normalize-space(.//*[@id='ct']//*[@class='xg1']),'来自:'),'【')",
        "author": "substring-before(substring-after(normalize-space(.//*[@id='ct']//*[@class='xg1']),'原作者:'),'|')",
        "navigation": "normalize-space(.//*[@id='pt'])",
        "content": ".//*[@id='content']/descendant::p/text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='mui-content']/h4)",
        "news_date": "substring(normalize-space(.//*[@class='link-after-title']),1,10)",
        "source": "normalize-space(.//*[@class='link-after-title']//*[@class='a-link'])",
        "author": "substring-before(substring-after(normalize-space(.//*[contains(text(),'作者')]),'作者：'),'来源')",
        "navigation": "",
        "content": ".//*[@id='article-content']/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[contains(text(),'编辑')]),'编辑：')",
        "tags": ""
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d*-\w*-\d*\.[s]*htm[l]*'

