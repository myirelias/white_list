# 雅安市人民政府
TASK_NAME = 'yaan'

# 起始URL
START_URL = 'http://www.yaan.gov.cn/'

# 控制域，必须为list格式
DOMAIN = ['yaan']
# 请求头
HEADERS = {
    'Host': 'www.yaan.gov.cn',
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
        "title": "normalize-space(.//*[@class='xq-title'])",
        "news_date": "normalize-space(.//*[@class='time pubtime']|.//*[contains(text(),'发布日期')]/following-sibling::div[1])",
        "source": "normalize-space(.//*[@class='map laiyuan']|.//*[contains(text(),'发布机构')]/following-sibling::div[1])",
        "author": "",
        "navigation": "",
        "content": ".//*[@class='xqing-web-box']/descendant::text()",
        "editor": "",
        "tags": ".//*[contains(@name,'eywords')]/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/show/[\d\w-]*\.s*html*'


