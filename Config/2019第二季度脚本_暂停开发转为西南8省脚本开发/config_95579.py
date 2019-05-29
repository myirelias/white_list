# 长江证券
TASK_NAME = '95579'

# 起始URL
START_URL = 'https://www.95579.com/main/financeinfo/index.html'

# 控制域，必须为list格式
DOMAIN = ['95579']
# 请求头
HEADERS = {
    'Host': 'www.95579.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.95579.com/',
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
        "title": "normalize-space(.//*[@class='wyh'])",
        "news_date": "substring(substring-before(normalize-space(.//*[@class='art_fu_title']),'来源'),3,50)",
        "source": "substring-before(substring-after(normalize-space(.//*[@class='art_fu_title']),'来源：'),'订阅')",
        "author": "",
        "navigation": "substring-after(normalize-space(.//*[@class='per_path']),'位置：')",
        "content": ".//*[@class='art_content']/descendant::text()",
        "editor": "",
        "tags": ""
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/a/\d{6,8}/\d*\.s*html*'

