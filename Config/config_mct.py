# 文化和旅游部
TASK_NAME = 'mct'

# 起始URL
START_URL = 'https://www.mct.gov.cn/'

# 控制域，必须为list格式
DOMAIN = ['mct.gov.cn']
# 请求头
HEADERS = {
    'Host': 'www.mct.gov.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
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
        "title": ".//*[@class='sp_title']/text()",
        "publish_time": "substring-before(substring-after(.//*[@class='sp_time'],'发布时间：'),'来源')",
        "soruce": "substring-before(substring-after(.//*[@class='sp_time'],'来源：'),'编辑')",
        "author": "",
        "belong": "substring-after(.//*[@class='bt-position'],'当前位置：')",
        "content": ".//*[@class='TRS_Editor']/descendant::text()",
        "editor": "substring-after(.//*[@class='sp_time'],'编辑：')",
    }
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/[\w]*\d*[_]*\d*\.[s]*htm[l]*'

