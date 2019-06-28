# 南阳网
TASK_NAME = '01ny'

# 起始URL
START_URL = 'http://www.01ny.cn/'

# 控制域，必须为list格式
DOMAIN = ['01ny']
# 请求头
HEADERS = {
    'Host': 'www.01ny.cn',
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
        "title": "string(.//*[@class='contentbq']//*/h1)",
        "news_date": "substring(.//*[@class='contentbq']//*/h1/following-sibling::p,1,20)",
        "source": "substring-after(.//*[@class='contentbq']//*/h1/following-sibling::p,'来自:')   ",
        "author": "substring-after(.//*[@class='contentbq']//*/h1/following-sibling::p,'来自:')",
        "navigation": "string(.//*[@class='locLeft'])",
        "content": ".//*[@class='textContentbq']/descendant::text()",
        "editor": "substring(.//*[contains(text(),'责任编辑')],7,15)",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "string(.//*[@id='title'])",
        "news_date": "substring(.//*[@class='laiyuan'],1,11)",
        "source": "substring-after(.//*[@class='laiyuan'],'来源')",
        "author": "",
        "navigation": "substring(normalize-space(.//*[@class='l mt5']),2,20)",
        "content": ".//*[@class='con']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "substring-before(.//*/h1,'作者')",
        "news_date": "substring(.//*[contains(text(),'作者')],1,20)",
        "source": "translate(substring-after(.//*[contains(text(),'来源')],'来源：'),'点击：','')",
        "author": "substring-before(substring-after(.//*[contains(text(),'作者')],'作者：'),'来源')",
        "navigation": "string(.//*[@class='crumbs'])",
        "content": ".//*[@class='content']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "string(.//*[@id='page-body']/h2)",
        "news_date": "substring-after(.//*[@class='author'],'留言时间：')",
        "source": "",
        "author": "substring-before(substring-after(.//*[@class='author'],'网友：'),'留言时间')",
        "navigation": "translate(string(.//*[@class='linklist navlinks']),'打印预览','')",
        "content": ".//*[@class='content']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "string(.//*[@class='content']/h1)",
        "news_date": "",
        "source": "",
        "author": "",
        "navigation": "",
        "content": ".//*[@class='content']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "string(.//*[@class='cjf24 cjfw'])",
        "news_date": "substring(normalize-space(.//*[@class='cjbkxd']),1,20)",
        "source": "substring-after(normalize-space(.//*[@class='cjbkxd']),'cn')",
        "author": "",
        "navigation": "substring(.//*[contains(text(),'您所在的位置')],9,50)",
        "content": ".//*[@class='cjxwnerc']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "string(.//*[@id='jsxw_sp_Con0']//*/h1)",
        "news_date": "substring(normalize-space(.//*[@id='jsxw_sp_Con0']//*/h1/following-sibling::p),1,20)",
        "source": "substring-after(normalize-space(.//*[@id='jsxw_sp_Con0']//*/h1/following-sibling::p),'来自:')",
        "author": "substring-before(substring-after(normalize-space(.//*[@id='jsxw_sp_Con0']//*/h1/following-sibling::p),'作者'),'|')",
        "navigation": "string(.//*[@class='tab-list'])",
        "content": ".//*[@class='textContentbq']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@id='Article']/h1)",
        "news_date": "substring(substring-after(normalize-space(.//*[contains(text(),'作者')]),' '),1,22)",
        "source": "substring-after(normalize-space(.//*[contains(text(),'来源')]),'来源：')",
        "author": "substring-before(substring-after(.//*[contains(text(),'作者')],'作者：'),' ')",
        "navigation": "normalize-space(.//*[@class='crumbs'])",
        "content": ".//*[@class='content']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='leftbq']/descendant::h1)",
        "news_date": "substring-before(normalize-space(.//*[@class='leftbq']/div[1]/p),'|')",
        "source": "substring-after(normalize-space(.//*[@class='leftbq']/div[1]/p),'来自:')",
        "author": "substring-before(substring-after(normalize-space(.//*[@class='leftbq']/div[1]/p),'作者:'),'|')",
        "navigation": "normalize-space(.//*[@class='locLeft'])",
        "content": ".//*[@class='textContentbq']/descendant::text()",
        "editor": "translate(substring-after(.//*[contains(text(),'责任编辑')],'：'),']','')",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d*/\w*[_]*\d*/[\d*\w*]*\.[s]*htm[l]*|index.php.*?id=\d*|viewtopic\.[s]*htm[l]*'

