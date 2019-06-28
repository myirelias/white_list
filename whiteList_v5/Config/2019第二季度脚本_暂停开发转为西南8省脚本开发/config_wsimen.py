# 泗门生活网
TASK_NAME = 'wsimen'

# 起始URL
START_URL = 'http://www.wsimen.com/'

# 控制域，必须为list格式
DOMAIN = ['wsimen']
# 请求头
HEADERS = {
    'Host': 'www.wsimen.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://www.wsimen.com/',
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
        "title": "normalize-space(.//*[@class='ph'])",
        "news_date": "substring-before(normalize-space(.//*[@id='ct']//*[@class='xg1']),'|')",
        "source": "substring-after(normalize-space(.//*[@id='ct']//*[@class='xg1']),'来自:')",
        "author": "substring-before(substring-after(normalize-space(.//*[@id='ct']//*[@class='xg1']),'作者:'),'|')",
        "navigation": "normalize-space(.//*[@class='nvhm']/parent::div)",
        "content": ".//*[@id='article_content']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/article[\d-]*\.s*html*'


