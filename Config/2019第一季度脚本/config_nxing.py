# 巴中传媒网
TASK_NAME = 'nxing'

# 起始URL
START_URL = 'http://www.nxing.cn/'

# 控制域，必须为list格式
DOMAIN = ['nxing']
# 请求头
HEADERS = {
    'Host': 'www.nxing.cn',
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
        "title": "string(.//*[@class='yc_tit']/h1)",
        "news_date": "normalize-space(.//*[@class='yc_tit']/p/span[1])",
        "source": "normalize-space(.//*[@class='yc_tit']/p/span[2])",
        "author": "",
        "navigation": "normalize-space(.//*[@class='h_nav'])",
        "content": ".//*[@class='yc_con_txt']/descendant::text()",
        "editor": "substring-after(.//*[@class='yc_zb'],'：')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "string(.//*[@class='hd']/h1)",
        "news_date": "string(.//*[@class='a_time'])",
        "source": "substring-after(.//*[@class='a_time' and contains(text(),'来源')],'来源：')",
        "author": "",
        "navigation": "",
        "content": ".//*[@class='entity-content']/descendant::p/text()",
        "editor": "substring-after(.//*[contains(text(),'责任编辑')],'：')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "string(.//*[@class='article-title'])",
        "news_date": "substring(.//*[@class='article-attr'],5,10)",
        "source": "string(.//*[@class='article-source'])",
        "author": "",
        "navigation": "",
        "content": ".//*[@class='article-content']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='entity-title'])",
        "news_date": "normalize-space(.//*[@class='entity-info']/span[1])",
        "source": "substring-after(normalize-space(.//*[contains(text(),'来源')]),'来源:')",
        "author": "",
        "navigation": "normalize-space(.//*[@class='post_crumb'])",
        "content": ".//*[@class='entity-content']/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[@class='ep-editor']),'责任编辑：')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[contains(@class,'album-detail')]/h1)",
        "news_date": "substring(normalize-space(.//*[contains(@class,'album-attr')]),1,20)",
        "source": "",
        "author": "",
        "navigation": ".//*[contains(@class,'album-attr')]/a",
        "content": "normalize-space(.//*[contains(@class,'album-desc')])",
        "editor": "",
        "tags": ""
    },
    {
        "title": "normalize-space(.//*[@class='news_detail_title'])",
        "news_date": "substring-after(normalize-space(.//*[@class='news_detail_info']),'发布时间：')",
        "source": "",
        "author": "",
        "navigation": "substring-after(normalize-space(.//*[contains(text(),'当前位置')]),'当前位置:')",
        "content": ".//*[@class='news_detail_content']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d*\.[s]*htm[l]*'

