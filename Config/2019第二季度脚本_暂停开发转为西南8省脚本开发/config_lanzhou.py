# 中国兰州网
TASK_NAME = 'lanzhou'

# 起始URL
START_URL = 'http://www.lanzhou.cn/'

# 控制域，必须为list格式
DOMAIN = ['lanzhou']
# 请求头
HEADERS = {
    'Host': 'www.lanzhou.cn',
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
        "title": "normalize-space(.//*[@id='main']/h1)",
        "news_date": "concat(2,substring-after(normalize-space(.//*[@class='con_top']),'2'))",
        "source": "substring-after(normalize-space(.//*[contains(text(),'稿源')]),'稿源：')",
        "author": "",
        "navigation": "translate(substring-after(normalize-space(.//*[@class='postion']/span),'您当前的位置'),'：','')",
        "content": ".//*[@class='main_con']/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[contains(text(),'编辑')]),'编辑：')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@id='biaotiy']/h1)",
        "news_date": "substring-before(substring-after(normalize-space(.//*[@id='biaotiyx']),'发布时间：'),'【')",
        "source": "substring-before(substring-after(normalize-space(.//*[@id='biaotiyx']),'稿源：'),'编辑')",
        "author": "",
        "navigation": "translate(substring-after(normalize-space(.//*[@class='duiqi']),'您当前的位置'),'：','')",
        "content": ".//*[@class='neirongkuang']/descendant::text()",
        "editor": "substring-before(substring-after(normalize-space(.//*[@id='biaotiyx']),'编辑：'),'发布时间')",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'[/\d]*\.s*html*'


