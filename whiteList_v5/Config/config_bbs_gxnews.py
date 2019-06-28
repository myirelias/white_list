# 红豆社区-广西
TASK_NAME = 'bbs_gxnews'

# 起始URL
START_URL = 'http://hongdou.gxnews.com.cn'

# 控制域，必须为list格式
DOMAIN = ['hongdou.gxnews']
# 请求头
HEADERS = {
    'Host': 'hongdou.gxnews.com.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
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
        "title": "substring-after(substring-before(normalize-space(//*[contains(@class,'postbit')][1]//*[@class='thead']),'(您是'),'标题:')",
        "news_date": "substring-before(substring-after(normalize-space(//*[contains(@class,'postbit')][1]//*[@width='230']),'发表于'),'第')",
        "source": "",
        "author": "normalize-space(.//*[contains(@class,'postbit')][1]//*[contains(@id,'postmenu')])",
        "navigation": "translate(normalize-space(.//*[contains(text(),'您现在的位置')]),'您现在的位置：:','')",
        "content": "//*[contains(@class,'postbit')][1]//*[@class='viewmessage']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/viewthread-\d*\.s*html*'

# 响应时间
# TIMEOUT = 20


