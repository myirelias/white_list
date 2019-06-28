# 周口网
TASK_NAME = 'zkxww'

# 起始URL
START_URL = 'http://www.zkxww.com/'

# 控制域，必须为list格式
DOMAIN = ['zkxww']
# 请求头
HEADERS = {
    'Host': 'www.zkxww.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://www.zkxww.com/news/china/gdxw/273674.html',
    'Cookie': 'Hm_lvt_ffeee7c07545e9807a61b5c2ee09f58f=1547515757; Hm_lpvt_ffeee7c07545e9807a61b5c2ee09f58f=1547515795',
    'Connection': 'keep-alive',
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
#     "tags": ""
# },
XPATHER_NEWS_LIST = [
    {
        "title": ".//*[@id='h1title']/text()",
        "news_date": "substring-before(.//*[contains(text(),'来源')],'来源')",
        "source": "substring-before(substring-after(.//*[contains(text(),'来源')],'来源:'),'阅读量')",
        "author": "",
        "navigation": "string(.//*[starts-with(@class,'connav')])",
        "content": ".//*[@class='text']/descendant::p/descendant::text()",  # 最后有一段script，所以此处必须指定p标签
        "editor": "substring-after(.//*[contains(text(),'编辑')],'编辑：')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": ".//*[@class='details-title']/text()",
        "news_date": "substring-after(.//*[contains(text(),'发布时间')],'发布时间：')",
        "source": "substring-after(.//*[contains(text(),'来源')],'来源：')",
        "author": "",
        "navigation": "substring-after(.//*[@class='news-crumbs'],'当前的位置：')",
        "content": ".//*[@class='details-main']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'\d*[-]*\d*[-]*\d*[/]*\d*\.[s]*htm[l]*'

