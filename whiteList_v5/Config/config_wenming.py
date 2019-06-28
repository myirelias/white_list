# 发改委
TASK_NAME = 'wenming'

# 起始URL
START_URL = 'http://www.wenming.cn/'

# 控制域，必须为list格式
DOMAIN = ['wenming.cn']
# 请求头
HEADERS = {
    'Host': 'www.wenming.cn',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
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
        "title": ".//*[starts-with(@id,'title')]/text()",
        "publish_time": "substring-before(substring-after((.//*[@id='time_tex']),'发表时间：'),'来源')",
        "source": "substring-after((.//*[@id='time_tex']),'来源：')",
        "author": "",
        "belong": "string(.//*[@class='title'])",
        "content": ".//*[@class='TRS_Editor']/descendant::text()",
        "editor": "",
    },
    {
        "title": ".//*[@class='tt-tit']/text()",
        "publish_time": "substring-after(.//*[contains(text(),'日期')],'日期：')",
        "source": "substring-after(.//*[contains(text(),'来源')],'来源：')",
        "author": "substring-after(.//*[contains(text(),'作者')],'作者：')",
        "belong": "string(.//*[@class='pl-l'])",
        "content": ".//*[@class='TRS_Editor']/descendant::text()",
        "editor": "substring-after(.//*[contains(text(),'责任编辑')],'编辑：')",
    },
    {
        "title": ".//*[@class='dc-title']/text()",
        "publish_time": ".//*[@class='dc-title02']/text()",
        "source": "substring-before(substring-after(.//*[contains(text(),'来源')],'来源：'),'责任编辑')",
        "author": "",
        "belong": "",
        "content": ".//*[@class='TRS_Editor']/descendant::p/descendant::text()",
        "editor": "substring-after(.//*[contains(text(),'责任编辑')],'责任编辑：')",
    },
    {
        "title": ".//*[@class='bqjj-tit']/text()",
        "publish_time": ".//*[@class='bqjj-qs']/text()",
        "source": "",
        "author": "",
        "belong": "",
        "content": ".//*[@class='TRS_Editor']/descendant::p/descendant::text()",
        "editor": "substring-after(.//*[contains(text(),'责任编辑')],'责任编辑：')",
    }
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{6,8}/\w*\d+_\d+\.[s]*htm[l]*'
