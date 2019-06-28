# 张家界政府网
TASK_NAME = 'zjj'

# 起始URL
START_URL = 'http://www.zjj.gov.cn/'

# 控制域，必须为list格式
DOMAIN = ['zjj']
# 请求头
HEADERS = {
    'Host': 'www.zjj.gov.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
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
#     "tags": ""
# },
XPATHER_NEWS_LIST = [
    {
        "title": "normalize-space(.//h2)",
        "news_date": "normalize-space(.//*[@class='note']/span[3])",
        "source": "substring-after(normalize-space(.//*[contains(text(),'来源')]),'来源：')",
        "author": "substring-after(normalize-space(.//*[contains(text(),'作者')]),'作者：')",
        "navigation": "substring(normalize-space(.//*[@class='currentPosition']),6,200)",
        "content": ".//*[@class='art']/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[contains(text(),'责任编辑')]),'：')",
        "tags": ".//*[@name='Keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='maincontainer']/div/div[1])",
        "news_date": "normalize-space(.//*[contains(text(),'发布日期')]/parent::td/following-sibling::td)",
        "source": "normalize-space(.//*[contains(text(),'索引号')]/parent::td/following-sibling::td)",
        "author": "",
        "navigation": "substring(normalize-space(.//*[contains(text(),'当前位置')]/parent::p),6,200)",
        "content": ".//*[@class='content']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='Keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{4,8}/\w*\d*\.[s]*htm[l]*'

