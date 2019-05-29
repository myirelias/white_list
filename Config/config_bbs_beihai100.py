# 北海100
TASK_NAME = 'bbs_beihai100'

# 起始URL
START_URL = 'http://www.beihai100.cn/index.php?m=bbs'

# 控制域，必须为list格式
DOMAIN = ['beihai100']
# 请求头
HEADERS = {
    'Host': 'www.beihai100.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://www.beihai100.cn/?_360safeparam=90524140',
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
        "title": "normalize-space(.//*[@id='subject_tpc'])",
        "news_date": ".//*[@id='readfloor_tpc']//*[contains(text(),'发表于')]/@title",
        "source": "",
        "author": "normalize-space(.//*[@id='readfloor_tpc']//*[contains(@class,'readName b')]/a)",
        "navigation": "normalize-space(.//*[@id='breadCrumb']//*[contains(text(),'首页')]/parent::div)",
        "content": ".//*[@id='readfloor_tpc']//*[@id='read_tpc']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/read-htm-tid-\d*\.s*html*'

# 响应时间
# TIMEOUT = 20


