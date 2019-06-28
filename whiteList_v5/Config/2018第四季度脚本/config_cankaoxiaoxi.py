# 参考消息
TASK_NAME = 'cankaoxiaoxi'

# 起始URL
START_URL = 'http://www.cankaoxiaoxi.com/'

# 控制域，必须为list格式
DOMAIN = ['cankaoxiaoxi']
# 请求头
HEADERS = {
    'Host': 'www.cankaoxiaoxi.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:52.0) Gecko/20100101 Firefox/52.0',
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
        "title": "normalize-space(.//*[@class='bg-content']/h1)",
        "news_date": "normalize-space(.//*[@id='pubtime_baidu'])",
        "source": "substring-after(normalize-space(.//*[@id='source_baidu']),'来源：')",
        "author": "",
        "navigation": "normalize-space(.//*[@class='crumb'])",
        "content": ".//*[contains(@class,'article-content')]/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[@id='editor_baidu']),'：')",
        "tags": ".//*[@name='keywords']/@content",
    },
    {
        "title": "normalize-space(.//*[@class='column']/h1)",
        "news_date": "normalize-space(.//*[@class='post-time'])",
        "source": "normalize-space(.//*[@class='source'])",
        "author": "",
        "navigation": "normalize-space(.//*[contains(@class,'mode-position')])",
        "content": ".//*[@data-gallery='photo-description']/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[contains(@class,'editor')]),'责任编辑：')",
        "tags": ".//*[@name='keywords']/@content",
    },
    {
        "title": "normalize-space(.//h2[@class='YH'])",
        "news_date": "normalize-space(.//*[@class='__BAIDUNEWS__tm'])",
        "source": "substring-after(normalize-space(.//*[@class='__BAIDUNEWS__source']),'来源：')",
        "author": "",
        "navigation": "",
        "content": ".//*[@class='__BAIDUNEWS__text']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content",
    },
    {
        "title": ".//*/h1/descendant::text()",
        "news_date": ".//*[@id='pubtime_baidu']/text()|.//*[@class='post-time']/text()",
        "soruce": "substring-after(.//*[@id='source_baidu']|.//*[@class='source']/text(),'来源：')",
        "author": "",
        "navigation": "string(.//*[@class='crumb']|.//*[starts-with(@class,'mode-position')])",
        "content": ".//*[@id='ctrlfscont']/descendant::text()|.//*[@data-gallery='photo-description']/descendant::text()",
        "editor": "substring-after(.//*[@id='editor_baidu']|.//*[starts-with(@class,'editor')],'编辑：')",
        "tags": ".//*[@name='keywords']/@content",
    },



]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/[\d]*[\w]*/\d{4,8}/\d{7}\.[s]*htm[l]*'

