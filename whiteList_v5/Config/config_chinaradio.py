# 央广网
TASK_NAME = 'china_radio'

# 起始URL
START_URL = 'http://www.cnr.cn/'

# 控制域，必须为list格式
DOMAIN = ['cnr.cn']
# 请求头
HEADERS = {
    'Host': 'www.cnr.cn',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:52.0) Gecko/20100101 Firefox/52.0',
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
        "title": ".//*[@class='subject']/h2/text()",
        "publish_time": "substring-before(.//*[@class='source'],'来源')",
        "soruce": "substring-after(.//*[@class='source'],'来源：')",
        "author": "",
        "belong": "string(.//*[@class='daoHang'])",
        "content": ".//*[starts-with(@class,'content')]/descendant::p/descendant::text()",
        "editor": "substring-after(.//*[contains(text(),'编辑')],'编辑：')",
    },
    {
        "title": ".//*/h1/text()",
        "publish_time": ".//*[@id='pubtime_baidu']/text()",
        "source": "substring-after(.//*[@id='source_baidu'],'来源：')",
        "author": "",
        "belong": ".//*[@class='CurrChnlCls']/text()",
        "content": ".//*[@class='TRS_Editor']/descendant::text()",
        "editor": "substring-after(.//*[contains(text(),'责编')],'责编：')",
    }

]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{6,8}/[\w]*\d+_\d+\.[s]*htm[l]*'

