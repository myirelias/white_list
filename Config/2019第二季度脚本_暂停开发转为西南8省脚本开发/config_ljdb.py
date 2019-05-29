# 丽江读本
TASK_NAME = 'ljdb'

# 起始URL
START_URL = 'http://www.ljdb.net/'

# 控制域，必须为list格式
DOMAIN = ['ljdb']
# 请求头
HEADERS = {
    'Host': 'www.ljdb.net',
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
        "title": "normalize-space(.//*[@class='ph'])",
        "news_date": "substring-before(normalize-space(.//*[@class='xg1']),'|')",
        "source": "substring-after(normalize-space(.//*[@class='xg1']),'来自:')",
        "author": "substring-before(substring-after(normalize-space(.//*[@class='xg1']),'发布者:'),'|')",
        "navigation": "normalize-space(.//*[@class='nvhm']/parent::div)",
        "content": ".//*[@id='article_content']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@id='thread_subject'])",
        "news_date": ".//*[@id='postlist']/div[1]//*[contains(text(),'发表于')]/span/@title",
        "source": "",
        "author": "normalize-space(.//*[@id='postlist']/div[1]//*[@class='authi']//*[@class='xw1'])",
        "navigation": "normalize-space(.//*[@id='pt']//*[@class='z'])",
        "content": ".//*[@id='postlist']/div[1]//*[@class='t_f']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'portal\.php.*?mod=view.*?aid=\d*|forum\.php.*?mod=viewthread.*?tid=\d*'

