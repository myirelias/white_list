# 王朝网络
TASK_NAME = 'wangchao'

# 起始URL
START_URL = 'http://www.wangchao.net.cn/'

# 控制域，必须为list格式
DOMAIN = ['wangchao']
# 请求头
# 投融界带头请求不到
HEADERS = {
    'Host': 'www.wangchao.net.cn',
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
        "title": "normalize-space(.//*[@id='contentside']//h1)",
        "news_date": "substring(normalize-space(.//*[@id='pageinfo']),1,20)",
        "source": "substring-before(substring-after(normalize-space(.//*[@id='pageinfo']),'来源:'),'评论')",
        "author": "",
        "navigation": "substring-after(normalize-space(.//*[@id='navtop']),'当前位置:')",
        "content": ".//*[@id='content']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'detail_\d*\.s*html*'

