# 中国商网
TASK_NAME = 'zgswcn'

# 起始URL
START_URL = 'http://www.zgswcn.com/'

# 控制域，必须为list格式
DOMAIN = ['zgswcn']
# 请求头
HEADERS = {
    'Host': 'www.zgswcn.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
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
        "title": "normalize-space(.//*[@id='articleTitle'])",
        "news_date": "normalize-space(.//*[@class='article-title']/p[2]/span[1])",
        "source": "normalize-space(.//*[@class='article-title']/p[2]/a)",
        "author": "normalize-space(.//*[@class='article-title']/p[1])",
        "navigation": "normalize-space(.//*[@class='article-top rel'])",
        "content": ".//*[@class='article-con']/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[contains(text(),'责任编辑')]),'编辑：')",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/article/\d{6,8}/\d*\.s*html*'


