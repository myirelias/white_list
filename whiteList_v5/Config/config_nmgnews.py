# 内蒙古新闻网
TASK_NAME = 'nmg_news'

# 起始URL',
START_URL = 'http://www.nmgnews.com.cn/'

# 控制域，必须为list格式
DOMAIN = ['nmgnews.com.cn']
# 请求头
HEADERS = {
    'Host': 'www.nmgnews.com.cn',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
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
        "title": ".//*[@class='black24']/text()",
        "publish_time": ".//*[@id='div3']/span[1]/text()",
        "source": "substring-after(.//*[@id='div3']//*[contains(text(),'来源')],'来源：')",
        "author": "",
        "belong": "substring-after(.//*/ul[@class='black12'],'位置 ：')",
        "content": ".//*[@id='div_content']/descendant::text()",
        "editor": "substring-before(substring-after(.//*[contains(text(),'编辑')],'编辑:'),']')",
    },
    {
        "title": ".//*[@class='STYLE5']/text()",
        "publish_time": ".//*[@align='center']/font[1]/descendant::text()",
        "source": ".//*[@class='STYLE11']/text()",
        "author": "",
        "belong": "substring-after(.//*[@class='STYLE11 STYLE14'],'位置 ：')",
        "content": ".//*[@id='pzoom']/descendant::text()",
        "editor": "substring-before(substring-after(.//*[contains(text(),'编辑')],'编辑'),']')",
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{4}/\d{2}/\d{2}/\d+\.[s]*htm[l]*'
