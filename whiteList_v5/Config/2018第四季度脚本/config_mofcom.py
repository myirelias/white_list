# 商务部
TASK_NAME = 'mofcom'

# 起始URL
START_URL = 'http://www.mofcom.gov.cn/'

# 控制域，必须为list格式
DOMAIN = ['mofcom']
# 请求头
HEADERS = {
    'Host': 'www.mofcom.gov.cn',
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
        "title": ".//*[@id='artitle']/text()",
        "news_date": ".//*[@id='arsource']//*[@align='center']/text()",
        "soruce": "substring-after(.//*[@class='from'],'文章来源：')",
        "author": "",
        "navigation": "substring-after(.//*[@class='position'],'当前位置：')",
        "content": ".//*[@class='cont']/descendant::p/descendant::text()|.//*[@class='artCon']/descendant::p/text()",
        "editor": "",
        "tags": "",
    },
    {
        "title": ".//*[@class='guider']/h4/text()",
        "news_date": "substring-before(substring-after(.//*[@class='source'],';'),'文章来源')",
        "source": "substring-after(substring-after(.//*[@class='source'],'文章来源：'),';')",
        "author": "",
        "navigation": "substring-after(.//*[@class='position'],'当前位置：')",
        "content": ".//*[@class='guider']/descendant::p/descendant::text()",
        "editor": "",
        "tags": "",
    },
    {
        "title": "normalize-space(.//*[@class='artTitle'])",
        "news_date": "substring(normalize-space(.//*[@id='show_time']),1,10)",
        "source": "substring-after(normalize-space(.//*[@id='show_time']),'来源：')",
        "author": "",
        "navigation": "",
        "content": ".//*[@class='con']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content",
    },
    {
        "title": "normalize-space(.//*[@class='artcle-tit'])",
        "news_date": "substring-after(normalize-space(.//h2[contains(text(),'发布日期')]),'发布日期：')",
        "source": "",
        "author": "",
        "navigation": "substring-after(normalize-space(.//*[@class='navMain']),'当前位置：')",
        "content": ".//*[@class='tol artcle']/descendant::p/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content",
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{6,8}/\d+\.[s]*htm[l]*'
