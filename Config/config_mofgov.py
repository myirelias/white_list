# 财政部
TASK_NAME = 'mof_gov'

# 起始URL
START_URL = 'http://www.mof.gov.cn/index.htm'

# 控制域，必须为list格式
DOMAIN = ['mof.gov.cn']
# 请求头
HEADERS = {
    'Host': 'www.mof.gov.cn',
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
        "title": ".//*[@class='font_biao1']/text()",
        "publish_time": "substring-before(.//*[contains(text(),'来源')],'来源')",
        "soruce": "substring-after(.//*[contains(text(),'来源')],'来源：')",
        "author": "",
        "belong": "substring-after(.//*[contains(text(),'当前位置')],'当前位置：')",
        "content": ".//*[@class='TRS_Editor']/descendant::p/text()",
        "editor": "",
    },

]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{6,8}/\w*\d+_\d+\.[s]*htm[l]*'


# 财政部需要正则替换的
# pattern = re.compile(r'/index.[s]*htm[l]*/')
# res = re.sub(pattern, '/', url)