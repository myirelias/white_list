# 政府网
TASK_NAME = 'gov'

# 起始URL
START_URL = 'http://www.gov.cn/'

# 控制域，必须为list格式
DOMAIN = ['gov.cn']
# 请求头
HEADERS = {
    'Host': 'www.gov.cn',
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
        "publish_time": "substring-before(.//*[@class='pages-date'],'来源')",
        "source": "substring-before(substring-after(.//*[@class='pages-date'],'来源：'),'【')",
        "author": "",
        "belong": "string(.//*[@class='BreadcrumbNav'])",
        "content": ".//*[@class='pages_content']/descendant::p/text()",
        "editor": "substring-after(.//*[contains(text(),'责任编辑')],'责任编辑：')",
    },
    {
        "title": ".//*[@class='art_tit']/descendant::text()",
        "publish_time": "substring-before(substring-after(.//*[@class='sp_time'],'日期'),'来源')",
        "source": "substring-before(substring-after(.//*[@class='sp_time'],'来源'),'【')",
        "author": "",
        "belong": "string(.//*[@class='dqwz'])",
        "content": ".//*[@id='zoom']/descendant::text()",
        "editor": "",
    }
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'[\d\w]*_\d*\.[s]*htm[l]*'



