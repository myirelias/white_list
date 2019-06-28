# 中华龙都
TASK_NAME = 'zhld'

# 起始URL
START_URL = 'http://www.zhld.com/'

# 控制域，必须为list格式
DOMAIN = ['zhld']
# 请求头
HEADERS = {
    'Host': 'www.zhld.com',
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
        "title": "normalize-space(.//*[@class='h1'])",
        "news_date": "normalize-space(.//*[contains(text(),'来源')]/parent::span/parent::td/following-sibling::td)",
        "source": "substring-after(normalize-space(.//*[contains(text(),'来源')]),'来源：')",
        "author": "",
        "navigation": "substring(normalize-space(.//*[contains(text(),'您当前的位置')]),9,100)",
        "content": ".//*[@class='STYLE9']/descendant::text()",
        "editor": "translate(substring-after(normalize-space(.//*[contains(text(),'责任编辑')]),'编辑：'),']','')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[contains(@class,'new_tit')]/h2)",
        "news_date": "normalize-space(.//*[@class='time'])",
        "source": "substring-after(normalize-space(.//*[@class='resource']),'来源：')",
        "author": "substring-after(normalize-space(.//*[@class='author']),'作者：')",
        "navigation": "normalize-space(.//*[@class='nav_dh'])",
        "content": ".//*[@id='text_fix']/descendant::text()",
        "editor": "substring-before(substring-after(normalize-space(.//*[contains(text(),'责任编辑')]),'责任编辑：'),']')",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{4}-\d{2}/\d{2}/content_\d*\.s*html*'


