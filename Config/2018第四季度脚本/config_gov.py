# 政府网
TASK_NAME = 'gov'

# 起始URL
START_URL = 'http://www.gov.cn/'

# 控制域，必须为list格式
DOMAIN = ['gov']
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
        "news_date": "substring-before(.//*[@class='pages-date'],'来源')",
        "source": "substring-before(substring-after(.//*[@class='pages-date'],'来源：'),'【')",
        "author": "",
        "navigation": "string(.//*[@class='BreadcrumbNav'])",
        "content": ".//*[@class='pages_content']/descendant::p/text()",
        "editor": "substring-after(.//*[contains(text(),'责任编辑')],'责任编辑：')",
        "tags": ".//*[@name='keywords']/@content",
    },
    {
        "title": ".//*[@class='art_tit']/descendant::text()",
        "news_date": "substring-before(substring-after(.//*[@class='sp_time'],'日期'),'来源')",
        "source": "substring-before(substring-after(.//*[@class='sp_time'],'来源'),'【')",
        "author": "",
        "navigation": "string(.//*[@class='dqwz'])",
        "content": ".//*[@id='zoom']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content",
    },
    {
        "title": ".//*[@id='UCAP-CONTENT']/p[contains(@style,'center')]/descendant::text()",
        "news_date": "normalize-space(.//*[contains(text(),'发布日期')]/parent::td/following-sibling::td)",
        "source": "normalize-space(.//*[contains(text(),'发文机关')]/parent::td/following-sibling::td)",
        "author": "",
        "navigation": "normalize-space(.//*[@class='BreadcrumbNav'])",
        "content": ".//*[@id='UCAP-CONTENT']/p[not(contains(@style,'center'))]/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content",
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'[\d\w]*_\d*\.[s]*htm[l]*'



