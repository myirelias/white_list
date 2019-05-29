# 全球金属网
TASK_NAME = 'ometal'

# 起始URL
START_URL = 'http://www.ometal.com/'

# 控制域，必须为list格式
DOMAIN = ['ometal']
# 请求头
HEADERS = {
    'Host': 'www.ometal.com',
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
        "title": "normalize-space(.//h1)",
        "news_date": "substring(normalize-space(.//*[contains(text(),'来源')]),1,18)",
        "source": "substring-before(substring-after(normalize-space(.//*[contains(text(),'来源')]),'来源:'),'字体')",
        "author": "",
        "navigation": "normalize-space(.//*[@class='s9' and @valign='middle' and @align='center'])",
        "content": ".//*[@id='fontzoom']/descendant::text()",
        "editor": "substring-before(substring-after(normalize-space(.//*[contains(text(),'责任编辑')]),'责任编辑：'),' ')",
        "tags": ".//*[@name='Keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'(/\d*)+/\w*/\d*\.s*html*'

