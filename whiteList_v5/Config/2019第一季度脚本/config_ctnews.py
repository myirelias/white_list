# 中国旅游新闻网
TASK_NAME = 'ctnews'

# 起始URL
START_URL = 'http://www.ctnews.com.cn/'

# 控制域，必须为list格式
DOMAIN = ['ctnews']
# 请求头
HEADERS = {
    'Host': 'www.ctnews.com.cn',
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
        "title": "string(.//*[@class='font01'])",
        "news_date": "string(.//*[@class='paperdate'])",
        "source": "",
        "author": "",
        "navigation": "",
        "content": ".//*[@id='ozoom']/descendant::text()|.//*[@class='font6' and @align='center']/descendant::table/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": ".//*[starts-with(@class,'article_title')]/descendant::text()",
        "news_date": "substring(.//*[contains(text(),'时间')],4,50)",
        "source": "substring(.//*[contains(text(),'来源')],4,50)",
        "author": "substring(.//*[contains(text(),'作者')],4,50)",
        "navigation": "substring(.//*[contains(text(),'您现在的位置')]/parent::tr,8,500)",
        "content": ".//*[@class='bt_content']/descendant::text()",
        "editor": "substring(.//*[contains(text(),'责任编辑')],6,20)",
        "tags": ".//*[@name='keyword']/@content "
    },
    {
        "title": "normalize-space(.//*[@class='title'])",
        "news_date": "substring-after(normalize-space(.//*[contains(text(),'发布时间')]),'：')",
        "source": "substring-after(normalize-space(.//*[contains(text(),'信息来源')]),'：')",
        "author": "",
        "navigation": "normalize-space(.//*[@class='dqwz'])",
        "content": ".//*[@class='bt_content']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='Keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{4,6}[/-]*\d*[/]*\d*/\w*[_]*\d*[_]*\d*\.[s]*htm[l]*'

