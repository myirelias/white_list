# 香山网
TASK_NAME = 'x3cn'

# 起始URL
START_URL = 'http://www.x3cn.com/'  # http://house.x3cn.com/index.php?caid=1 咨询版块有新闻

# 控制域，必须为list格式
DOMAIN = ['x3cn']
# 请求头
HEADERS = {
    'Host': 'www.x3cn.com',
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
        "title": "normalize-space(.//*[@id='title'])",
        "news_date": "substring(normalize-space(.//*[@class='laiyuan']),1,10)",
        "source": "substring-after(normalize-space(.//*[@class='laiyuan']),'来源：')",
        "author": "",
        "navigation": "substring(substring-before(normalize-space(.//*[@class='l mt5']),'/正文'),2,100)",
        "content": ".//*[@class='con']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'archive\.php.*?aid=\d*'

