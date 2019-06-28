# 中公教育
TASK_NAME = 'offcn'

# 起始URL
START_URL = 'http://www.offcn.com/'

# 控制域，必须为list格式
DOMAIN = ['offcn']
# 请求头
HEADERS = {
    'Host': 'www.offcn.com',
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
        "title": "normalize-space(.//*[@class='zg_xwzxtit'])",
        "news_date": "substring-before(normalize-space(.//*[@class='zg_xwzxtime']),'|')",
        "source": "substring-after(normalize-space(.//*[@class='zg_xwzxtime']),'来源：')",
        "author": "",
        "navigation": "normalize-space(.//*[@class='fl zg_xwzx_showdivfl'])",
        "content": ".//*[@class='zg_xwzxconshow']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='contentleft2']/h1)",
        "news_date": "substring-before(normalize-space(.//*[contains(text(),'来源')]/parent::h2),'|')",
        "source": "substring-after(normalize-space(.//*[contains(text(),'来源')]/parent::h2),'来源：')",
        "author": "",
        "navigation": "substring-after(.//*[@class='zgmbx_nav'],'您现在的位置：')",
        "content": ".//*[@class='contentleft2']/descendant::p/text()",
        "editor": "translate(substring-after(normalize-space(.//*[contains(text(),'责任编辑')]),'责任编辑：'),')','')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='zgsz_slt']/h1)",
        "news_date": "substring-before(normalize-space(.//*[contains(text(),'来源：')]),'|')",
        "source": "substring-after(normalize-space(.//*[contains(text(),'来源：')]),'来源：')",
        "author": "",
        "navigation": "substring-after(.//*[@class='zgmbx_nav'],'您现在的位置：')",
        "content": ".//*[starts-with(@class,'zgsz_sContent')]/descendant::text()",
        "editor": "translate(substring-after(normalize-space(.//*[contains(text(),'责任编辑')]),'责任编辑：'),'）','')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='zg_contentbox']/h1)",
        "news_date": "substring(normalize-space(.//*[@class='zg_timer']),1,20)",
        "source": "substring-before(substring-after(normalize-space(.//*[@class='zg_timer']),'来源：'),' ')",
        "author": "",
        "navigation": ".//*[@class='zg_weizhi_box']/a/text()",
        "content": ".//*[@class='zg_articlecon']/descendant::text()",
        "editor": "translate(substring-after(.//*[contains(text(),'责任编辑')],'责任编辑：'),')','')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[contains(@class,'nry_left')]/h2)",
        "news_date": "normalize-space(.//*[@class='zg_time']/em)",
        "source": "substring-after(normalize-space(.//*[@class='zg_time']//*[contains(text(),'来源')]),'来源：')",
        "author": "",
        "navigation": ".//*[contains(@class,'zg_weizhi')]/descendant::a/text()",
        "content": ".//*[@class='nry_content']/descendant::text()",
        "editor": "translate(substring-after(.//*[contains(text(),'责任编辑')],'责任编辑：'),')','')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='zg_Htitle'])",
        "news_date": "normalize-space(.//*[@class='zg_time']/em)",
        "source": "substring-after(normalize-space(.//*[@class='zg_time']),'来源：')",
        "author": "",
        "navigation": ".//*[@class='zgmbx_nav']/descendant::a/text()",
        "content": ".//*[@class='zg_articlecon']/descendant::text()",
        "editor": "translate(substring-after(.//*[contains(text(),'责任编辑')],'责任编辑：'),')','')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[contains(@class,'zgky_listmain_left')]/h1)",
        "news_date": "substring-before(normalize-space(.//*[contains(@class,'zgky_listmain_left_titme')]),'|')",
        "source": "substring-after(normalize-space(.//*[contains(@class,'zgky_listmain_left_titme')]),'|')",
        "author": "",
        "navigation": "normalize-space(.//*[contains(@class,'zgky_weizhi_left')])",
        "content": ".//*[@class='zgky_listmain_left_cont']/descendant::text()",
        "editor": "translate(substring-after(.//*[contains(text(),'责任编辑')],'责任编辑：'),')','')",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{4}/\d{4}/\d*\.[s]*htm[l]*'

