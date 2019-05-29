# 盛世收藏
TASK_NAME = 'sssc'

# 起始URL
START_URL = 'http://www.sssc.cn/'

# 控制域，必须为list格式
DOMAIN = ['sssc']
# 请求头
HEADERS = {
    'Host': 'api.sssc.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://www.sssc.cn/a/20181226/1545791755170810.shtml',
    'Cookie': 'UM_distinctid=168542f82287e-0f9e114260705b8-4c322a79-1fa400-168542f82291b4; Hm_lvt_e31a70b5db2120503a19890f736162d4=1547600627; Hm_lpvt_e31a70b5db2120503a19890f736162d4=1547600627; _ga=GA1.2.142421905.1547600629; _gid=GA1.2.1323685538.1547600629',
    'Connection': 'keep-alive',
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
        "title": "string(.//*[contains(@class,'text_cont_l_tit')])",
        "news_date": "substring-before(.//*[@class='origin'],'作者')",
        "source": "",
        "author": "substring-after(.//*[@class='origin'],'作者:')",
        "navigation": "string(.//*[@class='nav_lef'])",
        "content": ".//*[@class='text_cont_l_wenmain']/descendant::text()",
        "editor": "",
        "tags": ".//*/head/title/text()"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{6,8}/\d*\.[s]*htm[l]*'

