# 和讯网
TASK_NAME = 'hexun'

# 起始URL
START_URL = 'http://www.hexun.com/'

# 控制域，必须为list格式
DOMAIN = ['hexun']
# 请求头
HEADERS = {
    'Host': 'www.hexun.com',
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
        "title": "string(normalize-space(//*[contains(@class,'articleName')]/h1))",
        "news_date": "substring(normalize-space(.//*[@class='tip fl']),1,20)",
        "source": "substring(normalize-space(.//*[@class='tip fl']),20,100)",
        "author": "",
        "navigation": "string(normalize-space(.//*[@class='links']))",
        "content": ".//*[@class='art_context']/descendant::p/text()",
        "editor": "substring(normalize-space(.//*[contains(text(),'责任编辑')]),7,40)",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "string(.//*[@class='blog-top-tit'])",
        "news_date": "string(.//*/i[contains(text(),'年') and contains(text(),'月') and contains(text(),'日')])",
        "source": "",
        "author": "string(.//*[@class='t-name'])",
        "navigation": "",
        "content": ".//*[@class='article']/descendant::text()",
        "editor": "",
        "tags": ""
    },
    {
        "title": "string(.//*[@id='aBarName'])",
        "news_date": "string(.//*[@class='more_left_date']/span[2])",
        "source": "substring(.//*[contains(text(),'来源')],4,50)",
        "author": "",
        "navigation": "substring(.//*[@class='crumbs'],6,100)",
        "content": ".//*[@class='more_left_content']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='description']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='art_title'])",
        "news_date": "normalize-space(.//*[@id='pubtime_baidu'])",
        "source": "substring-after(normalize-space(.//*[@id='source_baidu']),'：')",
        "author": "substring-after(normalize-space(.//*[@id='author_baidu']),'：')",
        "navigation": "normalize-space(.//*[@class='crumbs_L'])",
        "content": ".//*[@class='art_context']/descendant::p/text()",
        "editor": "translate(substring-after(.//*[contains(text(),'责任编辑')],'：'),'）','')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[contains(@class,'zxny-tit')]/h1)",
        "news_date": "normalize-space(.//*[@class='fix zx-share']/span[1])",
        "source": "",
        "author": "",
        "navigation": "",
        "content": ".//*[@class='zxny-content']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@id='artibodyTitle']/h1)",
        "news_date": "normalize-space(.//*[contains(text(),'来源')]/parent::div/span[1])",
        "source": "substring-before(substring-after(normalize-space(.//*[@class='author gray']),'来源：'),'】')",
        "author": "substring-before(substring-after(normalize-space(.//*[@class='author gray']),'作者：'),'来源')",
        "navigation": "normalize-space(.//*[@class='breadcrumb'])",
        "content": ".//*[@class='concent']/descendant::text()",
        "editor": "translate(substring-after(normalize-space(.//*[@class='author gray']),'编辑：'),')','')",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/[\w*]*\d*[-]*\d*[-]*\d*[/]*\d*\.[s]*htm[l]*|detail\.do\?id=\d*'

