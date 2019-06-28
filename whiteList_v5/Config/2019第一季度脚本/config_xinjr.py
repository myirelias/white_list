# 中国新金融网
TASK_NAME = 'xinjr'

# 起始URL
START_URL = 'http://www.xinjr.com/'

# 控制域，必须为list格式
DOMAIN = ['xinjr']
# 请求头
HEADERS = {
    'Host': 'www.xinjr.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Cookie': 'Hm_lvt_17f17df9e026c4ed78486c3276c11c31=1551408543; Hm_lpvt_17f17df9e026c4ed78486c3276c11c31=1551408543',
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
        "title": "normalize-space(.//*[@class='arct'])",
        "news_date": "substring(normalize-space(.//*[contains(text(),'发布时间')]/parent::div),6,50)",
        "source": "substring(normalize-space(.//*[@class='arcWtiter']//*[contains(text(),'来源')]/parent::div),4,50)",
        "author": "substring(normalize-space(.//*[@class='arcWtiter']//*[contains(text(),'作者')]/parent::div),4,50)",
        "navigation": "normalize-space(.//*[@class='webpos'])",
        "content": ".//*[contains(@class,'arcBody')]/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },

]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/[\d-]*/\d*\.s*html*'

