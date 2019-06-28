# 中国电力新闻网
TASK_NAME = 'cpnn'

# 起始URL
START_URL = 'http://www.cpnn.com.cn/'

# 控制域，必须为list格式
DOMAIN = ['cpnn']
# 请求头
HEADERS = {
    'Host': 'www.cpnn.com.cn',
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
        "title": "normalize-space(.//*[@class='cpnn-con-title']/h1)",
        "news_date": "substring-after(normalize-space(.//*[@class='cpnn-zhengwen-time']),'日期：')",
        "source": "substring-before(substring-after(normalize-space(.//*[@class='cpnn-zhengwen-time']),'来源：'),'日期')",
        "author": "",
        "navigation": "substring-after(normalize-space(.//*[@class='cpnn-minnav']),'您的位置>')",
        "content": ".//*[@class='cpnn-con-zhenwen']/descendant::p/text()",
        "editor": "substring-after(normalize-space(.//*[contains(text(),'责任编辑')]),'编辑：')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='hdtitle']/h1)",
        "news_date": "substring-after(normalize-space(.//*[@class='tiebar']/span[3]),'日期：')",
        "source": "substring-after(normalize-space(.//*[@class='tiebar']/span[1]),'来源：')",
        "author": "substring-after(normalize-space(.//*[@class='tiebar']/span[2]),'作者：')",
        "navigation": "substring-after(normalize-space(.//*[@class='mianbaoxie']),'您的位置>')",
        "content": ".//*[@id='Zoom']/descendant::p/text()",
        "editor": "substring-after(normalize-space(.//*[contains(text(),'责任编辑')]),'编辑：')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='F-title'])",
        "news_date": "substring-after(normalize-space(.//*[@class='cDGray']),'日期：')",
        "source": "substring-before(substring-after(normalize-space(.//*[@class='cDGray']),'来源：'),'作者')",
        "author": "substring-before(substring-after(normalize-space(.//*[@class='cDGray']),'作者：'),'日期')",
        "navigation": "translate(normalize-space(.//*[@class='title02']),'您的位置','')",
        "content": ".//*[@id='zoom']/descendant::p/text()",
        "editor": "substring-after(normalize-space(.//*[contains(text(),'责任编辑')]),'编辑：')",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{6,8}/[\d\w_]*\.s*html*'


