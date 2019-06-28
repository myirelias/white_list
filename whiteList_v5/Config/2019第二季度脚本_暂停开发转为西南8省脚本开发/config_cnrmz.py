# 中国民族广播网
TASK_NAME = 'cnrmz'

# 起始URL
START_URL = 'http://www.cnrmz.cn/'

# 控制域，必须为list格式
DOMAIN = ['cnrmz']
# 请求头
HEADERS = {
    'Host': 'www.cnrmz.cn',
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
        "title": "normalize-space(.//*[@id='text']/table[1]/tbody/tr)",
        "news_date": "substring-after(normalize-space(.//*[contains(text(),'来源')]),'更新时间：')",
        "source": "substring-before(substring-after(normalize-space(.//*[contains(text(),'来源')]),'来源：'),'|')",
        "author": "",
        "navigation": "translate(substring-after(normalize-space(.//*[@id='currentPosition']),'当前位置'),':：','')",
        "content": ".//*[@class='TRS_Editor']/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[contains(text(),'责编')]),'责编：')",
        "tags": ""
    },
    {
        "title": "normalize-space(.//*[@class='title'])",
        "news_date": "substring-before(normalize-space(.//*[@class='crtimefont']),'|')",
        "source": "substring-after(normalize-space(.//*[@class='crtimefont']),'来源：')",
        "author": ".//*[@name='author']/@content",
        "navigation": "",
        "content": ".//*[@class='TRS_Editor']/descendant::text()",
        "editor": "",
        "tags": ""
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{4,6}/[\w\d_]*\.s*html*'


