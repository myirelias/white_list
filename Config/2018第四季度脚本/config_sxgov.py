# 黄河新闻网
TASK_NAME = 'sxgov'

# 起始URL
START_URL = 'http://www.sxgov.cn/'

# 控制域，必须为list格式
DOMAIN = ['sxgov']
# 请求头
HEADERS = {
    'Host': 'www.sxgov.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
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
        "title": ".//*[@class='dahei']/text()",
        "news_date": ".//*[@id='pubtime_baidu']/text()",
        "source": ".//*[@id='source_baidu']/text()",
        "author": "",
        "navigation": "substring-after(.//*[@id='bannermenuleft'],'所在的位置')",
        "content": ".//*[@class='Newsfont']/descendant::text()",
        "editor": ".//*[@id='editor_baidu']/text()",
        "tags": ".//*[@name='keywords']/@content",
    },
    {
        "title": ".//*[@style='font-size:21px; line-height:29px;']/text()",
        "news_date": ".//*[@id='pubtime_baidu']/text()",
        "source": ".//*[@id='source_baidu']/text()",
        "author": "",
        "navigation": "",
        "content": ".//*[@class='gray14']/descendant::text()",
        "editor": ".//*[@id='editor_baidu']/text()",
        "tags": ".//*[@name='keywords']/@content",
    },
    {
        "title": "normalize-space(.//*[@id='title']/h1)",
        "news_date": "substring-after(normalize-space(.//*[contains(text(),'发布时间')]),'发布时间：')",
        "source": "substring-after(normalize-space(.//*[contains(text(),'来源')]),'来源：')",
        "author": "",
        "navigation": "normalize-space(.//*[@id='baright'])",
        "content": ".//*[@id='ltext']/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[contains(text(),'编辑')]),'编辑：')",
        "tags": ".//*[@name='keywords']/@content",
    },
    {
        "title": "normalize-space(.//*[@class='woietitle']/h2)",
        "news_date": "normalize-space(.//*[@id='pubtime_baidu'])",
        "source": "substring-after(normalize-space(.//*[@id='source_baidu']),'来源：')",
        "author": "",
        "navigation": "substring(normalize-space(.//*[contains(text(),'当前位置')]),7,20)",
        "content": ".//*[@class='woieconent']/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[contains(text(),'责任编辑')]),'责任编辑：')",
        "tags": ".//*[@name='keywords']/@content",
    },
    {
        "title": "normalize-space(.//*[@class='title'])",
        "news_date": "substring-before(substring-after(normalize-space(.//*[contains(text(),'发布时间')]),'发布时间：'),'|')",
        "source": "substring-before(substring-after(normalize-space(.//*[contains(text(),'来源')]),'来源：'),'|')",
        "author": "",
        "navigation": "normalize-space(.//*[contains(text(),'黄河新闻网>')]/parent::div)",
        "content": ".//*[contains(@class,'Newsfont')]/descendant::text()",
        "editor": "substring-before(substring-after(normalize-space(.//*[contains(text(),'编辑')]),'编辑：'),'|')",
        "tags": ".//*[@name='keywords']/@content",
    },
    {
        "title": "normalize-space(.//*[@id='conleft'])",
        "news_date": "normalize-space(.//*[@id='con']//*[@class='blue'])",
        "source": "substring-after(normalize-space(.//*[@id='source_baidu']),'来源：')",
        "author": "",
        "navigation": "substring-after(normalize-space(.//*[@id='bannermenucenter']),'所在的位置：')",
        "content": ".//*[@class='Newsfont']/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[@id='editor_baidu']),'编辑：')",
        "tags": ".//*[@name='keywords']/@content",
    },
    {
        "title": "normalize-space(.//*[@class='nr_title'])",
        "news_date": "normalize-space(.//*[@id='pubtime_baidu'])",
        "source": "substring-after(normalize-space(.//*[@id='source_baidu']),'来源：')",
        "author": "",
        "navigation": "substring-after(normalize-space(.//*[contains(text(),'您所在的位置')]/parent::td),'位置：')",
        "content": ".//*[@class='nr_line']/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[@id='editor_baidu']),'编辑：')",
        "tags": ".//*[@name='keywords']/@content",
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'[\d\w]*_\d*\.[s]*htm[l]*'



