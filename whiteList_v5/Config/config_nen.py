# 东北新闻网
TASK_NAME = 'nen'

# 起始URL',
START_URL = 'http://www.nen.com.cn/'

# 控制域，必须为list格式
DOMAIN = ['nen.com.cn']
# 请求头
HEADERS = {
    'Host': 'news.nen.com.cn',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://news.nen.com.cn/gngjnew/gnnew/index.shtml',
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
        "title": ".//*/h1[1]/text()",
        "publish_time": "substring-before(.//*[contains(text(),'来源')],'来源')",
        "source": "substring-after(.//*[contains(text(),'来源')],'来源：')",
        "author": "",
        "belong": "substring-after(.//*[@id='rwb_navpath'],'您当前的位置 ：')",
        "content": ".//*[@class='box_con']/descendant::p/text()",
        "editor": "substring-before(substring-after(.//*[contains(text(),'编辑')],'编辑：'),')')",
    },
    {
        "title": ".//*[@class='contentt']/text()",
        "publish_time": ".//*[@class='contenttime']/text()",
        "source": ".//*[@class='contenttime']/a[2]/text()",
        "author": "",
        "belong": "substring-after(.//*[@class='inversepath'],'位置 ：')",
        "content": ".//*[@class='contentcon']/descendant::text()",
        "editor": "substring-before(substring-after(.//*[contains(text(),'责任编辑')],'编辑：'),']')",
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{4}/\d{2}/\d{2}/\d+\.[s]*htm[l]*'
