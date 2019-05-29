# 阿拉宁波网
TASK_NAME = 'cnnb'

# 起始URL
START_URL = 'http://www.cnnb.com/'

# 控制域，必须为list格式
DOMAIN = ['cnnb']
# 请求头
HEADERS = {
    'Host': 'www.cnnb.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Cookie': 'sUr8_3477_saltkey=MS8xhB8j; sUr8_3477_lastvisit=1547527239; sUr8_3477_lastact=1547530951%09forum.php%09ajax; UM_distinctid=168501244e22-0b19e4d8d529248-4c322a79-1fa400-168501244e3160; CNZZDATA546031=cnzz_eid%3D371853708-1547530079-%26ntime%3D1547530079; sUr8_3477_st_t=0%7C1547530923%7Cbe3e415e072b259737a1e36761b2d70b; sUr8_3477_forum_lastvisit=D_188_1547530881D_22_1547530890D_5_1547530894D_59_1547530923; sUr8_3477_visitedfid=59D5D22D188',
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
        "title": ".//*[@class='ph']/text()",
        "news_date": "substring-before(.//*[@class='xg1'],'|')",
        "source": "substring-after(.//*[@class='xg1'],'来自:')",
        "author": "substring-before(substring-after(.//*[@class='xg1'],'发布者:'),'|')",
        "navigation": "string(.//*[@id='pt'])",
        "content": ".//*[@id='article_content']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\w*-\d*[-]*\d\.[s]*htm[l]*'

