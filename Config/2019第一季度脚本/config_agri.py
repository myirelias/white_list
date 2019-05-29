# 中国农业信息网
TASK_NAME = 'agri'

# 起始URL
START_URL = 'http://www.agri.cn/'

# 控制域，必须为list格式
DOMAIN = ['agri']
# 请求头
HEADERS = {
    'Host': 'www.agri.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
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
        "title": "string(.//*[@class='nr_m14'])",
        "news_date": "substring-after(.//*[contains(text(),'日期')],'日期：')",
        "source": "substring-after(.//*[contains(text(),'来源')],'来源：')",
        "author": "substring-after(.//*[contains(text(),'作者')],'作者：')",
        "navigation": "substring-after(.//*[contains(text(),'您现在的位置')],'：')",
        "content": ".//*[@id='TRS_AUTOADD']/descendant::p/text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "string(.//*[@class='hui_15_cu'])",
        "news_date": "substring-before(substring-after(.//*[contains(text(),'日期：')],'日期：'),'作者')",
        "source": "substring-before(substring-after(.//*[contains(text(),'来源：')],'来源：'),'点击')",
        "author": "substring-before(substring-after(.//*[contains(text(),'作者：')],'作者：'),'来源')",
        "navigation": "substring-after(.//*[contains(text(),'您现在的位置')],':')",
        "content": ".//*[@id='TRS_AUTOADD']/descendant::p/text()|.//*[@class='TRS_Editor']/descendant::p/text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='STYLE5'])",
        "news_date": "normalize-space(html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr[2]/td)",
        "source": "",
        "author": "",
        "navigation": "substring-after(.//*[contains(text(),'您所在的位置')],'：')",
        "content": "html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr[3]/td/descendant::text()",
        "editor": "",
        "tags": ""
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{6,8}/\w*\d*_\d*\.[s]*htm[l]*'

