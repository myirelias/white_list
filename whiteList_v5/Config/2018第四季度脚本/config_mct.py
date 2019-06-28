# 文化和旅游部
TASK_NAME = 'mct'

# 起始URL
START_URL = 'https://www.mct.gov.cn/'

# 控制域，必须为list格式
DOMAIN = ['mct']
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
#     "news_date": "",
#     "source": "",
#     "author": "",
#     "navigation": "",
#     "content": "",
#     "editor": "",
#     "tags": "",
# },
XPATHER_NEWS_LIST = [
    {
        "title": ".//*[@class='sp_title']/text()",
        "news_date": "substring-before(substring-after(.//*[@class='sp_time'],'发布时间：'),'来源')",
        "soruce": "substring-before(substring-after(.//*[@class='sp_time'],'来源：'),'编辑')",
        "author": "",
        "navigation": "substring-after(.//*[@class='bt-position'],'当前位置：')",
        "content": ".//*[@class='TRS_Editor']/descendant::text()",
        "editor": "substring-after(.//*[@class='sp_time'],'编辑：')",
        "tags": "",
    },
    {
        "title": "normalize-space(.//*[@class='docTitleCls'])",
        "news_date": "normalize-space(.//*[contains(text(),'发文日期')]/following-sibling::span)",
        "source": "normalize-space(.//*[contains(text(),'发布机构')]/following-sibling::span)",
        "author": "",
        "navigation": "",
        "content": ".//*[@class='content']//*[not(@type='text/css')]/descendant::text()",
        "editor": "",
        "tags": "normalize-space(.//*[contains(text(),'主 题 词')]/following-sibling::span)",
    },
    {
        "title": "normalize-space(.//*[@class='daohang']/following-sibling::div/div[1])",
        "news_date": "substring(normalize-space(.//*[contains(text(),'来源')]),1,16)",
        "source": "substring-after(normalize-space(.//*[contains(text(),'来源')]),'来源：')",
        "author": "",
        "navigation": "substring-after(normalize-space(.//*[@class='daohang']),'当前的位置：')",
        "content": ".//*[@class='sanji_neirong']/descendant::text()",
        "editor": "",
        "tags": "",
    },
    {
        "title": "normalize-space(.//*[@class='tpbfmain']/h2)",
        "news_date": "normalize-space(.//*[@class='main_t']/span[1])",
        "source": "substring-after(normalize-space(.//*[@class='main_t']/span[2]),'来源：')",
        "author": "",
        "navigation": "substring-after(normalize-space(.//*[contains(text(),'当前位置')]),'位置：')",
        "content": ".//*[@class='zhu_main']/descendant::text()",
        "editor": "translate(substring-after(normalize-space(.//*[contains(text(),'责任编辑')]),'责任编辑：'),')','')",
        "tags": "",
    },
    {
        "title": "normalize-space(.//*[@class='xq_box']/h3)",
        "news_date": "substring(normalize-space(.//*[contains(text(),'来源')]),1,16)",
        "source": "substring-after(normalize-space(.//*[contains(text(),'来源')]),'来源：')",
        "author": "",
        "navigation": "substring-after(normalize-space(.//*[@class='mbx_box']),':')",
        "content": ".//*[@class='TRS_Editor']/descendant::text()",
        "editor": "translate(substring-after(normalize-space(.//*[contains(text(),'责任编辑')]),'责任编辑：'),')','')",
        "tags": "",
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/[\w]*\d*[_]*\d*\.[s]*htm[l]*'

