# 国家旅游地理
TASK_NAME = 'cntgol'

# 起始URL
START_URL = 'http://www.cntgol.com/'

# 控制域，必须为list格式
DOMAIN = ['cntgol']
# 请求头
HEADERS = {
    'Host': 'www.cntgol.com',
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
# },normalize-space(html/body/div[3]/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr[2]/td/table[1]/tbody/tr[3]/td)
XPATHER_NEWS_LIST = [
    {
        "title": "normalize-space(html/body/div[4]/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr[2]/td/table[1]/tbody/tr[3]/td)",
        "news_date": "substring(normalize-space(html/body/div[4]/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr[2]/td/table[1]/tbody/tr[4]/td),1,20)",
        "source": "substring-before(substring-after(.//*[contains(text(),'来源:')]/parent::div,'来源:'),'作者')",
        "author": "substring-before(substring-after(.//*[contains(text(),'作者:')]/parent::div,'作者:'),'编辑')",
        "navigation": "substring(normalize-space(.//*[contains(text(),'当前位置：')]),6,200)",
        "content": ".//*[@class='ArticleContent']/descendant::p/text()",
        "editor": "substring-after(.//*[contains(text(),'编辑:')]/parent::div,'编辑:')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(html/body/div[3]/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr[2]/td/table[1]/tbody/tr[3]/td)",
        "news_date": "substring(normalize-space(html/body/div[3]/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr[2]/td/table[1]/tbody/tr[4]/td),1,20)",
        "source": "substring-before(substring-after(normalize-space(.//*[contains(text(),'来源')]/parent::div),'来源:'),'作者')",
        "author": "substring-before(substring-after(normalize-space(.//*[contains(text(),'来源')]/parent::div),'作者:'),'编辑')",
        "navigation": "substring-after(normalize-space(.//*[contains(text(),'当前位置')]),'当前位置：')",
        "content": ".//*[@class='ArticleContent']//*[not(@type='text/javascript')]/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[contains(text(),'来源')]/parent::div),'编辑:')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//title)",
        "news_date": "substring-before(substring-after(normalize-space(.//*[@class='info']),'时间:'),'来源')",
        "source": "substring-before(substring-after(normalize-space(.//*[@class='info']),'来源:'),'作者')",
        "author": "substring-before(substring-after(normalize-space(.//*[@class='info']),'作者:'),'编辑')",
        "navigation": "",
        "content": ".//*[@class='picbox' or @class='intro']/descendant::text()",
        "editor": "substring-before(substring-after(normalize-space(.//*[@class='info']),'编辑:'),'点击')",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{4,8}[/]*\d*[/]*\d*\.[s]*htm[l]*'

