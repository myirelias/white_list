# 巴中传媒网
TASK_NAME = 'bznews'

# 起始URL
START_URL = 'http://www.bznews.org/'

# 控制域，必须为list格式
DOMAIN = ['bznews']
# 请求头
HEADERS = {
    'Host': 'www.bznews.org',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
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
        "title": "normalize-space(.//*[@id='titleContent'])",
        "news_date": "substring(substring-before(.//*[contains(text(),'来源')],'来源'),23,50)",
        "source": "substring-before(substring-after(.//*[contains(text(),'来源')],'来源：'),'【')",
        "author": "",
        "navigation": "substring(normalize-space(.//*[contains(text(),'您所在的位置')]),9,200)",
        "content": ".//*[@class='cotentBox']/descendant::text()",
        "editor": "substring(.//*[contains(text(),'责任编辑')],6,20)",
        "tags": ".//*[@name='Keywords']/@content"
    },
    {
        "title": "normalize-space(html/body/table[14]/tbody/tr/td[1]/table/tbody/tr/td/table[3]/tbody/tr[2]/td|.//title)",
        "news_date": "substring-after(substring-before(normalize-space(.//*[contains(text(),'来源')]),'来源'),'网')",
        "source": "substring-before(substring-after(normalize-space(.//*[contains(text(),'来源')]),'来源：'),'【')",
        "author": "",
        "navigation": "substring-after(normalize-space(.//*[@id='zimenu2']),'：')",
        "content": "html/body/table[14]/tbody/tr/td[1]/table/tbody/tr/td/table[6]/tbody/tr/td/descendant::text()|.//*[@name='Description']/@content",
        "editor": "substring-after(normalize-space(.//*[contains(text(),'责任编辑')]),'责任编辑：')",
        "tags": ".//*[@name='Keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{6,8}/\d*\.[s]*htm[l]*'

