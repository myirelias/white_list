# 正义网
TASK_NAME = 'jcrb'

# 起始URL
START_URL = 'http://www.jcrb.com/'

# 控制域，必须为list格式
DOMAIN = ['jcrb']
# 请求头
HEADERS = {
    'Host': 'www.jcrb.com',
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
        "title": "normalize-space(.//*[@id='mainLeft']/h1)",
        "news_date": "substring(normalize-space(.//*[@id='pubtime_baidu']),4,50)",
        "source": "substring(normalize-space(.//*[@id='source_baidu']),6,50)",
        "author": "substring(normalize-space(.//*[@id='author_baidu']),4,50)",
        "navigation": "normalize-space(.//*[@class='curpage'])",
        "content": ".//*[@class='mainContent']/descendant::text()",
        "editor": "translate(substring-after(normalize-space(.//*[@id='editor_baidu']),'：'),']','')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='wzbt'])",
        "news_date": "substring(normalize-space(.//*[contains(text(),'时间')]),4,20)",
        "source": "substring-after(normalize-space(.//*[contains(text(),'时间')]),'新闻来源：')",
        "author": "substring-before(substring-after(normalize-space(.//*[contains(text(),'作者')]),'作者：'),'新闻来源')",
        "navigation": "substring-after(normalize-space(.//*[contains(text(),'当前位置')]),'：')",
        "content": ".//*[@class='wzzw']/descendant::text()",
        "editor": "translate(substring-after(normalize-space(.//*[contains(text(),'责任编辑')]),'责任编辑：'),']','')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@id='article']/h1)",
        "news_date": "substring-after(normalize-space(.//*[@id='about']/span[1]),'时间：')",
        "source": "substring-after(normalize-space(.//*[@id='about']/span[3]),'来源：')",
        "author": "substring-after(normalize-space(.//*[@id='about']/span[2]),'作者：')",
        "navigation": "normalize-space(.//*[@id='curpage'])",
        "content": ".//*[@class='Custom_UnionStyle']/descendant::text()",
        "editor": "translate(substring-after(normalize-space(.//*[contains(text(),'责任编辑')]),'责任编辑：'),']','')",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d*/\w*\d*[_]*\d*\.[s]*htm[l]*'

