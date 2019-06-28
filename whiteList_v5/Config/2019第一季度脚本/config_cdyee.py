# 巴中传媒网
TASK_NAME = 'cdyee'

# 起始URL
START_URL = 'http://www.cdyee.com/'

# 控制域，必须为list格式
DOMAIN = ['cdyee']
# 请求头
HEADERS = {
    'Host': 'www.cdyee.com',
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
        "title": "string(.//*[@class='spnews_wzbt'])",
        "news_date": "substring(normalize-space(.//*[contains(text(),'时间')]),4,20)",
        "source": "substring(normalize-space(.//*[contains(text(),'来源')]),4,20)",
        "author": "substring(normalize-space(.//*[contains(text(),'作者')]),4,20)",
        "navigation": "substring(normalize-space(.//*[contains(text(),'您所在的位置')]),10,100)",
        "content": ".//*[@class='spwzxx']/descendant::text()",
        "editor": "substring(normalize-space(.//*[contains(text(),'编辑')]),4,20)",
        "tags": ".//head/title/text()"
    },
    {
        "title": "string(.//*/td[@class='f_lan'])",
        "news_date": "substring-before(substring-after(normalize-space(.//*[contains(text(),'时间')]),'时间：'),'作者')",
        "source": "substring-before(substring-after(normalize-space(.//*[contains(text(),'来源')]),'来源：'),'时间')",
        "author": "substring-after(normalize-space(.//*[contains(text(),'作者')]),'作者：')",
        "navigation": "substring(normalize-space(.//*[contains(text(),'所在的位置')]),9,100)",
        "content": ".//*[@class='f14 l28']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='description']/@content"
    },
    {
        "title": "normalize-space(.//*[contains(@class,'artical_title')])",
        "news_date": "normalize-space(.//*[@class='artical_pubtime'])",
        "source": "normalize-space(.//*[@class='artical_source'])",
        "author": "normalize-space(.//*[@class='artical_author'])",
        "navigation": "substring-after(normalize-space(.//*[contains(text(),'您所在的位置')]),'：')",
        "content": ".//*[contains(@class,'artical_content')]/descendant::text()",
        "editor": "normalize-space(.//*[@class='artical_editor'])",
        "tags": ""
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{4,6}[-]*\d{1,4}/\d*/\w*_\d*\.[s]*htm[l]*|index\.php.*?catid=\d*&id=\d*'

