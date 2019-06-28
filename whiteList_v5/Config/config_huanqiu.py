# 环球网
TASK_NAME = 'huanqiu'

# 起始URL
START_URL = 'http://www.huanqiu.com/'

# 控制域，必须为list格式
DOMAIN = ['huanqiu.com']
# 请求头
HEADERS = {
    'Host': 'www.huanqiu.com',
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
#     "publish_time": "",
#     "source": "",
#     "author": "",
#     "belong": "",
#     "content": "",
#     "editor": "",
# },
XPATHER_NEWS_LIST = [
    {
        "title": ".//*[@class='tle']/text()",
        "publish_time": ".//*[@class='la_t_a']/text()",
        "source": ".//*[@class='la_t_b']/descendant::text()",
        "author": "",
        "belong": "string(.//*[@class='nav_left'])",
        "content": ".//*[@class='la_con']/descendant::text()",
        "editor": ".//*[@class='la_e_a']/text()",
    }


]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{4}-\d{2}/\d+.[s]*htm[l]*'

