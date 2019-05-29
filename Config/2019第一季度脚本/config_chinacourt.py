# 中国法院网
TASK_NAME = 'chinacourt'

# 起始URL
START_URL = 'https://www.chinacourt.org/index.shtml'

# 控制域，必须为list格式
DOMAIN = ['chinacourt']
# 请求头
HEADERS = {
    'Host': 'www.chinacourt.org',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
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
        "title": "normalize-space(.//*[@class='detail_bigtitle'])",
        "news_date": "normalize-space(.//*[@class='time'])",
        "source": "substring(normalize-space(.//*[@class='source']),4,50)",
        "author": "",
        "navigation": "normalize-space(.//*[@class='address'])",
        "content": ".//*[@class='detail_txt']/descendant::text()",
        "editor": "substring(normalize-space(.//*[@class='compile']),6,50)",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='b_title'])",
        "news_date": "substring-after(normalize-space(.//*[contains(text(),'发布时间')]),'发布时间：')",
        "source": "substring-after(normalize-space(.//*[@class='from']),'来源：')",
        "author": "substring-before(substring-after(normalize-space(.//*[contains(text(),'作者')]),'作者：'),'发布时间')",
        "navigation": "substring-after(normalize-space(.//*[@class='detail_location']),'当前位置：')",
        "content": ".//*[@class='text general']/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[@class='editor']),'责任编辑：')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='piccontext']/h2)",
        "news_date": "substring-after(normalize-space(.//*[@class='info']),'时间：')",
        "source": "",
        "author": "",
        "navigation": "substring-before(substring-after(normalize-space(.//*[@class='info']),'所属栏目：'),'|')",
        "content": ".//*[@class='picshow_total_title']/descendant::text()",
        "editor": "",
        "tags": ""
    },

]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d*/\d*/\w*/\d*\.s*html*'

