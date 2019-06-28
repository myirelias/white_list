# 中国新闻网
TASK_NAME = 'chinanews'

# 起始URL
START_URL = 'http://www.chinanews.com/'

# 控制域，必须为list格式
DOMAIN = ['chinanews.com']
# 请求头
HEADERS = {
    'Host': 'www.chinanews.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0'
}


# xpath规则
XPATHER_HREF = ".//*/@href"
# 字段模版
# {
#     "title": "",
#     "publish_time": "",
#     "source": "",
#     "author": "",
#     "belong": "",
#     "content": "",
#     "editor": "",
# },
XPATHER_NEWS_LIST = [
    {
        "title": ".//*/h1/text()",
        "publish_time": "substring-before(.//*[@class='left-time'],'来源')",
        "source": "substring-before(substring-after(.//*[@class='left-time'],'来源'),' ')",
        "author": "",
        "belong": "string(.//*[@id='nav'])",
        "content": ".//*[@class='left_zw']/descendant::p/text()",
        "editor": "substring-after(.//*[contains(text(),'责任编辑')],'编辑')",
    },
    {
        "title": ".//*[@id='mian']//*[@class='title']/text()",
        "publish_time": "substring-before(substring-after(.//*[contains(text(),'发布时间')],'发布时间：'),'【')",
        "source": "",
        "author": "",
        "belong": "substring-after(.//*[contains(text(),'你的位置')],'你的位置：')",
        "content": ".//*[@class='t3']/descendant::text()",
        "editor": "substring-before(substring-after(.//*[contains(text(),'编辑')],'编辑：'),'】')",
    }

]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{4}/\d{2}-\d{2}/\d+.[s]*htm[l]*'

# pagecode
PAGECODE = 'gb2312'

