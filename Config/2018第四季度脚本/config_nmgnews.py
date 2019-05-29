# 内蒙古新闻网
TASK_NAME = 'nmgnews'

# 起始URL',
START_URL = 'http://www.nmgnews.com.cn/'

# 控制域，必须为list格式
DOMAIN = ['nmgnews']
# 请求头
HEADERS = {
    'Host': 'www.nmgnews.com.cn',
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
        "title": ".//*[@class='black24']/text()",
        "news_date": ".//*[@id='div3']/span[1]/text()",
        "source": "substring-after(.//*[@id='div3']//*[contains(text(),'来源')],'来源：')",
        "author": "",
        "navigation": "substring-after(.//*/ul[@class='black12'],'位置 ：')",
        "content": ".//*[@id='div_content']/descendant::text()",
        "editor": "substring-before(substring-after(.//*[contains(text(),'编辑')],'编辑:'),']')",
        "tags": ".//*[@name='keywords']/@content",
    },
    {
        "title": ".//*[@class='STYLE5']/text()",
        "news_date": ".//*[@align='center']/font[1]/descendant::text()",
        "source": ".//*[@class='STYLE11']/text()",
        "author": "",
        "navigation": "substring-after(.//*[@class='STYLE11 STYLE14'],'位置 ：')",
        "content": ".//*[@id='pzoom']/descendant::text()",
        "editor": "substring-before(substring-after(.//*[contains(text(),'编辑')],'编辑'),']')",
        "tags": ".//*[@name='keywords']/@content",
    },
    {
        "title": "normalize-space(.//*[@class='black24_b'])",
        "news_date": "substring(substring-after(normalize-space(.//*[contains(text(),'来源')]/parent::td),' '),1,20)",
        "source": "substring-after(normalize-space(.//*[contains(text(),'来源')]/parent::td),'来源:')",
        "author": "",
        "navigation": "",
        "content": ".//*[@id='pzoom']/descendant::text()",
        "editor": "translate(substring(normalize-space(.//*[contains(text(),'责任编辑')]),6,20),']','')",
        "tags": ".//*[@name='keywords']/@content",
    },
    {
        "title": "normalize-space(html/body/table[1]/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td[1]/table[2]/tbody/tr/td/table/tbody/tr/td/div/table[1]/tbody/tr[2]/td)",
        "news_date": "substring(normalize-space(html/body/table[1]/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td[1]/table[2]/tbody/tr/td/table/tbody/tr/td/div/table[2]/tbody/tr[2]/td/div/font),1,18)",
        "source": "substring-before(substring-after(normalize-space(.//*[contains(text(),'稿源')]),'稿源：'),'编辑')",
        "author": "",
        "navigation": "substring-after(normalize-space(html/body/table[1]/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td[1]/table[1]/tbody/tr/td[2]/table/tbody/tr/td),'：')",
        "content": "html/body/table[1]/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td[1]/table[2]/tbody/tr/td/table/tbody/tr/td/div/table[3]/tbody/tr[2]/td/div/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[contains(text(),'稿源')]),'编辑：')",
        "tags": ".//*[@name='keywords']/@content",
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{4}/\d{2}/\d{2}/\d+\.[s]*htm[l]*'
