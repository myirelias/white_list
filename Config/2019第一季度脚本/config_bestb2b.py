# 志趣网
TASK_NAME = 'bestb2b'

# 起始URL
START_URL = 'https://www.bestb2b.com/news.htm'

# 控制域，必须为list格式
DOMAIN = ['bestb2b']
# 请求头
HEADERS = {
    'Host': 'www.bestb2b.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.bestb2b.com/',
    'Cookie': 'JSESSIONID=abckKMaVTuDYl4lP_FuHw; Hm_lvt_c19cb23867cd5205cecffd049d42ae9a=1547605902; Hm_lpvt_c19cb23867cd5205cecffd049d42ae9a=1547606271',
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
        "title": ".//*[@id='main']//*/h1/text()",
        "news_date": "substring-after(.//*[@href='#talkabout']/parent::td,'发表：')",
        "source": "substring-before(substring-after(.//*[@href='#talkabout']/parent::td,'来源:'),'点击')",
        "author": "",
        "navigation": "",
        "content": ".//*[@style='TEXT-INDENT: 2em']/descendant::text()",
        "editor": "substring-before(substring-after(.//*[@href='#talkabout']/parent::td,'编辑：'),'来源')",
        "tags": ".//*/head/title/text()"
    },
    {
        "title": ".//*[@class='container']/h1/text()",
        "news_date": "substring-before(substring-after(.//*[contains(text(),'发布时间')],'发布时间：'),'，')",
        "source": "substring-before(substring-after(.//*[contains(text(),'发布时间')],'所在地：'),'发布人')",
        "author": "substring-before(substring-after(.//*[contains(text(),'发布时间')],'发布人IP：'),'价格')",
        "navigation": "string(.//table/tbody//*/td[1])",
        "content": "string(.//*[contains(text(),'发布时间')])",
        "editor": "",
        "tags": ".//*/head/title/text()"
    },
    {
        "title": ".//*/h1/text()",
        "news_date": "string(.//*[contains(text(),'发布时间')]/following-sibling::td[1])",
        "source": "",
        "author": "string(.//*[contains(text(),'发布人')]/following-sibling::td[1])",
        "navigation": "substring-after(.//*[contains(text(),'您的位置')],'您的位置：')",
        "content": ".//*[@id='b2barticle']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\w*[_]*\w*[_]*\d*\.[s]*htm[l]*'

