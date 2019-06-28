# 未来网
TASK_NAME = 'k618'

# 起始URL
START_URL = 'http://www.k618.cn/'

# 控制域，必须为list格式
DOMAIN = ['k618']
# 请求头
HEADERS = {
    'Host': 'www.k618.cn',
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
        "title": ".//*[contains(@class,'news_content')]/h1/text()",
        "news_date": "substring-before(.//*[@class='news_time_source'],'来源')",
        "source": "substring-after(.//*[@class='news_time_source'],'来源')",
        "author": "substring-before(substring-after(.//*[contains(text(),'作者')],'作者：'),'编辑')",
        "navigation": "string(.//*[@class='news_crumb'])",
        "content": ".//*[@class='TRS_Editor']/descendant::text()|.//*[@class='news_main']/descendant::text()",
        "editor": "substring-after(.//*[contains(text(),'编辑')],'编辑：')",
        "tags": "",
    }
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{6,8}/\w*\d+_\d+\.[s]*htm[l]*'

