# 中国发展网
TASK_NAME = 'chinadevelopment'

# 起始URL
START_URL = 'http://www.chinadevelopment.com.cn/'

# 控制域，必须为list格式
DOMAIN = ['chinadevelopment']
# 请求头
HEADERS = {
    'Host': 'www.chinadevelopment.com.cn',
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
        "title": "normalize-space(.//*[@class='article-content-title'])",
        "news_date": "normalize-space(.//*[contains(@class,'date')])",
        "source": "normalize-space(.//*[contains(@class,'source')])",
        "author": "",
        "navigation": "normalize-space(.//*[@class='column m-crumb'])",
        "content": ".//*[contains(@class,'article-detail')]/descendant::text()",
        "editor": "substring(normalize-space(.//*[contains(text(),'责任编辑')]),6,20)   ",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='con_title'])",
        "news_date": "substring(normalize-space(.//*[@class='con_time']),1,20)",
        "source": "substring(normalize-space(.//*[@class='con_time']),20,200)",
        "author": "",
        "navigation": "substring-after(normalize-space(.//*[contains(text(),'当前位置')]),'当前位置：')",
        "content": ".//*[@class='content article-content']/descendant::text()",
        "editor": "translate(substring-after(normalize-space(.//*[@class='zrbj']),'责编：'),'】','')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='show_box']/h1)",
        "news_date": "normalize-space(.//*[@class='show_box_info']/span[1])",
        "source": "normalize-space(.//*[@class='show_box_info']/span[2])",
        "author": "",
        "navigation": "substring-after(normalize-space(.//*[@class='now']),'当前位置：')",
        "content": ".//*[@class='show_box_m']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//h3)",
        "news_date": "substring(normalize-space(.//*[@class='subtitle']),1,10)",
        "source": "substring(normalize-space(.//*[@class='subtitle']),11,50)",
        "author": "",
        "navigation": "",
        "content": ".//*[@class='article']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='text_title']/h1)",
        "news_date": "substring(normalize-space(.//*[@class='rqly']),1,20)",
        "source": "substring-before(substring-after(normalize-space(.//*[@class='rqly']),'来源：'),'作者')",
        "author": "substring-after(.//*[@id='zuozhe'],'作者：')",
        "navigation": "normalize-space(.//*[@class='dqwz'])",
        "content": ".//*[@class='box_con']/descendant::text()",
        "editor": "translate(substring-after(.//*[@class='edit'],'责任编辑：'),']','')",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{4,6}/\d*/\d*\.[s]*htm[l]*'

