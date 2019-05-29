# 团结报
TASK_NAME = 'tuanjiebao'

# 起始URL
START_URL = 'http://www.tuanjiebao.com/'

# 控制域，必须为list格式
DOMAIN = ['tuanjiebao']
# 请求头
HEADERS = {
    'Host': 'www.tuanjiebao.com',
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
        "title": "normalize-space(.//*[@class='t-l'])",
        "news_date": "substring(substring-after(normalize-space(.//*[@class='t-s']),'发布时间：'),1,10)",
        "source": "substring-after(normalize-space(.//*[@class='t-s']),'来源：')",
        "author": "substring-after(normalize-space(.//*[@class='t-s']),'作者：')",
        "navigation": "substring-after(normalize-space(.//*[@class='clumb']),'当前位置：')",
        "content": ".//*[@class='fujian2']/descendant::text()",
        "editor": "substring-before(substring-after(normalize-space(.//*[contains(text(),'责任编辑')]),'责任编辑：'),']')",
        "tags": ".//*[contains(@name,'eywords')]/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{4}-\d{2}/\d*/content_\d*\.s*html*'


