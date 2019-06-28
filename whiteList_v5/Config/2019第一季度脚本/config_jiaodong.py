# 胶东在线
TASK_NAME = 'jiaodong'

# 起始URL
START_URL = 'http://www.jiaodong.net/'

# 控制域，必须为list格式
DOMAIN = ['jiaodong']
# 请求头
HEADERS = {
    'Host': 'www.jiaodong.net',
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
        "title": "normalize-space(.//*/h1)",
        "news_date": "substring-after(substring-before(normalize-space(.//*[contains(@class,'source f14')]),'A'),'来源：')",
        "source": "substring-after(substring-before(normalize-space(.//*[contains(@class,'source f14')]),'A'),'来源：')",
        "author": "",
        "navigation": "substring(normalize-space(.//*[@class='syshide']),9,200)",
        "content": ".//*[@id='content']/descendant::text()",
        "editor": "translate(substring-after(.//*[contains(text(),'责任编辑')],'责任编辑：'),']','')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='heiti20'])",
        "news_date": "substring-after(substring-before(normalize-space(.//*[contains(text(),'来源')]),'来源'),' ')",
        "source": "substring-before(substring-after(normalize-space(.//*[contains(text(),'来源')]),'来源：'),'【')",
        "author": "",
        "navigation": "substring(normalize-space(.//a[contains(text(),'胶东在线')]/parent::td),9,200)",
        "content": ".//*[@class='newscontent']/descendant::text()",
        "editor": "substring-before(substring-after(normalize-space(.//*[contains(text(),'责任编辑')]),'责任编辑：'),'】')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='heiti18gray'])",
        "news_date": "normalize-space(html/body/table[5]/tbody/tr/td[1]/table[4]/tbody/tr[2]/td)",
        "source": "",
        "author": "",
        "navigation": "substring-after(normalize-space(html/body/table[5]/tbody/tr/td[1]/table[2]/tbody/tr[1]/td[2]),'：')",
        "content": "normalize-space(html/body/table[5]/tbody/tr/td[1]/table[4]/tbody/tr[5])",
        "editor": "substring-after(normalize-space(.//*[contains(text(),'责任编辑')]),'责任编辑：')",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{4}/\d{2}/\d{2}/\d*\.[s]*htm[l]*'

