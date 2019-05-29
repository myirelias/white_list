# 正北方网
TASK_NAME = 'northnews'

# 起始URL
START_URL = 'http://www.northnews.cn/'

# 控制域，必须为list格式
DOMAIN = ['northnews']
# 请求头
HEADERS = {
    'Host': 'www.northnews.cn',
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
        "title": "normalize-space(.//*[@class='l-cont']/h1)",
        "news_date": "normalize-space(.//*[@class='name']/span[3])",
        "source": "substring(normalize-space(.//*[contains(text(),'来源') and @class='at01']),4,50)",
        "author": "substring(normalize-space(.//*[contains(text(),'作者') and @class='at01']),4,50)",
        "navigation": "normalize-space(.//*[@class='senav'])",
        "content": ".//*[@class='zhengwen']/descendant::text()",
        "editor": "substring(normalize-space(.//*[contains(text(),'责任编辑') and @class='at01']),6,50)",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='l-tit']/h1)",
        "news_date": "normalize-space(.//*[@class='l-tit']/p/span[1])",
        "source": "substring-after(normalize-space(.//*[@class='l-tit']/p/span[2]),'来源：')",
        "author": "",
        "navigation": "normalize-space(.//*[@class='crumb'])",
        "content": "normalize-space(.//*[@class='picture-main']//*[@class='summary'])",
        "editor": "substring-after(normalize-space(.//*[@class='l-tit']/p/span[3]),'责任编辑：')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='wz-tit']/h1)",
        "news_date": "normalize-space(.//*[@class='auth']/span[1])",
        "source": "substring-after(normalize-space(.//*[contains(text(),'来源')]),'来源：')",
        "author": "substring-after(normalize-space(.//*[contains(text(),'作者')]),'作者：')",
        "navigation": "normalize-space(.//*[@class='l-pos'])",
        "content": ".//*[@class='zhengwen content']/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[contains(text(),'责任编辑')]),'责任编辑：')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='title']/h3)",
        "news_date": "substring(normalize-space(.//*[@class='author']/p),1,20)",
        "source": "substring-before(substring-after(normalize-space(.//*[@class='author']/p),'来源：'),'编辑')",
        "author": "",
        "navigation": "normalize-space(.//*[@class='position'])",
        "content": ".//*[contains(@class,'txt-content')]/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[@class='author']/p),'编辑：')",
        "tags": ".//*[@name='keywords']/@content"
    },

]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{4,6}/\d{2,4}/\d*\.[s]*htm[l]*'

