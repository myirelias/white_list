# 消费日报
TASK_NAME = 'xfrb'

# 起始URL
START_URL = 'http://www.xfrb.com.cn/'

# 控制域，必须为list格式
DOMAIN = ['xfrb']
# 请求头
HEADERS = {
    'Host': 'www.xfrb.com.cn',
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
#     "news_date": "",
#     "source": "",
#     "author": "",
#     "navigation": "",
#     "content": "",
#     "editor": "",
#     "tags": "",
# },
XPATHER_NEWS_LIST = [
    {
        "title": ".//*[@class='title']/text()",
        "news_date": "substring-after(substring-before(.//*[contains(text(),'发布时间')],'来源'),'发布时间：')",
        "source": "substring-after(.//*[contains(text(),'发布时间')],'来源：')",
        "author": "",
        "navigation": "string(.//*[@class='content_left']/h1)",
        "content": ".//*[@class='content_div']/descendant::text()",
        "editor": "substring-before(substring-after(.//*[contains(text(),'责任编辑')],'责任编辑：'),'】')",
        "tags": ".//*[@name='keywords']/@content",
    },
    {
        "title": ".//*[@class='head_title']/descendant::text()",
        "news_date": "normalize-space(.//*[@class='head_detail_t'])",
        "source": "substring-before(substring-after(normalize-space(.//*[@class='head_detail']),'来源:'),'2')",
        "author": "substring-after(normalize-space(.//*[@class='head_detail']),'作者:')",
        "navigation": "normalize-space(.//*[@class='detail_location'])",
        "content": ".//*[@class='foto-inner']/descendant::text()",
        "editor": "translate(substring-after(normalize-space(.//*[contains(text(),'责任编辑')]),'责任编辑：'),'】','')",
        "tags": ".//*[@name='keywords']/@content",
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d+.[s]*htm[l]*'



