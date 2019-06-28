# 中国投资资讯网
TASK_NAME = 'ocn'

# 起始URL
START_URL = 'http://www.ocn.com.cn/'

# 控制域，必须为list格式
DOMAIN = ['ocn']
# 请求头
HEADERS = {
    'Host': 'www.ocn.com.cn',
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
        "title": "normalize-space(.//*[@class='newsinfo']/h1)",
        "news_date": "normalize-space(.//*[@class='date']/span[2])",
        "source": "substring-after(.//*[@class='date']/span[1],'：')",
        "author": "normalize-space(.//*[@class='date']/span[3])",
        "navigation": "substring(normalize-space(.//*[@class='plpath']),6,50)",
        "content": ".//*[@id='ncontent']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='Description']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='content']//h1)",
        "news_date": "substring(normalize-space(.//*[@class='date']),1,10)",
        "source": "substring(normalize-space(.//*[@class='date']),10,20)",
        "author": "",
        "navigation": "substring-after(normalize-space(.//*[contains(text(),'您现在的位置')]),'您现在的位置：')",
        "content": ".//*[@id='content']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='Description']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d*/\w*\d*\.[s]*htm[l]*'

