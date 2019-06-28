# 饲料行业信息网
TASK_NAME = 'feedtrade'

# 起始URL
START_URL = 'http://www.feedtrade.com.cn/'

# 控制域，必须为list格式
DOMAIN = ['feedtrade']
# 请求头
HEADERS = {
    'Host': 'www.feedtrade.com.cn',
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
        "title": "normalize-space(.//*[@class='title'])",
        "news_date": "substring(substring-after(normalize-space(.//*[@class='wzly']),'更新时间：'),1,20)",
        "source": "substring-before(substring-after(normalize-space(.//*[@class='wzly']),'来源：'),'更新时间')",
        "author": "translate(substring-after(normalize-space(.//*[@class='zz']),'作者'),':：）)','')",
        "navigation": "normalize-space(.//*[@id='menudir']/dl)",
        "content": ".//*[@class='zwbf']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@id='newsTitle'])",
        "news_date": "concat(2,substring(substring-after(normalize-space(.//*[@id='newsTitle']/parent::td/parent::tr/following-sibling::tr),'2'),1,19))",
        "source": "substring(substring-after(normalize-space(.//*[@id='newsTitle']/parent::td/parent::tr/following-sibling::tr),'2'),20,200)",
        "author": "",
        "navigation": "normalize-space(.//*[@id='menu']/following-sibling::table[1]//*[@align='left'])",
        "content": ".//*[@class='ReplyContent']/descendant::p/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//h1)",
        "news_date": "substring-after(normalize-space(.//*[contains(text(),'文章来源')]),'更新时间：')",
        "source": "substring-before(substring-after(normalize-space(.//*[contains(text(),'文章来源')]),'文章来源：'),'作者')",
        "author": "substring-before(substring-after(normalize-space(.//*[contains(text(),'文章来源')]),'作者：'),'更新时间')",
        "navigation": "normalize-space(.//*[@class='white']//a[contains(text(),'首页') and @href='http://www.feedtrade.com.cn/']/parent::td)",
        "content": ".//*[@class='ReplyContent']/descendant::p/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d*\.s*html*'


