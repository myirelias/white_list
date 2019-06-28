# 人民网
TASK_NAME = 'people'

# 起始URL
START_URL = 'http://www.people.com.cn/'

# 控制域，必须为list格式
DOMAIN = ['people.com.cn']
# 请求头
HEADERS = {
    'Host': 'www.people.com.cn',
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
        "title": ".//*/h1/text()",
        "publish_time": "substring-before(.//*[contains(text(),'来源：')],'来源')",
        "source": "substring-after(.//*[contains(text(),'来源：')],'来源：')",
        "author": "",
        "belong": "string(.//*[@id='rwb_navpath'])",
        "content": ".//*[@class='box_con']/descendant::text()",
        "editor": ".//*[starts-with(@class,'edit')]/text()",
    }

]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/[\w]*\d+[-]*\d*.[s]*htm[l]*'

