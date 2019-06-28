# 中金在线
TASK_NAME = 'cnfol'

# 起始URL
START_URL = 'http://www.cnfol.com/'

# 控制域，必须为list格式
DOMAIN = ['cnfol']
# 请求头
HEADERS = {
    'Host': 'futures.cnfol.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://www.cnfol.com/',
    'Cookie': 'cookieNameFlag=40966cc1-bbf9-4f62-8042-30852c34e4ec; ad_1125=1547448813000; ad_1126=1547448813000; UM_distinctid=165c774e8fc4d7-05c18acfc9efcc-1262694a-1fa400-165c774e8fe343; Hm_lvt_c378c4854ec370c1c8438f72e19b7170=1547445289; CnlIds=153664965364639985; Hm_lpvt_c378c4854ec370c1c8438f72e19b7170=1547448812; CNZZDATA1253240157=398583480-1547444975-http%253A%252F%252Fwww.cnfol.com%252F%7C1547444975',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0',
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
        "title": ".//*[@class='title']/text()",
        "news_date": ".//*[@class='tit']/span[1]/text()",
        "source": "substring-after(.//*[contains(text(),'来源')],'来源：')",
        "author": "substring-after(.//*[contains(text(),'作者')],'作者：')",
        "navigation": "string(.//*[@class='BdPiLTl Fl'])",
        "content": ".//*[@class='EDArtInfo']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": ".//*[@class='artTitle']/text()",
        "news_date": ".//*[@class='artDes']/span[1]/text()",
        "source": "substring-after(.//*[contains(text(),'来源')],'来源:')",
        "author": "substring-after(.//*[contains(text(),'作者')],'作者:')",
        "navigation": "string(.//*[@class='LocalUl'])",
        "content": ".//*[@class='Article']/descendant::text()",
        "editor": "substring-after(.//*[contains(text(),'责任编辑')],'责任编辑：')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": ".//*[@class='ArtH1']/text()",
        "news_date": ".//*[@class='ArtHps Cf']/span[1]/text()",
        "source": ".//*[@class='ArtHps Cf']/a[1]/text()",
        "author": "",
        "navigation": "string(.//*[@class='VdoUrhere Cf'])",
        "content": ".//*[@id='ArtDsc']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": ".//*[@class='main']/h1/text()",
        "news_date": ".//*[@class='time']/text()",
        "source": ".//*[@class='texInfoL Fl']/a/text()",
        "author": "",
        "navigation": "string(.//*[@class='BdPiLTl'])",
        "content": ".//*[@class='mainInfo']/descendant::text()",
        "editor": "substring-after(.//*[contains(text(),'责任编辑')],'责任编辑：')   ",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "string(.//*[@class='Head'])",
        "news_date": "substring-before(substring-after(.//*[@class='MBTime'],'['),']')",
        "source": "",
        "author": "",
        "navigation": "",
        "content": ".//*[contains(@class,'ArticleCont')]/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='Keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@id='Title'])",
        "news_date": "normalize-space(.//*[@id='pubtime_baidu'])",
        "source": "substring-after(normalize-space(.//*[@id='source_baidu']),'来源：')",
        "author": "substring-after(normalize-space(.//*[@id='author_baidu']),'作者：')",
        "navigation": "normalize-space(.//*[contains(@class,'Location')])",
        "content": ".//*[@id='Content']/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[@id='editor_baidu']),'责任编辑：')",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d*[/-]\d*\.[s]*htm[l]*'

