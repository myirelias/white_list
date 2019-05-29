# 无锡新传媒
TASK_NAME = 'wxrb'

# 起始URL
START_URL = 'http://www.wxrb.com/'

# 控制域，必须为list格式
DOMAIN = ['wxrb']
# 请求头
HEADERS = {
    'Host': 'www.wxrb.com',
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
        "title": "normalize-space(.//h1)",
        "news_date": "normalize-space(.//*[@class='time_sour']/span[1])",
        "source": "substring(normalize-space(.//*[@class='time_sour']/span[2]),4,50)",
        "author": "",
        "navigation": "normalize-space(.//*[@class='brd_path'])",
        "content": ".//*[@class='newscontent']/descendant::text()",
        "editor": "translate(substring-after(.//*[@class='editer'],'责任编辑：'),']','')",
        "tags": ".//*[@name='Keywords']/@content"
    },
    {
        "title": "normalize-space(.//div[contains(@class,'main over')]//h2)",
        "news_date": "normalize-space(.//*[@class='time']/span[1])",
        "source": "substring-after(normalize-space(.//*[contains(text(),'来源')]),'来源：')",
        "author": "",
        "navigation": "normalize-space(.//*[@class='brd_path'])",
        "content": ".//*[@class='TRS_Editor']/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[contains(text(),'责任编辑')]),'责任编辑：')",
        "tags": ".//*[@name='Keywords']/@content"
    },
    {
        "title": "normalize-space(html/body/table[3]/tbody/tr/td[1]/table[2]/tbody/tr/td/table/tbody/tr[1]/td)",
        "news_date": "normalize-space(html/body/table[3]/tbody/tr/td[1]/table[2]/tbody/tr/td/table/tbody/tr[2]/td)",
        "source": "substring-before(substring-after(normalize-space(.//td[contains(text(),'来源')]),'来源：'),'编辑')",
        "author": "",
        "navigation": "normalize-space(html/body/table[3]/tbody/tr/td[1]/table[1]/tbody/tr/td)",
        "content": ".//*[@id='zenwen']/descendant::text()",
        "editor": "substring-after(normalize-space(.//td[contains(text(),'编辑')]),'编辑：')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//table[@class='newsprpt']//*[@class='style31'])",
        "news_date": "substring(normalize-space(.//table[@class='newsprpt']//*[@class='style32']),30,200)",
        "source": "substring-before(substring-after(normalize-space(.//td[contains(text(),'来源')]),'来源：'),'编辑')",
        "author": "",
        "navigation": "",
        "content": ".//div[@class='newsprpt']/descendant::text()",
        "editor": "substring-after(normalize-space(.//td[contains(text(),'编辑')]),'编辑：')",
        "tags": ".//*[@name='keywords']/@content"
    },

]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d*/[\w*]*\d*[_]*\d*\.[s]*htm[l]*'

