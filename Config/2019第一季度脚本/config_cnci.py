# 中国文化产业网
TASK_NAME = 'cnci'

# 起始URL
START_URL = 'http://www.cnci.net.cn/'

# 控制域，必须为list格式
DOMAIN = ['cnci']
# 请求头
HEADERS = {
    'Host': 'www.cnci.net.cn',
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
        "title": "normalize-space(.//*[@class='commonDetailedtitle']/h3)",
        "news_date": "substring(normalize-space(.//*[@class='commonDetailedtitleTimeAuthor']),1,14)",
        "source": "substring-before(substring-after(normalize-space(.//*[@class='commonDetailedtitleTimeAuthor']),'来源：'),'编辑')",
        "author": "",
        "navigation": "normalize-space(.//*[starts-with(@class,'title')])",
        "content": ".//*[@class='commonDetailedContents']/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[@class='commonDetailedtitleTimeAuthor']),'编辑：')",
        "tags": ".//*[@name='Keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{4}-\d{2}/\d{2}/\w*_\d*\.s*html*'

