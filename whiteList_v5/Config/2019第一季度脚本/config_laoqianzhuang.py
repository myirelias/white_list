# 老钱庄
TASK_NAME = 'laoqianzhuang'

# 起始URL
START_URL = 'https://www.laoqianzhuang.com/'

# 控制域，必须为list格式
DOMAIN = ['laoqianzhuang']
# 请求头
HEADERS = {
    'Host': 'www.laoqianzhuang.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
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
        "title": "normalize-space(.//*[@class='atc-head'])",
        "news_date": "normalize-space(.//*[@id='pubtime_baidu'])",
        "source": "substring(normalize-space(.//*[@id='source_baidu']),4,50)",
        "author": "",
        "navigation": "substring(normalize-space(.//*[contains(text(),'当前位置：')]),6,200)",
        "content": ".//*[@class='atc-content']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d*/\d*\.s*html*'

