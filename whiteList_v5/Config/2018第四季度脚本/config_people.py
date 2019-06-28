# 人民网
TASK_NAME = 'people'

# 起始URL
START_URL = 'http://www.people.com.cn/'

# 控制域，必须为list格式
DOMAIN = ['people']
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
        "title": ".//*/h1/text()",
        "news_date": "substring-before(.//*[contains(text(),'来源：')],'来源')",
        "source": "substring-after(.//*[contains(text(),'来源：')],'来源：')",
        "author": "",
        "navigation": "string(.//*[@id='rwb_navpath'])",
        "content": ".//*[@class='box_con']/descendant::text()",
        "editor": ".//*[starts-with(@class,'edit')]/text()",
        "tags": ".//*[@name='keywords']/@content",
    },
    {
        "title": "normalize-space(.//*[@class='title']/h2)",
        "news_date": "substring-before(normalize-space(.//*[contains(text(),'来源')]),'来源：')",
        "source": "substring-after(normalize-space(.//*[contains(text(),'来源')]),'来源：')",
        "author": "normalize-space(.//*[@class='title']/p)",
        "navigation": "normalize-space(.//*[@class='subNav'])",
        "content": ".//*[@class='artDet']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content",
    },
    {
        "title": "normalize-space(.//*[@class='navBar']/h2)",
        "news_date": ".//*[@name='publishdate']/@content",
        "source": "",
        "author": "",
        "navigation": "normalize-space(.//*[contains(@class,'wrapNavBar')])",
        "content": ".//*[contains(@class,'article') and contains(@id,'post_content')]/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content",
    },

]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/[\w]*\d+[-]*\d*.[s]*htm[l]*'

