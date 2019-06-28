# 维科网
TASK_NAME = 'changsha'

# 起始URL
START_URL = 'http://www.changsha.cn/'

# 控制域，必须为list格式
DOMAIN = ['changsha']
# 请求头
HEADERS = {
    'Host': 'www.changsha.cn',
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
        "title": "normalize-space(.//*[@class='maintitle'])",
        "news_date": "substring-after(substring-after(normalize-space(.//*[@class='detail_source']),'作者'),'|')",
        "source": "substring-before(substring-after(normalize-space(.//*[@class='detail_source']),'来源：'),'|')",
        "author": "substring-before(substring-after(normalize-space(.//*[@class='detail_source']),'作者：'),'|')",
        "navigation": "substring(normalize-space(.//*[@class='position']),8,200)",
        "content": ".//*[@class='article_content']/descendant::text()",
        "editor": "",
        "tags": ""
    },
    {
        "title": "normalize-space(.//*[@class='text']/h1)",
        "news_date": "substring-after(normalize-space(.//*[@class='time']),'|')",
        "source": "translate(substring-after(normalize-space(.//*[contains(text(),'来源：')]),'来源：'),'】','')",
        "author": "",
        "navigation": "substring(normalize-space(.//*[@class='location']),6,200)",
        "content": ".//*[@id='tempNewsContentDiv']/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[@class='source']),'编辑：')",
        "tags": ""
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'[/\d*]*\.s*html*'

