# 漳州新闻网
TASK_NAME = 'zznews'

# 起始URL
START_URL = 'http://www.zznews.cn/'

# 控制域，必须为list格式
DOMAINS = ['zznews']
# 请求头
HEADERS = {
    'Host': 'www.zznews.cn',
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
        "title": "normalize-space(.//*[@class='n-cont-top']/h1)",
        "news_date": "substring(substring-after(substring-before(normalize-space(.//*[contains(text(),'您当前的位置')]),'来源'),'位置'),8,100)",
        "source": "substring-after(substring-before(normalize-space(.//*[contains(text(),'您当前的位置')]),'编辑'),'来源:')",
        "author": "",
        "navigation": "substring-after(normalize-space(.//*[@class='dqwz']),'：')",
        "content": ".//*[@id='news-content']/descendant::text()",
        "editor": "substring-before(substring-after(normalize-space(.//*[contains(text(),'您当前的位置')]),'编辑:'),'字体')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='nph_set_title']/h1)",
        "news_date": "normalize-space(.//*[@class='nph_set_title']/span[3])",
        "source": "",
        "author": "",
        "navigation": "substring(normalize-space(.//*[contains(@class,'nph_chn')]),10,100)",
        "content": ".//*[@id='photoDesc']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@id='content_title'])",
        "news_date": "substring(normalize-space(.//*[@id='content_source']),1,10)",
        "source": "substring-after(normalize-space(.//*[@id='content_source']),'来源：')",
        "author": "",
        "navigation": "normalize-space(.//*[@id='h_right1'])",
        "content": ".//*[@id='fontzoom']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='newsp-l-biaoti']/h2)",
        "news_date": "substring(normalize-space(.//*[@class='newsp-l-biaoti']/p),1,16)",
        "source": "substring-before(substring-after(normalize-space(.//*[@class='newsp-l-biaoti']/p),'稿源：'),'【')",
        "author": "",
        "navigation": "substring(normalize-space(.//*[@class='newsp-l-daohang']),9,200)",
        "content": ".//*[@class='newsp-l-top']/descendant::text()",
        "editor": "substring-before(substring-after(normalize-space(.//*[contains(text(),'编辑')]),'编辑：'),'【')",
        "tags": ""
    },

]

REGEX_LIST = r'.*'
# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'[/\d*]*\.[s]htm[l]*'

