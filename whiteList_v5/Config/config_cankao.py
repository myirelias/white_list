# 参考消息
TASK_NAME = 'cankaoxiaoxi'

# 起始URL
START_URL = 'http://www.cankaoxiaoxi.com/'

# 控制域，必须为list格式
DOMAIN = ['cankaoxiaoxi.com']
# 请求头
HEADERS = {
    'Host': 'www.cankaoxiaoxi.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:52.0) Gecko/20100101 Firefox/52.0',
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
#     "publish_time": "",
#     "source": "",
#     "author": "",
#     "belong": "",
#     "content": "",
#     "editor": "",
# },
XPATHER_NEWS_LIST = [
    {
        "title": ".//*/h1/descendant::text()",
        "publish_time": ".//*[@id='pubtime_baidu']/text()",
        "soruce": "substring-after(.//*[@id='source_baidu'],'来源：')",
        "author": "",
        "belong": "string(.//*[@class='crumb'])",
        "content": ".//*[@id='ctrlfscont']/descendant::text()",
        "editor": "substring-after(.//*[@id='editor_baidu'],'编辑：')",
    },
    {
        "title": ".//*/h1/descendant::text()",
        "publish_time": ".//*[@class='post-time']/text()",
        "source": ".//*[@class='source']/text()",
        "author": "",
        "belong": "string(.//*[starts-with(@class,'mode-position')])",
        "content": ".//*[@data-gallery='photo-description']/descendant::text()",
        "editor": "substring-after(.//*[starts-with(@class,'editor')],'编辑：')",
    }

]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/[\d]*[\w]*/\d{4,8}/\d{7}\.[s]*htm[l]*'

