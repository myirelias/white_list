# 中青网
TASK_NAME = 'youth'

# 起始URL
START_URL = 'http://www.youth.cn/'

# 控制域，必须为list格式
DOMAIN = ['youth.cn']
# 请求头
HEADERS = {
    'Host': 'www.youth.cn',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://news.youth.cn/',
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
        "title": ".//*[@class='l_tit']/text()",
        "publish_time": "substring-after(.//*[@id='pubtime_baidu'],'时间：')",
        "soruce": "substring-after(.//*[@id='source_baidu'],'来源：')",
        "author": "",
        "belong": "string(.//*[@class='hd_meun_jk1'])",
        "content": ".//*[@class='article']/descendant::p/descendant::text()",
        "editor": "substring-after(.//*[@id='editor_baidu'],'编辑：')",
    },
    {
        "title": ".//*[@class='page_title']/h1/descendant::text()",
        "publish_time": "substring-after(.//*[contains(text(),'发稿时间')],'发稿时间：')",
        "soruce": "substring-after(.//*[contains(text(),'来源')],'来源：')",
        "author": "",
        "belong": "string(.//*[@class='floleft page_zi'])",
        "content": ".//*[@id='container']/descendant::p/descendant::text()|.//*[@id='container']/descendant::text()",
        "editor": "substring-after(.//*[contains(text(),'责任编辑')],'编辑：')",
    },
    {
        "title": ".//*[@class='pbt']/descendant::text()",
        "publish_time": "substring-before(substring-after(.//*[contains(text(),'发稿时间')],'发稿时间：'),'来源')",
        "source": "substring-after(.//*[contains(text(),'来源')],'来源：')",
        "author": "",
        "belong": "string(.//*[@class='lm_mc'])",
        "content": ".//*[@class='page_text']/descendant::text()",
        "editor": "substring-after(.//*[contains(text(),'责任编辑')],'编辑：')",
    }
]


# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{6,8}/[\w]*\d{6,8}_\d+\.[s]*htm[l]*'
