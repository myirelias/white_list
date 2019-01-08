# 半月谈
TASK_NAME = 'banyuetan'

# 起始URL
START_URL = 'http://www.banyuetan.org/'

# 控制域，必须为list格式
DOMAIN = ['banyuetan.org']
# 请求头
HEADERS = {
    'Host': 'www.banyuetan.org',
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
        "title": ".//*[@class='content_con_list']/h1/text()",
        "publish_time": "substring-before(.//*[@class='content_con_list']/h2,'来源')",
        "soruce": "substring-after(substring-before(.//*[@class='content_con_list']/h2,'编辑'),'来源：')",
        "author": "",
        "belong": "string(.//*[@class='content_con_tip'])",
        "content": ".//*[@class='text']/descendant::text()",
        "editor": "substring-before(substring-after(.//*[@class='content_con_list']/h2,'编辑'),'分享到')",
    },
    {
        "title": ".//*[@class='name']/text()",
        "publish_time": "substring-before(.//*[@class='mess'],'来源')",
        "source": "substring-after(.//*[contains(text(),'来源')],'来源：')",
        "author": "",
        "belong": "substring-after(.//*[@class='navigation'],'当前位置：')",
        "content": ".//*[@id='MyContent']/descendant::text()",
        "editor": "substring-before(substring-after(.//*[contains(text(),'编辑')],'编辑：'),')')",
    },
    {
        "title": ".//*[@class='detail_tit']/h1/text()",
        "publish_time": ".//*[@class='detail_tit_time']/text()",
        "source": "substring-after(.//*[contains(text(),'来源')],'来源：')",
        "author": "",
        "belong": "substring-after(.//*[@class='navigation'],'当前位置：')",
        "content": ".//*[@class='detail_content']/descendant::text()",
        "editor": "substring-after(.//*[contains(text(),'责任编辑')],'责任编辑：')",

    }
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d*[_]*\d*\.[s]*htm[l]*'

