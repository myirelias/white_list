# 中国财经时报网
TASK_NAME = '3news'

# 起始URL
START_URL = 'http://www.3news.cn/'

# 控制域，必须为list格式
DOMAIN = ['3news']
# 请求头
HEADERS = {
    'Host': 'www.3news.cn',
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
        "title": "normalize-space(.//*[@class='title'])",
        "news_date": "substring-after(normalize-space(.//*[@class='source']),'发布时间：')",
        "source": "substring-before(substring-after(normalize-space(.//*[@class='source']),'来源：'),'发布时间')",
        "author": "",
        "navigation": "normalize-space(.//*[@class='mbx'])",
        "content": ".//*[@class='text']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='ArticleTitle'])",
        "news_date": "normalize-space(.//*[@class='ArticleInfo']/*[@class='left'])",
        "source": "",
        "author": "",
        "navigation": "substring(normalize-space(.//*[@class='athere']),6,50)",
        "content": ".//*[@class='content']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='row title'])",
        "news_date": "normalize-space(.//*[@class='pubDate'])",
        "source": "substring-after(normalize-space(.//*[@class='source']),'来源：')",
        "author": "",
        "navigation": "normalize-space(.//*[@class='nav'])",
        "content": ".//*[@class='article-content']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{4}/\d{4}/\d*\.[s]*htm[l]*'

