# 天府社区
TASK_NAME = 'bbs_scol'

# 起始URL
START_URL = 'https://bbs.scol.com.cn/'

# 控制域，必须为list格式
DOMAIN = ['scol']
# 请求头
HEADERS = {
    'Host': 'bbs.scol.com.cn',
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
        "title": "normalize-space(.//*[@class='con_title'])",
        "news_date": "substring-before(normalize-space(.//*[@class='publish-time']),'|')",
        "source": "",
        "author": "substring-before(normalize-space(.//*[contains(@class,'J_fixed_show')]),'主题')",
        "navigation": "",
        "content": ".//*[@id='ct']//*[contains(@class,'con_lt')]//*[contains(@id,'postmessage')]/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/thread-\d*-1-\d*\.s*html*'

# 响应时间
# TIMEOUT = 20


