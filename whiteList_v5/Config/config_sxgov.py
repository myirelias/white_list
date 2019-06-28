# 黄河新闻网
TASK_NAME = 'sxgov'

# 起始URL
START_URL = 'http://www.sxgov.cn/'

# 控制域，必须为list格式
DOMAIN = ['sxgov.cn']
# 请求头
HEADERS = {
    'Host': 'www.sxgov.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0'
}


# xpath规则
XPATHER_HREF = ".//*/@href"
# 字段模版
# {
#     "title": "",
#     "publish_time": "",
#     "source": "",
#     "author": "",
#     "belong": "",
#     "content": "",
#     "editor": "",
# },
XPATHER_NEWS_LIST = [
    {
        "title": ".//*[@class='dahei']/text()",
        "publish_time": ".//*[@id='pubtime_baidu']/text()",
        "source": ".//*[@id='source_baidu']/text()",
        "author": "",
        "belong": "substring-after(.//*[@id='bannermenuleft'],'所在的位置')",
        "content": ".//*[@class='Newsfont']/descendant::text()",
        "editor": ".//*[@id='editor_baidu']/text()",
    },
    {
        "title": ".//*[@style='font-size:21px; line-height:29px;']/text()",
        "publish_time": ".//*[@id='pubtime_baidu']/text()",
        "source": ".//*[@id='source_baidu']/text()",
        "author": "",
        "belong": "",
        "content": ".//*[@class='gray14']/descendant::text()",
        "editor": ".//*[@id='editor_baidu']/text()",
    }
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'[\d\w]*_\d*\.[s]*htm[l]*'



