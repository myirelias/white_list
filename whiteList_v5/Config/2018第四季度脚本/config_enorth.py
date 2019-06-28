# 北方网
TASK_NAME = 'enorth'

# 起始URL',
START_URL = 'http://www.enorth.com.cn/'

# 控制域，必须为list格式
DOMAIN = ['enorth']
# 请求头
HEADERS = {
    'Host': 'edu.enorth.com.cn',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://edu.enorth.com.cn/',
    'Connection': 'keep-alive'
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
        "title": "substring-before(.//*[@id='title']/div[@class='row'],'扫码')",
        "news_date": ".//*/p[contains(@class,'info')]/span[last()]/text()",
        "source": "substring-after(.//*[contains(text(),'来源')],'来源：')",
        "author": "substring-after(.//*[contains(text(),'作者')],'作者：')",
        "navigation": "substring-after(.//*[@class='brumb'],'位置 ：')",
        "content": ".//*[@class='content']/descendant::text()",
        "editor": "substring-after(.//*[contains(text(),'编辑')],'编辑：')",
        "tags": "",
    },
    {
        "title": "normalize-space(.//*[@class='nph_set_title']/h1)",
        "news_date": "normalize-space(.//*[@class='time_source'])",
        "source": "",
        "author": "",
        "navigation": "substring(normalize-space(.//*[contains(@class,'nph_chn')]),9,200)",
        "content": ".//*[@class='nph_cnt']/descendant::text()",
        "editor": "",
        "tags": "",
    },
]


# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{4}/\d{2}/\d{2}/\d+\.[s]*htm[l]*'

