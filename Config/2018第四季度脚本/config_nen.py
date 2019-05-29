# 东北新闻网
TASK_NAME = 'nen'

# 起始URL',
START_URL = 'http://www.nen.com.cn/'

# 控制域，必须为list格式
DOMAIN = ['nen']
# 请求头
HEADERS = {
    'Host': 'news.nen.com.cn',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://news.nen.com.cn/gngjnew/gnnew/index.shtml',
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
        "title": ".//*[@class='contentt']/text()",
        "news_date": ".//*[@class='contenttime']/text()",
        "source": ".//*[@class='contenttime']/a[2]/text()",
        "author": "",
        "navigation": "substring-after(.//*[@class='inversepath'],'位置 ：')",
        "content": ".//*[@class='contentcon']/descendant::text()",
        "editor": "substring-before(substring-after(.//*[contains(text(),'责任编辑')],'编辑：'),']')",
        "tags": ".//*[@name='keywords']/@content",
    },
    {
        "title": "normalize-space(html/body/table[5]/tbody/tr/td[1]/table/tbody/tr/td/table[2]/tbody/tr[2]/td)",
        "news_date": "normalize-space(.//*[@class='navhui2'][2])",
        "source": "normalize-space(.//*[@class='navhui2'][3])",
        "author": "",
        "navigation": "",
        "content": "html/body/table[5]/tbody/tr/td[1]/table/tbody/tr/td/table[4]/tbody/tr/td/descendant::text()",
        "editor": "translate(substring-after(normalize-space(.//*[contains(text(),'责任编辑')]),'责任编辑：'),']','')",
        "tags": ".//*[@name='keywords']/@content",
    },
    {
        "title": "normalize-space(.//*[@class='page-inner']/h2)",
        "news_date": "concat(2,substring-after(normalize-space(.//*[@class='thedate']),'2'))",
        "source": "substring-before(normalize-space(.//*[@class='thedate']),'2')",
        "author": "",
        "navigation": "",
        "content": ".//*[@class='page-inner']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content",
    },
    {
        "title": "normalize-space(.//*[@class='navbiao'])",
        "news_date": "concat(2,substring-after(substring-after(normalize-space(.//*[contains(text(),'来源')]),'来源：'),'2'))",
        "source": "substring-before(substring-after(normalize-space(.//*[contains(text(),'来源')]),'来源：'),'2')",
        "author": "",
        "navigation": "",
        "content": ".//td[@align='left']/descendant::p/text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content",
    },
    {
        "title": "normalize-space(.//*/h1)",
        "news_date": "substring-before(.//*[contains(text(),'来源')],'来源')",
        "source": "substring-after(.//*[contains(text(),'来源')],'来源：')",
        "author": "",
        "navigation": "substring-after(.//*[@id='rwb_navpath'],'您当前的位置 ：')",
        "content": ".//*[@class='box_con']/descendant::p/text()",
        "editor": "substring-before(substring-after(.//*[contains(text(),'编辑')],'编辑：'),')')",
        "tags": ".//*[@name='keywords']/@content",
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{4}/\d{2}/\d{2}/\d+\.[s]*htm[l]*'
