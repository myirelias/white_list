# 青岛网络广播电台
TASK_NAME = 'qtv'

# 起始URL
START_URL = 'http://www.qtv.com.cn/'

# 控制域，必须为list格式
DOMAIN = ['qtv']
# 请求头
HEADERS = {
    'Host': 'www.qtv.com.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
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
#     "tags": ""
# },
XPATHER_NEWS_LIST = [
    {
        "title": "normalize-space(.//*[@class='content-l']/h1)",
        "news_date": "normalize-space(.//*[@class='news-resource']/span[1])",
        "source": "substring(normalize-space(.//*[contains(text(),'来源')]),4,50)",
        "author": "",
        "navigation": "normalize-space(.//*[@class='position'])",
        "content": ".//*[@class='news-content']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@id='video_title']/h1)",
        "news_date": "normalize-space(.//*[@class='video-date'])",
        "source": "",
        "author": "",
        "navigation": "normalize-space(.//*[@class='position'])",
        "content": ".//*[@class='video-des']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='question-title'])",
        "news_date": "substring(normalize-space(.//*[contains(text(),'来源')]/parent::p),1,18)",
        "source": "substring-after(normalize-space(.//*[contains(text(),'来源')]),'来源：')",
        "author": "",
        "navigation": "",
        "content": ".//*[@class='question-detail-con']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='zwConTitle_z']/h1)",
        "news_date": "substring(normalize-space(.//*[contains(text(),'来源')]/parent::p),1,16)",
        "source": "substring-after(normalize-space(.//*[contains(text(),'来源')]),'来源：')",
        "author": "",
        "navigation": "substring(normalize-space(.//*[@class='now_z']),9,200)",
        "content": ".//*[@class='zwConreally_z']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'[/\d*]*\.[s]htm[l]*'

