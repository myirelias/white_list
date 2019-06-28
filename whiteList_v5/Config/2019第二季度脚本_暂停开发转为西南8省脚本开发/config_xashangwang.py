# 滨海高新
TASK_NAME = 'xashangwang'

# 起始URL
START_URL = 'http://www.xashangwang.com/'

# 控制域，必须为list格式
DOMAIN = ['xashangwang']
# 请求头
HEADERS = {
    'Host': 'www.xashangwang.com',
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
        "title": "normalize-space(.//*[@class='insideL']/h2)",
        "news_date": "substring(substring-after(normalize-space(.//*[@class='copyfrom']),'日期：'),1,20)",
        "source": "substring-after(.//*[contains(text(),'来源：')],'：')",
        "author": "",
        "navigation": "substring-after(normalize-space(.//*[@class='locations']),'位置：')",
        "content": ".//*[@class='showcontent']/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[@class='copyfrom']),'编辑：')",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\w*_\d*/\d*\.s*html*'

