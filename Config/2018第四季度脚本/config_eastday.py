# 上海东方网
TASK_NAME = 'eastday'

# 起始URL
START_URL = 'http://www.eastday.com/'

# 控制域，必须为list格式
DOMAIN = ['eastday']
# 请求头
HEADERS = {
    'Host': 'www.eastday.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Cookie': 'wdcid=71a380985fcd0755; wdlast=1542091193',
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
#     "tags": "",
# },
XPATHER_NEWS_LIST = [
    {
        "title": ".//*[@id='biaoti']/text()",
        "news_date": ".//*[@id='pubtime_baidu']/text()",
        "source": "substring-before(substring-after(.//*[@id='editor_baidu']/parent::p,'来源'),'作者')",
        "author": "substring-before(substring-after(.//*[@id='editor_baidu']/parent::p,'作者'),'选稿')",
        "navigation": "string(.//*[contains(@class,'weizhi')])",
        "content": ".//*[@id='zw']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content",
    },
    {
        "title": ".//*/h1[@class='blue22 textcenter']/text()",
        "news_date": "substring-before(.//*[contains(@class,'timer')],'来源')",
        "source": "substring-before(substring-after(.//*[contains(@class,'timer')],'来源'),'选稿')",
        "author": "",
        "navigation": "substring-after(.//*[contains(@class,'pos')], '当前位置')",
        "content": ".//*[starts-with(@id,'zw')]/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content",
    },
    {
        "title": "normalize-space(.//*[@class='dabiao7 ma'])",
        "news_date": "substring-after(normalize-space(.//*[contains(text(),'时间')]/parent::p),'时间：')",
        "source": "substring-before(substring-after(normalize-space(.//*[contains(text(),'来源')]/parent::p),'来源：'),'作者')",
        "author": "substring-before(substring-after(normalize-space(.//*[contains(text(),'作者')]/parent::p),'作者：'),'选稿')",
        "navigation": "normalize-space(.//*[@class='breadnav'])",
        "content": ".//*[@class='para ma']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content",
    },
    {
        "title": "normalize-space(.//*[@class='title'])",
        "news_date": "normalize-space(.//*[@class='info']/span[1])",
        "source": "substring-after(normalize-space(.//*[contains(text(),'来源')]),'来源：')",
        "author": "substring-after(normalize-space(.//*[contains(text(),'作者')]),'作者：')",
        "navigation": "substring-after(normalize-space(.//*[@class='bread']),'当前位置')",
        "content": ".//*[@class='nr']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content",
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{4,8}/\w*\d+\.[s]*htm[l]*'



