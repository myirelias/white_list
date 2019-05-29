# 直销同城网
TASK_NAME = 'zx58'

# 起始URL
START_URL = 'https://www.zx58.cn/'

# 控制域，必须为list格式
DOMAIN = ['zx58']
# 请求头
HEADERS = {
    'Host': 'www.zx58.cn',
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
        "title": "normalize-space(.//*[@class='ns-news']//*[@class='tp'])",
        "news_date": "substring(normalize-space(.//*[@class='na']//*[contains(text(),'发布时间')]),6,50)",
        "source": "substring(normalize-space(.//*[@class='na']//*[contains(text(),'来源')]),4,50)",
        "author": "",
        "navigation": "substring-after(normalize-space(.//*[contains(@class,'contenttitle container')]),'当前位置：')",
        "content": ".//*[@class='txt']/descendant::text()",
        "editor": "substring(normalize-space(.//*[@class='na']//*[contains(text(),'责编')]),4,50)",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/news/\d*\.s*html*'


