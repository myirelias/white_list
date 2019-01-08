# 中国记协
TASK_NAME = 'zgjx'

# 起始URL
START_URL = 'http://www.zgjx.cn/'

# 控制域，必须为list格式
DOMAIN = ['zgjx.cn', 'xinhuanet.com']
# 请求头
HEADERS = {
    'Host': 'www.zgjx.cn',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'If-Modified-Since': 'Mon, 26 Mar 2018 03:25:27 GMT',
    'If-None-Match': '"5ab86827-1cd48"',
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
        "title": ".//*[@id='Title']/text()",
        "publish_time": "substring-before(.//*[contains(text(),'年') and contains(text(),'月') and contains(text(),'日')],'来源')",
        "source": "substring-after(.//*[contains(text(),'来源')],'来源：')",
        "author": "",
        "belong": "",
        "content": ".//*[@id='Content']/descendant::p/descendant::text()",
        "editor": "substring-before(substring-after(.//*[contains(text(),'责任编辑')],'责任编辑:'),'）')",
    }
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{4}-\d{2}/\d+/\w+_\d+\.[s]*htm[l]*'
