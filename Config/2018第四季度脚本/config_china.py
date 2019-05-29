# 名称
TASK_NAME = 'china'

# 起始URL
START_URL = 'http://www.china.com.cn/'

# 控制域
DOMAIN = 'china'
# 请求头
HEADERS = {
    'Host': 'www.china.com.cn',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://www.china.com.cn/',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
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
        "title": ".//*[@class='articleTitle']/descendant::text()",
        "news_date": "substring-after(.//*[@id='pubtime_baidu'],'发布时间：')",
        "source": "substring-after(.//*[@id='source_baidu'],'来源：')",
        "author": "substring-after(.//*[@id='author_baidu'],'作者：')",
        "navigation": "",
        "content": ".//*[@class='articleBody']/descendant::text()",
        "editor": "substring-after(.//*[@class='articleEditor'],'编辑：')",
        "tags": ".//*[@name='keywords']/@content",
    },
    {
        "title": ".//*[@class='artTitle']/text()",
        "news_date": "substring-after(.//*[@id='pubtime_baidu'],'发布时间：')",
        "source": "substring-after(.//*[@id='source_baidu'],'来源：')",
        "author": "substring-after(.//*[@id='author_baidu'],'作者：')",
        "navigation": "string(.//*[@class='artLink'])",
        "content": ".//*[@class='artCon']/descendant::text()",
        "editor": "substring-after(.//*[@id='editor_baidu'],'编辑：')",
        "tags": ".//*[@name='keywords']/@content",
    },
    {
        "title": ".//*[@class='cTitle']/text()",
        "news_date": "substring-before(substring-after(.//*[@class='cInfo'],'发布时间：'),'责任编辑')",
        "source": "substring-before(substring-after(.//*[@class='cInfo'],'文章来源：'),'发布时间')",
        "author": "",
        "navigation": "string(.//*[@class='cNav'])",
        "content": ".//*[@class='cBody']/descendant::text()",
        "editor": "substring-after(.//*[@class='cInfo'],'编辑：')",
        "tags": ".//*[@name='keywords']/@content",
    },
    {
        "title": "normalize-space(.//*[@class='d2_box']/h1)",
        "news_date": "substring-before(substring-after(normalize-space(.//*[contains(text(),'发布时间')]),'发布时间：'),'|')",
        "source": "substring-before(substring-after(normalize-space(.//*[contains(text(),'来源')]),'来源：'),'|')",
        "author": "substring-after(normalize-space(.//*[contains(text(),'作者')]),'作者：')",
        "navigation": "normalize-space(.//*[@class='crumbs'])",
        "content": ".//div[contains(@class,'text')]/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[contains(text(),'责任编辑')]),'编辑：')",
        "tags": ".//*[@name='keywords']/@content",
    },
    {
        "title": "normalize-space(.//*[@id='box2']/h1)",
        "news_date": "substring-after(normalize-space(.//*[@id='pubtime_baidu']),'发布时间：')",
        "source": "substring-after(normalize-space(.//*[@id='source_baidu']),'来源：')",
        "author": "substring-after(normalize-space(.//*[@id='author_baidu']),'作者：')",
        "navigation": "substring-after(normalize-space(.//*[@id='box1']),'当前位置：')",
        "content": ".//*[@id='box3']/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[@id='editor_baidu']),'编辑：')",
        "tags": ".//*[@name='keywords']/@content",
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{4}-\d{2}/\d{2}/\w+_\d+.htm'

