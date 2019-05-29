# 景德镇在线
TASK_NAME = 'jdzol'

# 起始URL
START_URL = 'http://www.jdzol.com/'

# 控制域，必须为list格式
DOMAIN = ['jdzol']
# 请求头
HEADERS = {
    'Host': 'www.jdzol.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Cookie': 'Hm_lvt_c0dee1fd89bb5c3bd1bd14d26222fb01=1557391719; Hm_lpvt_c0dee1fd89bb5c3bd1bd14d26222fb01=1557391719',
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
        "title": "substring-before(normalize-space(.//*[@id='Article']/h1),'发布时间')",
        "news_date": "substring-before(substring-after(normalize-space(.//*[@id='Article']/h1),'发布时间：'),'作者')",
        "source": "substring-after(normalize-space(.//*[@id='Article']/h1),'来源：')",
        "author": "substring-before(substring-after(normalize-space(.//*[@id='Article']/h1),'作者：'),'来源')",
        "navigation": "normalize-space(.//*[@class='crumbs'])",
        "content": ".//*[@class='content']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\w*_\d*/\d*\.s*html*'


