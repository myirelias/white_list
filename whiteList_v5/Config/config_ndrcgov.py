# 发改委
TASK_NAME = 'ndrc_gov'

# 起始URL
START_URL = 'http://www.ndrc.gov.cn/'

# 控制域，必须为list格式
DOMAIN = ['ndrc.gov.cn']
# 请求头
HEADERS = {
    'Host': 'www.ndrc.gov.cn',
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
        "title": ".//*[@align='center']//*[@style='font-size: 18pt']/text()",
        "publish_time": ".//*[contains(text(),'年') and contains(text(),'月') and contains(text(),'日')]/text()",
        "soruce": "",
        "author": "",
        "belong": "string(.//*[@class='position'])",
        "content": ".//*[@class='TRS_Editor']/descendant::text()",
        "editor": "",
    },
    {
        "title": ".//*/font[@size='5']/descendant::text()",
        "publish_time": "",
        "source": "substring-after(.//*[contains(text(),'来源')],'来源：')",
        "author": "",
        "belong": "string(.//*[@class='position'])",
        "content": ".//*[@class='TRS_Editor']/descendant::text()",
        "editor": "",
    },
    {
        "title": ".//*[@class='txt_title1']/text()",
        "publish_time": "",
        "source": "substring-before(substring-after(.//*[contains(text(),'来源')],'来源：'),'）')",
        "author": "",
        "belong": "string(.//*[@class='position'])",
        "content": ".//*[@class='TRS_Editor']/descendant::text()",
        "editor": "",
    },
    {
        "title": ".//*[contains(@class,'txt_title')]/text()",
        "publish_time": "substring-before(.//*[contains(@class,'txt_subtitle')],'来源')",
        "source": "substring-after(.//*[contains(text(),'来源')],'来源：')",
        "author": "",
        "belong": "",
        "content": ".//*[@class='TRS_Editor']/descendant::text()",
        "editor": "",
    }
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{6,8}/\w*\d+_\d+\.[s]*htm[l]*'

