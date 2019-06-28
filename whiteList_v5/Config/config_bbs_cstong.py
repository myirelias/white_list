# 长沙通
TASK_NAME = 'bbs_cstong'

# 起始URL
START_URL = 'http://www.cstong.net/'

# 控制域，必须为list格式
DOMAIN = ['cstong']
# 请求头
HEADERS = {
    'Host': 'www.cstong.net',
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
        "title": "normalize-space(.//*[@id='J_post_title'])",
        "news_date": "substring-before(normalize-space(.//*[@class='lz_namebar']//*[@class='fr']),'楼主')",
        "source": "",
        "author": "normalize-space(.//*[@class='lz_namebar']//*[contains(@class,'username')])",
        "navigation": "",
        "content": ".//*[@id='J_posts_list']//*[contains(@id,'read_') and contains(@class,'floor')][1]//*[@class='editor_content']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/read-htm-tid-\d*\.s*html*'

# 响应时间
# TIMEOUT = 20


