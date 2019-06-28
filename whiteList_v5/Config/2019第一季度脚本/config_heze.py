# 菏泽网
TASK_NAME = 'heze'

# 起始URL
START_URL = 'http://www.heze.cn/'

# 控制域，必须为list格式
DOMAIN = ['heze']
# 请求头
HEADERS = {
    'Host': 'www.heze.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://www.heze.cn/news/news.htm',
    'Cookie': '_gscu_733456985=47517419j0lu4y80; _gscs_733456985=47517419shtm5k80|pv:1; _gscbrs_733456985=1; Hm_lvt_78eff4799d6f55845db7daab3e04d4bd=1547517419; Hm_lpvt_78eff4799d6f55845db7daab3e04d4bd=1547517419',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
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
        "title": ".//*[@class='titleArea']/h1/text()",
        "news_date": "substring-before(.//*[@class='laiYuanArea'],'来源')",
        "source": "substring-after(.//*[@class='laiYuanArea'],'来源:')",
        "author": "",
        "navigation": "substring-after(.//*[@class='navlist'],'位置：')",
        "content": ".//*[@class='neiRongArea']/descendant::text()",
        "editor": "substring-after(.//*[contains(text(),'责任编辑')],'责任编辑')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='cont-h'])",
        "news_date": "substring(normalize-space(.//*[contains(text(),'来源')]/parent::div),1,10)",
        "source": "substring-after(normalize-space(.//*[contains(text(),'来源')]/parent::div),'来源：')",
        "author": "substring-after(normalize-space(.//*[contains(text(),'责任编辑')]/parent::p),'作者：')",
        "navigation": "normalize-space(.//*[contains(@class,'location')])",
        "content": ".//*[@class='content']/descendant::text()",
        "editor": "substring-before(substring-after(normalize-space(.//*[contains(text(),'责任编辑')]/parent::p),'责任编辑：'),'作者')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//td[@class='bigText'])",
        "news_date": "substring(normalize-space(.//*[contains(text(),'来源')]),1,20)",
        "source": "substring-before(substring-after(normalize-space(.//*[contains(text(),'来源')]),'来源:'),'记者')",
        "author": "substring-before(substring-after(normalize-space(.//*[contains(text(),'来源')]),'记者：'),'字体大小')",
        "navigation": "substring-after(normalize-space(.//*[contains(text(),'您现在的位置')]/parent::td),'：')",
        "content": ".//*[@id='zoom']/descendant::text()",
        "editor": "",
        "tags": ""
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{0,4}[-]*\d{0,2}/\d*/\w*_\d*\.[s]*htm[l]*'

