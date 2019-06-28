# 中国教育新闻网
TASK_NAME = 'jyb'

# 起始URL
START_URL = 'http://www.jyb.cn/'

# 控制域，必须为list格式
DOMAIN = ['jyb']
# 请求头
HEADERS = {
    'Host': 'www.jyb.cn',
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
        "title": "normalize-space(.//*[@class='xl_title']/h1)",
        "news_date": "substring-after(normalize-space(.//*[contains(text(),'发布时间')]),'发布时间：')",
        "source": "substring-after(normalize-space(.//*[@id='js_source']),'来源：')",
        "author": "substring-after(normalize-space(.//*[contains(text(),'作者')]),'作者：')",
        "navigation": "normalize-space(.//*[@class='yxj_station'])",
        "content": ".//*[@class='xl_text']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{6,8}/[\w\d_]*\.s*html*'


