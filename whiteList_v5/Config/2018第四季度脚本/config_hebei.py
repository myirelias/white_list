# 长城在线
TASK_NAME = 'hebei'

# 起始URL',
START_URL = 'http://www.hebei.com.cn/'

# 控制域，必须为list格式
DOMAIN = ['hebei']
# 请求头
HEADERS = {
    'Host': 'news.hebei.com.cn',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://www.hebei.com.cn/',
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
        "title": "normalize-space(.//*[@id='gjTitle'])",
        "news_date": "normalize-space(.//*[@class='docRelTime'])",
        "source": "normalize-space(.//*[@class='docSourceName'][2])",
        "author": "",
        "navigation": "substring-after(normalize-space(.//*[contains(text(),'您当前的位置')]),'您当前的位置：')",
        "content": ".//*[@id='fontzoom']/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[@id='docEditor'][2]),'责任编辑：')",
        "tags": ".//*[@name='Keywords']/@content",
    },
    {
        "title": "normalize-space(.//*[@class='zwbg']/h2)",
        "news_date": "concat(2,substring-after(normalize-space(.//td[@class='zwbg' and @height='35']),'2'))",
        "source": "substring-before(substring-after(normalize-space(.//*[contains(text(),'稿源')]/parent::td),'稿源：'),'编辑')",
        "author": "",
        "navigation": "substring-after(normalize-space(.//*[contains(text(),'您当前的位置')]/parent::td),'当前的位置：')",
        "content": ".//*[@class='r_content']/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[contains(text(),'编辑')]/parent::td),'编辑：')",
        "tags": ".//*[@name='keywords']/@content",
    },
    {
        "title": "normalize-space(.//*[@class='title'])",
        "news_date": "normalize-space(.//*[@class='xx']/span[3])",
        "source": "substring-after(normalize-space(.//*[contains(text(),'来源')]),'来源：')",
        "author": "substring-after(normalize-space(.//*[contains(text(),'作者')]),'作者：')",
        "navigation": "substring(normalize-space(.//*[@class='daohang']),10,200)",
        "content": ".//*[@class='gjy-nr']/descendant::p/text()",
        "editor": "substring-after(normalize-space(.//*[contains(text(),'责任编辑')]/parent::div),'责任编辑：')",
        "tags": ".//*[@name='Keywords']/@content",
    },
    {
        "title": "normalize-space(.//*[@id='docTitle'])",
        "news_date": "normalize-space(.//*[@id='pubtime_baidu'])",
        "source": "substring-after(normalize-space(.//*[@id='source_baidu']),'来源：')",
        "author": "substring-after(normalize-space(.//*[@id='author_baidu']),'作者：')",
        "navigation": "substring-after(normalize-space(.//*[@id='docLocation1']),'当前的位置：')",
        "content": ".//*[@id='fontzoom']/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[@id='editor_baidu']),'编辑：')",
        "tags": ".//*[@name='Keywords']/@content",
    },
    {
        "title": ".//*/h1/text()",
        "news_date": "substring-after(.//*[@class='post_source'],'来源：')",
        "source": "substring-before(substring-after(.//*[@class='post_source'],'来源：'),' ')",
        "author": "",
        "navigation": "string(.//*[@class='cms_block_span'])",
        "content": ".//*[@class='text']/descendant::text()",
        "editor": "substring-after(.//*[@class='editor'],'编辑：')",
        "tags": ".//*[@name='Keywords']/@content",
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{4}/\d{2}/\d{2}/\d+\.[s]*htm[l]*'

