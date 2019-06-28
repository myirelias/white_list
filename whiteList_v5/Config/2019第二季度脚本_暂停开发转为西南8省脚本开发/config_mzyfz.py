# 民主与法制网
TASK_NAME = 'mzyfz'

# 起始URL
START_URL = 'http://www.mzyfz.com'

# 控制域，必须为list格式
DOMAIN = ['mzyfz']
# 请求头
HEADERS = {
    'Host': 'www.mzyfz.com',
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
        "title": "normalize-space(.//*[@class='lt1'])",
        "news_date": "substring(normalize-space(.//*[contains(text(),'来源')]),1,20)",
        "source": "substring-after(normalize-space(.//*[contains(text(),'来源')]),'来源：')",
        "author": "",
        "navigation": "translate(substring-after(normalize-space(.//*[contains(@class,'navline')]),'当前位置'),':：','')",
        "content": ".//*[@id='maincontent']/descendant::text()",
        "editor": "translate(substring-after(normalize-space(.//*[contains(text(),'责任编辑')]),'编辑'),':：','')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='a_title'])",
        "news_date": "substring(substring-after(normalize-space(.//*[contains(@class,'a_info')]),'时间：'),1,12)",
        "source": "substring-before(substring-after(normalize-space(.//*[contains(@class,'a_info')]),'作者：'),'时间')",
        "author": "",
        "navigation": "",
        "content": ".//*[@class='a_content']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{4}-\d{2}-\d{2}/content-\d*\.s*html*|/paper/paper[_\d]*\.s*html*'

