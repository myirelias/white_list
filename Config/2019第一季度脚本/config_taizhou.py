# 中国台州网
TASK_NAME = 'taizhou'

# 起始URL
START_URL = 'http://www.taizhou.com.cn/'

# 控制域，必须为list格式
DOMAIN = ['taizhou']
# 请求头
HEADERS = {
    'Host': 'www.taizhou.com.cn',
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
        "title": "normalize-space(.//article/table[1]/descendant::tr[1]|.//*[contains(@class,'title')])",
        "news_date": "normalize-space(.//*[@id='pubtime_baidu'])",
        "source": "substring(normalize-space(.//*[@id='source_baidu']),4,50)",
        "author": "normalize-space(.//*[@id='author_baidu'])",
        "navigation": "substring(normalize-space(.//*[@class='head-track']),8,50)",
        "content": ".//*[contains(@class,'article-content')]/descendant::text()",
        "editor": "normalize-space(.//*[@id='editor_baidu'])",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@id='article']/h1)",
        "news_date": "substring-after(.//*[contains(text(),'发布时间')],'发布时间：')",
        "source": "substring-after(.//*[contains(text(),'来源')],'来源：')",
        "author": "substring-after(.//*[contains(text(),'作者')],'作者：')",
        "navigation": "normalize-space(.//*[@id='position'])",
        "content": ".//*[@id='content']/descendant::text()",
        "editor": "substring-after(.//*[contains(text(),'编辑')],'编辑:')",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/[\w*_]*\d*\.[s]*htm[l]*'

