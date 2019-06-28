# 河北新闻网
TASK_NAME = 'hebnews'

# 起始URL',
START_URL = 'http://www.hebnews.cn/'

# 控制域，必须为list格式
DOMAIN = ['hebnews']
# 请求头
HEADERS = {
    'Host': 'hebei.hebnews.cn',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://gov.hebnews.cn/',
    'Connection': 'keep-alive'
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
        "title": "normalize-space(.//*[@id='title'])",
        "news_date": "normalize-space(.//*[@id='relate']/div[3])",
        "source": "substring(.//*[contains(text(),'来源')],4,20)",
        "author": "",
        "navigation": "substring-after(normalize-space(.//*[@id='position']),'提示：')",
        "content": ".//*[@class='content']/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[@class='editer']),'责任编辑：')",
        "tags": ".//*[@name='keywords']/@content",
    },
    {
        "title": "normalize-space(.//*[@class='zwbg' and contains(@height,'25')])",
        "news_date": "substring-after(normalize-space(.//*[contains(text(),'时间')]),'时间：')",
        "source": "substring-before(substring-after(normalize-space(.//*[contains(text(),'稿源')]/parent::td),'稿源：'),'时间')",
        "author": "",
        "navigation": "",
        "content": ".//*[@id='wrapper']/table[1]/tbody/tr[3]/td/table/tbody/tr/td[1]/table/tbody/tr/td/table[4]/tbody/tr/td/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[contains(text(),'责任编辑')]/parent::td),'责任编辑：')",
        "tags": "",
    },

    {
        "title": ".//*/h1/text()",
        "news_date": "substring-before(.//*[@class='post_source'],'来源：')",
        "source": "substring-after(.//*[@class='post_source'],'来源：')",
        "author": "",
        "navigation": "string(.//*[@class='bc_main'])",
        "content": ".//*[@class='text']/descendant::text()",
        "editor": "substring-after(.//*[@class='editor'],'编辑：')",
        "tags": ".//*[@name='keywords']/@content",
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{4}-\d{2}/\d+/\w+_\d+\.[s]*htm[l]*'

