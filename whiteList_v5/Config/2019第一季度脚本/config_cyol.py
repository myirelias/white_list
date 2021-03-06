# 中青在线
TASK_NAME = 'cyol'

# 起始URL
START_URL = 'http://www.cyol.com/'

# 控制域，必须为list格式
DOMAIN = ['cyol']
# 请求头
HEADERS = {
    'Host': 'www.cyol.com',
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
        "title": "string(.//h1)",
        "news_date": "substring(.//*[contains(text(),'发布时间')],6,17)",
        "source": "substring(.//*[contains(text(),'来源')],4,17)",
        "author": "substring-after(.//h6,'作者：')",
        "navigation": "string(normalize-space(.//*[@class='black14']|.//*[@class='mbx']))",
        "content": ".//*[@class='zhengwen']/descendant::text()|.//*[@class='content']/descendant::p/text()",
        "editor": "substring(normalize-space(.//*[@class='editor']|.//*[contains(text(),'编辑：')]),5,20)",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='bttitle'])",
        "news_date": "substring(substring-after(normalize-space(.//*[@class='laiy']),'发布时间：'),1,17)",
        "source": "substring-after(normalize-space(.//*[@class='laiy']),'来源：')",
        "author": "",
        "navigation": "normalize-space(.//*[@class='cont_left'])",
        "content": ".//*[@class='pictext']/descendant::text()",
        "editor": "translate(substring-after(.//*[contains(text(),'编辑')],'编辑：'),'】','')",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\w*_\d*\.[s]*htm[l]*'

