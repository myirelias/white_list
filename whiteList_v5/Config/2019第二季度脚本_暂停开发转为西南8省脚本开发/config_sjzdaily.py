# 石家庄新闻网
TASK_NAME = 'sjzdaily'

# 起始URL
START_URL = 'http://www.sjzdaily.com.cn/'

# 控制域，必须为list格式
DOMAIN = ['sjzdaily']
# 请求头
HEADERS = {
    'Host': 'www.sjzdaily.com.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
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
        "title": "normalize-space(.//*[@class='art_title'])",
        "news_date": "substring-before(substring-after(normalize-space(.//*[@class='info']),'时间：'),'来源')",
        "source": "substring-after(normalize-space(.//*[@class='info']),'来源：')",
        "author": "",
        "navigation": "normalize-space(.//*[@class='breadcrumbnav'])",
        "content": ".//*[@class='content']/descendant::text()",
        "editor": "normalize-space(.//*[@class='dutyofficer'])",
        "tags": ""
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{4}-\d{2}/\d*/content_\d*\.s*html*'



