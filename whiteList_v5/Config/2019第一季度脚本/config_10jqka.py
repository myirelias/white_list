# 同花顺财经网
TASK_NAME = '10jqka'

# 起始URL
START_URL = 'http://www.10jqka.com.cn/'

# 控制域，必须为list格式
DOMAIN = ['10jqka']
# 请求头
HEADERS = {
    'Host': 'www.10jqka.com.cn',
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
        "title": "string(.//*[@class='main-title'])",
        "news_date": "string(.//*[@id='pubtime_baidu'])",
        "source": ".//*[contains(text(),'来源')]/img/@src",
        "author": "",
        "navigation": "string(.//*[@class='top-crumbs']//*[@class='top-channel'])",
        "content": ".//*[contains(@class,'atc-conten')]/descendant::p/text()",
        "editor": "substring(.//*[@id='editor_baidu'],6,20)",
        "tags": ".//*[@name='description']/@content"
    },
    {
        "title": "string(.//*[@class='tac detail-title'])",
        "news_date": "string(.//*[@class='date'])",
        "source": "string(.//*[contains(@class,'post-author')])",
        "author": "",
        "navigation": "",
        "content": ".//*[contains(@class,'post-text-main')]/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='main article']/h2)",
        "news_date": "substring-before(normalize-space(.//*[@class='time']),'阅读')",
        "source": "",
        "author": "substring-before(normalize-space(.//*[@class='name-tag']),'评分')",
        "navigation": "",
        "content": ".//*[@class='article-con']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='articleTit'])",
        "news_date": "translate(normalize-space(.//*[@class='fromNews']),'来源：','')",
        "source": "",
        "author": "",
        "navigation": "normalize-space(.//*[@class='sub_nav'])",
        "content": ".//*[@class='art_main']/descendant::p/text()",
        "editor": "substring-after(normalize-space(.//*[@id='editor_baidu']),'：')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='YBTit'])",
        "news_date": "substring-after(normalize-space(.//*[contains(text(),'发表时间')]),':')",
        "source": "normalize-space(.//*[contains(text(),'所属机构')]/following-sibling::dd)",
        "author": "",
        "navigation": "",
        "content": ".//*[@class='YBText']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='main-title'])",
        "news_date": "normalize-space(.//*[@id='pubtime_baidu'])",
        "source": "normalize-space(.//*[@id='sourcename'])",
        "author": "",
        "navigation": "normalize-space(.//*[@class='top-channel'])",
        "content": ".//*[@class='main-text atc-content']/descendant::p/text()",
        "editor": "substring-after(normalize-space(.//*[@id='editor_baidu']),'：')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@id='activity-name'])",
        "news_date": "normalize-space(.//*[@id='publish_time'])",
        "source": "normalize-space(.//*[@id='js_author_name'])",
        "author": "substring-after(.//*[contains(text(),'作者')],'作者：')",
        "navigation": "",
        "content": ".//*[@id='js_content']/descendant::text()",
        "editor": "",
        "tags": ""
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{6,8}/\w*\d*\.[s]*htm[l]*|/\w*_\d*\.[s]*htm[l]*'

