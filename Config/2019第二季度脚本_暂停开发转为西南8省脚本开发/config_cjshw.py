# 昌吉生活网
TASK_NAME = 'cjshw'

# 起始URL
START_URL = 'https://www.cjshw.com/'

# 控制域，必须为list格式
DOMAIN = ['cjshw']
# 请求头
HEADERS = {
    'Host': 'www.cjshw.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
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
        "title": "normalize-space(.//*[@class='Title_ch'])",
        "news_date": "substring-before(substring-after(normalize-space(.//*[contains(text(),'新闻来源')]/parent::div),'发布时间：'),'阅读量')",
        "source": "substring-after(normalize-space(.//*[contains(text(),'新闻来源')]/parent::div),'新闻来源：')",
        "author": "",
        "navigation": ".//*[@class='y_h_logo']/img/@alt",
        "content": ".//*[@class='ul_htmlinfo']/descendant::text()",
        "editor": "substring-before(substring-after(normalize-space(.//*[contains(text(),'新闻来源')]/parent::div),'责任编辑：'),'审核')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='title'])",
        "news_date": "substring(normalize-space(.//*[contains(text(),'发布时间')]),7,100)",
        "source": "substring-after(normalize-space(.//*[contains(text(),'新闻来源')]),'来源：')",
        "author": "",
        "navigation": ".//*[@class='y_h_logo']/img/@alt",
        "content": ".//*[@class='edit editwz']/descendant::text()",
        "editor": "substring-before(substring-after(normalize-space(.//*[contains(text(),'责任编辑')]),'责任编辑：'),'审核')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='container']//h2)",
        "news_date": "substring(substring-after(normalize-space(.//*[contains(text(),'发布时间')]),'发布时间：'),1,10)",
        "source": "substring-before(substring-after(normalize-space(.//*[contains(text(),'发布时间')]),'新闻来源：'),'手机')",
        "author": "",
        "navigation": "normalize-space(.//*[contains(text(),'当前位置')]|.//*[@class='nohover']/parent::div)",
        "content": ".//*[@class='cj_new_detail']/descendant::text()",
        "editor": "substring-before(substring-after(normalize-space(.//*[contains(text(),'发布时间')]),'责任编辑：'),'审核')",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/news/detail/id/\d*\.s*html*'


