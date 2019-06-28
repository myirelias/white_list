# 中国农村网
TASK_NAME = 'crnews'

# 起始URL
START_URL = 'http://www.crnews.net/'

# 控制域，必须为list格式
DOMAIN = ['crnews']
# 请求头
HEADERS = {
    'Host': 'www.crnews.net',
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
        "title": "normalize-space(.//*[@id='doctitle_h2'])",
        "news_date": "substring(normalize-space(.//*[@class='ly']),1,10)",
        "source": "substring-before(substring-after(normalize-space(.//*[@class='ly']),'来源：'),'作者')",
        "author": "substring-after(normalize-space(.//*[@class='ly']),'作者：')",
        "navigation": "normalize-space(.//*[@class='lb_wz'])",
        "content": ".//*[@class='texty']/descendant::text()",
        "editor": "",
        "tags": ""
    },
    {
        "title": "normalize-space(.//*[@class='article_title'])",
        "news_date": "substring-before(substring-after(normalize-space(.//*[@class='article_date']),'发布时间：'),']')",
        "source": "substring-before(substring-after(normalize-space(.//*[@class='article_date']),'信息来源：'),']')",
        "author": "",
        "navigation": "substring-after(normalize-space(.//*[contains(text(),'您当前所在')]),'您当前所在：')",
        "content": ".//*[@class='article']/descendant::text()",
        "editor": "",
        "tags": ""
    },
    {
        "title": ".//*[@class='dtxt']/descendant::h2/text()",
        "news_date": "substring(normalize-space(.//*[contains(text(),'来源')]),1,20)",
        "source": "substring-before(substring-after(normalize-space(.//*[contains(text(),'来源')]),'来源：'),'作者')",
        "author": "substring-after(normalize-space(.//*[contains(text(),'来源')]),'作者：')",
        "navigation": "normalize-space(.//*[@class='ct_left adleft']/h2)",
        "content": ".//*[contains(@class,'dbox')]/descendant::text()",
        "editor": "normalize-space(.//*[@id='zerenbianji'])",
        "tags": ""
    },
    {
        "title": "normalize-space(.//title)",
        "news_date": "substring(normalize-space(.//*[contains(text(),'来源')]),1,20)",
        "source": "substring-before(substring-after(normalize-space(.//*[contains(text(),'来源')]),'来源：'),'作者')",
        "author": "substring-after(normalize-space(.//*[contains(text(),'来源')]),'作者：')",
        "navigation": "normalize-space(.//h2)",
        "content": ".//*[@id='content1']/descendant::text()",
        "editor": "normalize-space(.//*[@id='zerenbianji'])",
        "tags": ".//*[@name='Keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d*_\d*\.s*html*'

