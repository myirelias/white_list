# 保定政府网
TASK_NAME = 'bd'

# 起始URL
START_URL = 'http://www.bd.gov.cn/'

# 控制域，必须为list格式
DOMAIN = ['bd']
# 请求头
HEADERS = {
    'Host': 'www.bd.gov.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
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
        "title": "normalize-space(.//*[@class='sj_bt'])",
        "news_date": "substring(substring-after(normalize-space(.//*[contains(text(),'发布时间')]),'发布时间：'),1,10)",
        "source": "",
        "author": "substring-after(normalize-space(.//*[contains(text(),'发布时间')]),'发布人：')",
        "navigation": "substring-after(normalize-space(.//*[@class='ej_rdqwz']),'当前位置：')",
        "content": ".//*[@class='sj_nr']/descendant::text()",
        "editor": "",
        "tags": ""
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/content[-\d]*\.s*html*'


