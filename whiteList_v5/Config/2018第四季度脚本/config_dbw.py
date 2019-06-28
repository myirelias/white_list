# 东北网
TASK_NAME = 'dbw'

# 起始URL
START_URL = 'https://www.dbw.cn/'

# 控制域，必须为list格式
DOMAIN = ['dbw']
# 请求头
HEADERS = {
    'Host': 'www.dbw.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.dbw.cn/',
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
        "title": "normalize-space(.//*[@class='neirong']/h1)",
        "news_date": "substring-before(substring-after(.//*[@class='dizhi hui'],'时间：'),'来源')",
        "source": "substring-before(substring-after(.//*[@class='dizhi hui'],'来源：'),'编辑')",
        "author": "",
        "navigation": "substring-after(.//*[@class='dangq'],'位置')",
        "content": ".//*[@class='duanluo']/descendant::text()",
        "editor": "substring-after(.//*[@class='dizhi hui'],'编辑：')",
        "tags": "",
    },
    {
        "title": ".//*[@class='tt_news']/text()",
        "news_date": "substring-before(.//*[@class='info'],'来源')",
        "source": "substring-before(substring-after(.//*[@class='info'],'来源：'),'作者')",
        "author": "substring-after(.//*[@class='info'],'作者：')",
        "navigation": "substring-after(.//*[contains(@class,'postion')],'位置')",
        "content": ".//*[@id='p-detail']/descendant::p/text()",
        "editor": "substring-after(.//*[contains(text(),'编辑')],'编辑：')",
        "tags": "",
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{4}/\d{2}/\d{2}/\d+\.[s]*htm[l]*'



