# 台海网
TASK_NAME = 'taihainet'

# 起始URL
START_URL = 'http://www.taihainet.com/'

# 控制域，必须为list格式
DOMAIN = ['taihainet']
# 请求头
HEADERS = {
    'Host': 'www.taihainet.com',
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
        "title": "normalize-space(.//*[@class='wrapper']/h1)",
        "news_date": "normalize-space(.//time)",
        "source": "normalize-space(.//*[@class='source_baidu'])",
        "author": "normalize-space(.//*[@class='editors'])",
        "navigation": "substring-after(normalize-space(.//*[contains(@class,'list-path')]),'您现在的位置：')",
        "content": ".//*[@class='article-content']/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[@class='article-footer']),'责任编辑：')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='h1'])",
        "news_date": "normalize-space(.//*[@class='post-time'])",
        "source": "normalize-space(.//*[@class='source'])",
        "author": "",
        "navigation": "normalize-space(.//*[@class='crumb'])",
        "content": ".//*[@class='gallery-photo-description']/descendant::text()",
        "editor": "translate(normalize-space(.//*[@class='editor']),'责任编辑：','')",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/[\d-]*/\d*\.s*html*'


