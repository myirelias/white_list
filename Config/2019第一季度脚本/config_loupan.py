# 楼盘网
TASK_NAME = 'loupan'

# 起始URL
START_URL = 'http://www.loupan.com/'

# 控制域，必须为list格式
DOMAIN = ['loupan']
# 请求头
HEADERS = {
    'Host': 'www.loupan.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://liuyang.loupan.com/',
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
        "title": ".//*/h1[@class='title']/text()",
        "news_date": "substring-before(.//*[@class='meta'],'来源')",
        "source": "substring-after(.//*[contains(text(),'来源')],'：')",
        "author": "",
        "navigation": "string(.//*[@class='m-crumbs'])",
        "content": ".//*[@id='ajax_all_page']/descendant::text()",
        "editor": "substring-after(.//*[contains(text(),'责任编辑')],'：')",
        "tags": ".//*[@name='Keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{6,8}/\d*\.[s]*htm[l]*'

