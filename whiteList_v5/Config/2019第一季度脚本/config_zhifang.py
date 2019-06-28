# 智房网
TASK_NAME = 'zhifang'

# 起始URL
START_URL = 'https://news.zhifang.com/'

# 控制域，必须为list格式
DOMAIN = ['zhifang']
# 请求头
HEADERS = {
    'Host': 'news.zhifang.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Cookie': 'SERVERID=f88a262107ceda83ac53521d0290dfcd|1547540755|1547540755; Hm_lvt_08bf4689a26352081a53384dcbe8999a=1547540763; Hm_lpvt_08bf4689a26352081a53384dcbe8999a=1547540763',
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
        "title": ".//*/h1/text()",
        "news_date": "substring-before(.//*[@class='source'],'来源')",
        "source": "substring-after(.//*[@class='source'],'来源：')",
        "author": "",
        "navigation": "string(.//*[@class='topnav'])",
        "content": ".//*[@class='box']/descendant::p/text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d*\.[s]*htm[l]*'

