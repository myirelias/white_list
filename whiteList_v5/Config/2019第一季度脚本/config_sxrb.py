# 山西新闻网
TASK_NAME = 'sxrb'

# 起始URL
START_URL = 'http://www.sxrb.com/'

# 控制域，必须为list格式
DOMAIN = ['sxrb']
# 请求头
HEADERS = {
    'Host': 'www.sxrb.com',
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
#     "tags": ""
# },
XPATHER_NEWS_LIST = [
    {
        "title": "normalize-space(.//*[@class='art_tit'])",
        "news_date": "substring-before(substring-after(normalize-space(.//*[@class='art_info']),'时间：'),'来源')    ",
        "source": "substring-after(normalize-space(.//*[@class='art_info']),'来源：')",
        "author": "",
        "navigation": "normalize-space(.//*[@id='rwb_navpath'])",
        "content": ".//*[@class='art_txt']/descendant::text()",
        "editor": "translate(substring-after(.//*[contains(@class,'editer')],'责编：'),')','')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='content_title']/b)",
        "news_date": "normalize-space(.//*[@id='time'])",
        "source": "",
        "author": "",
        "navigation": "normalize-space(.//*[@class='logo_zi'])",
        "content": ".//*[@class='text']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='Keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='detConTit'])",
        "news_date": "normalize-space(.//*[contains(@class,'today')])",
        "source": "",
        "author": "",
        "navigation": "normalize-space(.//*[@class='search'])",
        "content": ".//*[@class='detail-text']/descendant::text()",
        "editor": "",
        "tags": ""
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d*[_]*\d*/\d*\.[s]*htm[l]*'

