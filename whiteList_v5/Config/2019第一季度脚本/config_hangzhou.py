# 杭州网
TASK_NAME = 'hangzhou'

# 起始URL
START_URL = 'http://www.hangzhou.com.cn/'

# 控制域，必须为list格式
DOMAIN = ['hangzhou']
# 请求头
HEADERS = {
    'Host': 'www.hangzhou.com.cn',
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
        "title": "string(.//*[@class='tit'])",
        "news_date": "substring(normalize-space(.//*[contains(text(),'发布时间')]),6,20)",
        "source": "substring-after(substring-before(normalize-space(.//*[contains(text(),'来源')]),'作者'),'：')",
        "author": "substring-after(substring-before(normalize-space(.//*[contains(text(),'来源')]),'编辑'),'作者：')",
        "navigation": "substring(normalize-space(.//*[@class='weizhi']),6,100)",
        "content": ".//*[@class='zhengwen']/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[contains(text(),'来源')]),'编辑：')",
        "tags": ".//*[@name='Keywords']/@content"
    },
    {
        "title": "string(.//*[@class='tittle_18px'])",
        "news_date": "substring(substring-after(normalize-space(.//*[contains(text(),'年') and contains(text(),'月') and contains(text(),'日')]),' '),1,20)",
        "source": "substring(substring-after(normalize-space(.//*[contains(text(),'年') and contains(text(),'月') and contains(text(),'日')]),' '),26,100)",
        "author": "substring-before(substring-after(.//*[contains(text(),'作者')],'作者：'),'编辑')",
        "navigation": "string(.//body//*[contains(text(),'杭州楼市')]//parent::div)",
        "content": ".//article/descendant::text()",
        "editor": "substring-after(.//*[contains(text(),'作者')],'编辑：')",
        "tags": ".//*[@name='Keywords']/@content"
    },
    {
        "title": "string(.//*[@class='bcolor02'])",
        "news_date": ".//*[@name='publishdate']/@content",
        "source": "substring-before(substring-after(normalize-space(.//*[contains(text(),'来源')]),'来源：'),'作者')",
        "author": "substring-before(substring-after(normalize-space(.//*[contains(text(),'来源')]),'作者：'),'编辑')",
        "navigation": "string(.//*[@class='white'])",
        "content": ".//*[@class='wz14']/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[contains(text(),'来源')]),'编辑：')",
        "tags": ".//*[@name='Keywords']/@content"
    },
    {
        "title": "string(.//*[contains(@class,'wname01')])",
        "news_date": ".//*[@name='publishdate']/@content",
        "source": "substring-before(substring-after(normalize-space(.//*[contains(text(),'来源')]),'来源：'),'作者')",
        "author": "substring-before(substring-after(normalize-space(.//*[contains(text(),'来源')]),'作者：'),'编辑')",
        "navigation": "substring(normalize-space(.//*[contains(text(),'您所在的位置')]//parent::td/parent::tr),8,100)",
        "content": ".//*[contains(@class,'wname02')]/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[contains(text(),'来源')]),'编辑：')",
        "tags": ".//*[@name='Keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[contains(@class,'lname05')])",
        "news_date": ".//*[@name='publishdate']/@content",
        "source": "substring-before(substring-after(normalize-space(.//*[contains(text(),'来源')]),'来源：'),'作者')",
        "author": "substring-before(substring-after(normalize-space(.//*[contains(text(),'来源')]),'作者：'),'编辑')",
        "navigation": "substring(normalize-space(.//*[contains(text(),'您所在的位置')]//parent::td/parent::tr),8,100)",
        "content": ".//*[contains(@class,'lname06')]/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[contains(text(),'来源')]),'编辑：')",
        "tags": ".//*[@name='Keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='mdg_title'])",
        "news_date": "normalize-space(.//*[contains(text(),'来源')]/parent::tr/td[2])",
        "source": "substring-after(normalize-space(.//*[contains(text(),'来源')]),'：')",
        "author": "",
        "navigation": "normalize-space(.//*[contains(text(),'当前位置')]/parent::td/following-sibling::td)",
        "content": ".//*[@id='zoom']/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keyword']/@content"
    },
    {
        "title": "normalize-space(html/body/div[2]/div[1]/table[3]/tbody/tr/td/table[1]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td)",
        "news_date": "substring(normalize-space(.//*[contains(text(),'来源')]),1,20)",
        "source": "substring-after(normalize-space(.//*[contains(text(),'来源')]),'来源：')",
        "author": "substring-before(substring-after(normalize-space(.//*[contains(text(),'作者')]),'作者：'),'编辑')",
        "navigation": "normalize-space(html/body/div[2]/div[1]/table[1]/tbody/tr/td[2]/table/tbody/tr/td)",
        "content": ".//*[@class='cont_txt']/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[contains(text(),'编辑')]),'编辑：')",
        "tags": ".//*[@name='Keywords']/@content"
    },
    {
        "title": "normalize-space(html/body/div[2]/div/div[2]/div/div[2]/table/tbody/tr[3]/td)",
        "news_date": "substring(normalize-space(html/body/div[2]/div/div[2]/div/div[2]/table/tbody/tr[4]/td),1,20)",
        "source": "substring-before(substring-after(normalize-space(.//*[contains(text(),'来源')]),'来源：'),'作者')",
        "author": "substring-before(substring-after(normalize-space(.//*[contains(text(),'作者')]),'作者：'),'编辑')",
        "navigation": "normalize-space(.//*[contains(text(),'当前位置')]/following-sibling::span)",
        "content": ".//*[@class='titbox_cont']//*[@class='fontsz14']/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[contains(text(),'编辑')]),'编辑：')",
        "tags": ".//*[@name='Keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'[/]*\d*[-]*\d*[/]*\d*/\w*_\d*\.[s]*htm[l]*'

