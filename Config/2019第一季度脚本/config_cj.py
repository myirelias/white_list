# 天下金融网
TASK_NAME = 'cj'

# 起始URL
START_URL = 'http://www.cj.gov.cn/'

# 控制域，必须为list格式
DOMAIN = ['cj']
# 请求头
HEADERS = {
    'Host': 'www.cj.gov.cn',
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
        "title": ".//*[@id='divTitle']/descendant::text()",
        "news_date": "normalize-space(.//*[@class='con_md_hidden']//*[contains(text(),'时间')]/following-sibling::td|.//*[contains(text(),'发文日期')]/following-sibling::td)",
        "source": "normalize-space(.//*[@class='con_md_hidden']//*[contains(text(),'来源')]/following-sibling::td|.//*[contains(text(),'来') and contains(text(),'源')]/following-sibling::td)",
        "author": "",
        "navigation": "substring(normalize-space(.//*[@class='row showpath']),6,200)",
        "content": ".//*[@id='info_content']/descendant::text()|.//*[@class='cent_nr_box']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='zd_contect_t'])",
        "news_date": "substring-after(normalize-space(.//*[@class='zd_contect_info']/span[1]),'日期：')",
        "source": "substring-after(normalize-space(.//*[@class='zd_contect_info']/span[2]),'来源：')",
        "author": "",
        "navigation": "substring-after(normalize-space(.//*[contains(text(),'当前位置')]),'：')",
        "content": ".//*[@class='zd_contect_cont']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='article-title'])",
        "news_date": "normalize-space(.//*[@class='info']/span[1])",
        "source": "substring-after(normalize-space(.//*[@class='info']/span[2]),'来源：')",
        "author": "",
        "navigation": "normalize-space(.//*[@class='am-breadcrumb'])",
        "content": ".//*[@class='am-article-bd']/descendant::p/text()",
        "editor": "substring-after(.//*[contains(text(),'责任编辑')],'：')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='show']/h1)",
        "news_date": "normalize-space(.//*[contains(text(),'时间')]/following-sibling::span[1])",
        "source": "normalize-space(.//*[contains(text(),'来源')]/following-sibling::span[1])",
        "author": "",
        "navigation": "substring-after(normalize-space(.//*[@class='map']),'：')",
        "content": ".//*[@class='show_are']/descendant::p/descendant::text()",
        "editor": "",
        "tags": ""
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d*\.s*html*'

