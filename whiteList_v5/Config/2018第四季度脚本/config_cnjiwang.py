# 中国吉林网
TASK_NAME = 'cnjiwang'

# 起始URL',
START_URL = 'http://www.cnjiwang.com/'

# 控制域，必须为list格式
DOMAIN = ['cnjiwang']
# 请求头
HEADERS = {
    'Host': 'ent.cnjiwang.com',
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
        "title": "normalize-space(.//*[@class='sp_zwtt'])",
        "news_date": "substring(normalize-space(.//*[@class='sp_zwdate']),1,10)",
        "source": "substring-after(normalize-space(.//*[@class='sp_zwdate']),'来源：')",
        "author": "",
        "navigation": "",
        "content": ".//*[@class='sp_zwleft left']/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[contains(text(),'编辑')]),'：')",
        "tags": ".//*[@name='keywords']/@content",
    },
    {
        "title": ".//*/h1/descendant::text()",
        "news_date": "substring-before(.//*[contains(text(),'来源')],'|')",
        "source": "substring-after(.//*[contains(text(),'来源')],'来源：')",
        "author": "",
        "navigation": "substring-after(.//*[@class='path'],'位置 ：')",
        "content": ".//*[@class='content']/descendant::text()",
        "editor": "substring-after(.//*[contains(text(),'责任编辑')],'编辑：')",
        "tags": ".//*[@name='keywords']/@content",
    },
    {
        "title": "normalize-space(.//*[@class='gysjnews_tit'])",
        "news_date": "substring(substring-after(normalize-space(.//*[contains(text(),'发布时间')]),'发布时间：'),1,18)",
        "source": "substring-after(normalize-space(.//*[contains(text(),'来源')]),'来源：')",
        "author": "",
        "navigation": "substring(normalize-space(.//*[@class='dqwz']),9,200)",
        "content": ".//*[@class='gysjnews_sp']/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[contains(text(),'编辑')]),'编辑：')",
        "tags": ".//*[@name='keywords']/@content",
    },
]


# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{6,8}/\d+\.[s]*htm[l]*'
