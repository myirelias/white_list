# 中国文明网
TASK_NAME = 'wenming'

# 起始URL
START_URL = 'http://www.wenming.cn/'

# 控制域，必须为list格式
DOMAIN = ['wenming']
# 请求头
HEADERS = {
    'Host': 'www.wenming.cn',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
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
        "title": ".//*[starts-with(@id,'title')]/text()",
        "news_date": "substring-before(substring-after((.//*[@id='time_tex']),'发表时间：'),'来源')",
        "source": "substring-after((.//*[@id='time_tex']),'来源：')",
        "author": "",
        "navigation": "string(.//*[@class='title'])",
        "content": ".//*[@class='TRS_Editor']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": ".//*[@class='tt-tit']/text()",
        "news_date": "substring-after(.//*[contains(text(),'日期')],'日期：')",
        "source": "substring-after(.//*[contains(text(),'来源')],'来源：')",
        "author": "substring-after(.//*[contains(text(),'作者')],'作者：')",
        "navigation": "string(.//*[@class='pl-l'])",
        "content": ".//*[@class='TRS_Editor']/descendant::text()",
        "editor": "substring-after(.//*[contains(text(),'责任编辑')],'编辑：')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": ".//*[@class='dc-title']/text()",
        "news_date": ".//*[@class='dc-title02']/text()",
        "source": "substring-before(substring-after(.//*[contains(text(),'来源')],'来源：'),'责任编辑')",
        "author": "",
        "navigation": "",
        "content": ".//*[@class='TRS_Editor']/descendant::p/descendant::text()",
        "editor": "substring-after(.//*[contains(text(),'责任编辑')],'责任编辑：')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": ".//*[@class='bqjj-tit']/text()",
        "news_date": ".//*[@class='bqjj-qs']/text()",
        "source": "",
        "author": "",
        "navigation": "",
        "content": ".//*[@class='TRS_Editor']/descendant::p/descendant::text()",
        "editor": "substring-after(.//*[contains(text(),'责任编辑')],'责任编辑：')",
        "tags": ".//*[@name='keywords']/@content"
    },
{
        "title": "string(.//*/h2)",
        "news_date": "",
        "source": "",
        "author": "",
        "navigation": "",
        "content": ".//*[@class='news']/descendant::text()",
        "editor": "substring-after(.//*[contains(text(),'责任编辑')],'责任编辑：')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "string(.//*[@id='title_tex'])",
        "news_date": "substring-before(substring-after(.//*[@id='time_tex'],'发表时间：'),'来源')",
        "source": "substring-after(.//*[@id='time_tex'],'来源：')",
        "author": "",
        "navigation": "string(.//*[@class='title'])",
        "content": ".//*[@class='TRS_Editor']/descendant::text()",
        "editor": "substring-after(.//*[@class='editor_tex'],'责任编辑：')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "string(.//*[@class='tt-tit'])",
        "news_date": "substring-after(.//*[@class='tt-rq'],'：')",
        "source": "substring-after(.//*[@class='tt-ly'],'：')",
        "author": "",
        "navigation": "string(.//*[@class='pl-l'])",
        "content": ".//*[@class='TRS_Editor']/descendant::text()",
        "editor": "substring-after(.//*[@class='main-editor'],'：')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": ".//*[@class='ad460']/descendant::text()",
        "news_date": "",
        "source": "substring-after(.//*[@class='laiyuan'],'：')",
        "author": "",
        "navigation": "",
        "content": ".//*[@class='TRS_Editor']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='main_l']/h1)",
        "news_date": ".//*[@name='publishdate']/@content",
        "source": "substring-before(substring-after(normalize-space(.//*[contains(text(),'稿件来源')]),'稿件来源：'),'责任编辑')",
        "author": "",
        "navigation": "substring(normalize-space(.//*[contains(text(),'当前位置')]/parent::div),7,200)",
        "content": ".//*[@id='zoom']/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[contains(text(),'责任编辑')]),'责任编辑：')",
        "tags": ".//*[@name='keywords']/@content",
    },
    {
        "title": "normalize-space(.//*[@class='detailboxspan'])",
        "news_date": "substring(substring-after(normalize-space(.//*[contains(text(),'发布时间')]),'发布时间：'),1,10)",
        "source": "substring-before(substring-after(normalize-space(.//*[contains(text(),'来源')]),'来源：'),'发布时间')",
        "author": "",
        "navigation": "normalize-space(.//*[@class='local'])",
        "content": ".//*[@class='TRS_Editor']/descendant::text()",
        "editor": "substring-before(substring-after(normalize-space(.//*[contains(text(),'编辑')]),'编辑：'),'【')",
        "tags": ".//*[@name='keywords']/@content",
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{6,8}/\w*\d+_\d+\.[s]*htm[l]*'
