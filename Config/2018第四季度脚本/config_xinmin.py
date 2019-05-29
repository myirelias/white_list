# 新民网
TASK_NAME = 'xinmin'

# 起始URL
START_URL = 'http://www.xinmin.cn/'

# 控制域，必须为list格式
DOMAIN = ['xinmin']
# 请求头
HEADERS = {
    'Host': 'www.xinmin.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'https://www.sogou.com/link?url=DSOYnZeCC_r-rWSaN-SCAIgeOEv2eQM5',
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
#     "tags": "",
# },
XPATHER_NEWS_LIST = [
    {
        "title": ".//*[@class='a_title']/text()",
        "news_date": ".//*[contains(text(),'编辑')]/following-sibling::span[1]/text()",
        "source": "substring-after(.//*[contains(text(),'来源')],'来源：')",
        "author": "substring-after(.//*[contains(text(),'作者')],'作者：')",
        "navigation": "substring-after(.//*[@class='Mbx'],'位置：')",
        "content": ".//*[@class='a_content']/descendant::p/text()",
        "editor": "substring-after(.//*[contains(text(),'编辑')],'编辑：')",
        "tags": ".//*[@name='keywords']/@content",
    },
    {
        "title": "normalize-space(.//*[@class='article_title'])",
        "news_date": "normalize-space(.//*[@class='info']/span[4])",
        "source": "substring-after(normalize-space(.//*[contains(text(),'来源')]),'来源：')",
        "author": "",
        "navigation": "substring-after(normalize-space(.//*[contains(text(),'您现在的位置')]),'您现在的位置：')",
        "content": ".//*[@class='a_p']/descendant::p/text()",
        "editor": "normalize-space(.//*[contains(text(),'编辑')]/following-sibling::span)",
        "tags": ".//*[@name='keywords']/@content",
    },
    {
        "title": "normalize-space(.//*[@class='MP_title'])",
        "news_date": "normalize-space(.//*[@class='MP_datetime'])",
        "source": "substring-before(substring-after(normalize-space(.//*[@class='MP_info']),'来源：'),'新民网编辑')",
        "author": "",
        "navigation": "substring-after(normalize-space(.//*[contains(text(),'现在的位置')]),'您现在的位置：')",
        "content": ".//*[@class='MP_article']/descendant::p/text()",
        "editor": "translate(substring-after(normalize-space(.//*[@class='MP_editor']),'编辑：'),'）','')",
        "tags": ".//*[@name='keywords']/@content",
    },
    {
        "title": "normalize-space(.//*[@class='content_title'])",
        "news_date": "normalize-space(.//*[@class='page_time'])",
        "source": "normalize-space(.//*[@class='page_from'])",
        "author": "",
        "navigation": "",
        "content": ".//*[@class='content_article']/descendant::p/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content",
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{4}/\d{2}/\d{2}/\d+\.[s]*htm[l]*'



