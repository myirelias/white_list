# 合肥热线
TASK_NAME = 'hefei'

# 起始URL
START_URL = 'http://www.hefei.cc/'

# 控制域，必须为list格式
DOMAIN = ['hefei']
# 请求头
HEADERS = {
    'Host': 'www.hefei.cc',
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
        "title": "normalize-space(.//*[@class='list_main_content']/h1)",
        "news_date": "normalize-space(.//*[@class='content_line']/span[1])",
        "source": "substring-after(.//*[@class='content_line']//*[contains(text(),'来源')],'来源：')",
        "author": "",
        "navigation": "substring-after(normalize-space(.//*[@class='p_l']),'当前位置：')",
        "content": ".//*[@id='weiboshare']//*[not(@type='text/javascript')]/descendant::text()",
        "editor": "substring-after(.//*[contains(text(),'责任编辑')],'责任编辑：')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='web_xx_l']/h1)",
        "news_date": "substring(normalize-space(.//*[contains(text(),'来源')]),1,12)",
        "source": "substring-before(substring-after(normalize-space(.//*[contains(text(),'来源')]),'来源：'),'浏览次数')",
        "author": "",
        "navigation": "substring-after(normalize-space(.//*[@class='p_l']),'当前位置：')",
        "content": ".//*[@class='web_xx_box']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='titel'])",
        "news_date": "",
        "source": "",
        "author": "",
        "navigation": "substring-after(normalize-space(.//*[@class='this_p']),'当前位置：')",
        "content": ".//*[@class='intro']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='KEYWords']/@content"
    },
    {
        "title": "normalize-space(.//*[@id='content']/h2)",
        "news_date": "substring(normalize-space(.//*[contains(text(),'来源')]),1,12)",
        "source": "substring-before(substring-after(normalize-space(.//*[contains(text(),'来源')]),'来源：'),'浏览')",
        "author": "",
        "navigation": "substring-after(normalize-space(.//*[@class='page_nav']),'：')",
        "content": ".//*[@id='news_subject']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{4}/\d{4}/\d*\.[s]*htm[l]*'

