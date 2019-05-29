# 乐居网
TASK_NAME = 'leju'

# 起始URL
START_URL = 'http://sc.leju.com/'

# 控制域，必须为list格式
DOMAIN = ['leju']
# 请求头
HEADERS = {
    'Host': 'sc.leju.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://www.leju.com/',
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
        "title": "normalize-space(.//*[@class='title'])",
        "news_date": "substring(translate(normalize-space(.//*[@class='origin']),'原创',''),1,20)",
        "source": "substring-before(substring-after(normalize-space(.//*[@class='origin']),'来源：'),'作者')",
        "author": "substring-after(normalize-space(.//*[@class='origin']),'作者：')",
        "navigation": "normalize-space(.//*[@class='breadcrumb'])",
        "content": ".//*[@class='article-body']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='Keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='l_tit'])",
        "news_date": "normalize-space(.//*[@class='l_infoBox']/span[1])",
        "source": "substring-after(normalize-space(.//*[contains(text(),'来源')]),'：')",
        "author": "",
        "navigation": "normalize-space(.//*[@class='crumbs'])",
        "content": ".//*[@id='editHTML']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='Keywords']/@content"
    }
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/[\d-]*/\d*\.s*html*'

