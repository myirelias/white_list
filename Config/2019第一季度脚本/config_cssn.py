# 中国社会科学网
TASK_NAME = 'cssn'

# 起始URL
START_URL = 'http://www.cssn.cn/'

# 控制域，必须为list格式
DOMAIN = ['cssn']
# 请求头
HEADERS = {
    'Host': 'www.cssn.cn',
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
        "title": "normalize-space(.//*[@class='TitleFont'])",
        "news_date": "substring-before(.//*[contains(text(),'来源')],'来源')",
        "source": "substring-before(substring-after(.//*[contains(text(),'来源')],'来源：'),'作者')",
        "author": "translate(substring-after(.//*[contains(text(),'来源')],'作者：'),'字号','')",
        "navigation": "string(.//*[@class='CurrChnlCls']/parent::span)",
        "content": ".//*[@class='TRS_Editor']/descendant::text()",
        "editor": "translate(substring-after(.//*/span[contains(text(),'责编')],'责编：'),'）','')",
        "tags": "substring-after(.//*/span[contains(text(),'关键词')],'关键词：')"
    },
    {
        "title": "normalize-space(.//*[@class='huang16c'])",
        "news_date": "substring(substring-after(normalize-space(.//*[contains(text(),'发布时间')]),'发布时间：'),1,12)",
        "source": "substring-after(normalize-space(.//*[contains(text(),'来源')]),'来源：')",
        "author": "substring-before(substring-after(normalize-space(.//*[contains(text(),'作者')]),'作者：'),'来源')",
        "navigation": "normalize-space(.//*[contains(text(),'您所在的位置')]/following-sibling::span)",
        "content": ".//*[@class='TRS_Editor']/descendant::p/text()",
        "editor": "",
        "tags": ""
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{6,8}/\w*\d*[_]*\d*\.[s]*htm[l]*'

