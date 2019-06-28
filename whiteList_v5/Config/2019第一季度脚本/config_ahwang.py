# 安徽网
TASK_NAME = 'ahwang'

# 起始URL
START_URL = 'http://www.ahwang.cn/'

# 控制域，必须为list格式
DOMAIN = ['ahwang']
# 请求头
HEADERS = {
    'Host': 'www.ahwang.cn',
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
        "title": "normalize-space(.//*[@class='ina_news_text']/h1)",
        "news_date": "normalize-space(.//*[@class='ina_data'])",
        "source": "substring(normalize-space(.//*[@class='ina_source']),4,50)",
        "author": "substring-before(normalize-space(.//*[@class='ina_author']),'向Ta')",
        "navigation": "substring(normalize-space(.//*[contains(text(),'当前位置：')]),6,200)",
        "content": ".//*[starts-with(@class,'ina_content')]/descendant::text()",
        "editor": "substring(normalize-space(.//*[contains(text(),'责任编辑')]),6,20)",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@id='article']/h1|.//*[starts-with(@class,'article-title')])",
        "news_date": "normalize-space(.//*[@class='date'])",
        "source": "substring(normalize-space(.//*[@class='source']),4,50)",
        "author": "",
        "navigation": "substring(normalize-space(.//*[contains(text(),'您的位置：')]),6,200)",
        "content": ".//*[starts-with(@class,'article-content')]/descendant::text()",
        "editor": "substring(normalize-space(.//*[contains(text(),'责任编辑')]),6,20)",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='video-content-title'])",
        "news_date": "normalize-space(.//*[contains(@class,'date')])",
        "source": "",
        "author": "",
        "navigation": "normalize-space(.//*[contains(@class,'cd-breadcrumb')])",
        "content": ".//*[@class='video-describe']/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[@class='editor']),'编辑：')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='article-main']/h1|.//*[contains(@class,'article-main')]/h1)",
        "news_date": "normalize-space(.//*[@class='release-date']|.//*[@class='date'])",
        "source": "substring-after(normalize-space(.//*[@class='source']|.//*[@class='where']),'来源：')",
        "author": "",
        "navigation": "normalize-space(.//*[contains(@class,'news_path')]|.//*[@class='navlist'])",
        "content": ".//*[contains(@class,'news_txt')]/descendant::text()|.//*[@class='article-content']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    }
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d*/*\d*\.s*html*|/\w*_\d*\.s*html*'

