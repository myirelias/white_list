# 铁血网
TASK_NAME = 'tiexue'

# 起始URL
START_URL = 'https://www.tiexue.net/'

# 控制域，必须为list格式
DOMAIN = ['tiexue']
# 请求头
HEADERS = {
    'Host': 'www.tiexue.net',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.tiexue.net/',
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
        "title": "normalize-space(.//*[@class='title'])",
        "news_date": "substring(substring-after(normalize-space(.//*[@class='auteurInfo']),';'),1,18)",
        "source": "substring-before(normalize-space(.//*[@class='auteurInfo']),'document')",
        "author": "",
        "navigation": "normalize-space(.//*[@class='crumbs'])",
        "content": ".//*[@class='newconli2']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='a-title'])",
        "news_date": "substring-after(normalize-space(.//*[@class='time']),'发布时间：')",
        "source": "substring-after(normalize-space(.//*[contains(text(),'来源')]),'来源：')",
        "author": "substring-after(normalize-space(.//*[@class='author_name']),'作者:')",
        "navigation": "",
        "content": ".//*[@class='newconli2']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='post_tit'])",
        "news_date": "normalize-space(.//span[@class='float_L'])",
        "source": "",
        "author": "",
        "navigation": "",
        "content": ".//*[@class='newconli2']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='titles'])",
        "news_date": "normalize-space(.//*[@class='date'])",
        "source": "",
        "author": "",
        "navigation": "normalize-space(.//*[contains(@class,'positions')])",
        "content": ".//*[@class='talks']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'post[\d_]*\.s*html*'

# 页面编码
PAGE_CODE = 'gbk'

