# 中山新闻网
TASK_NAME = 'zsnews'

# 起始URL
START_URL = 'http://www.zsnews.cn/'

# 控制域，必须为list格式
DOMAIN = ['zsnews']
# 请求头
HEADERS = {
    'Host': 'www.zsnews.cn',
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
        "title": "normalize-space(.//*[contains(@class,'article-title')])",
        "news_date": "substring(.//*[contains(text(),'发布时间')],6,50)",
        "source": "substring(.//*[contains(text(),'来源')],4,50)",
        "author": "substring(.//*[contains(text(),'作者')],4,50)",
        "navigation": "normalize-space(.//*[@class='tree-nav-large'])",
        "content": ".//*[@class='article-content']/descendant::text()",
        "editor": "substring(.//*[contains(text(),'责任编辑')],6,50)",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "html/body/center/table/tbody/tr/td/table[2]/tbody/tr[2]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[1]/td/div/span/descendant::text()",
        "news_date": "substring(substring-before(normalize-space(.//*[contains(text(),'发布日期')]),'作者'),6,50)",
        "source": "substring-after(normalize-space(.//*[contains(text(),'来源于')]),'来源于：')",
        "author": "substring-after(substring-before(normalize-space(.//*[contains(text(),'发布日期')]),'责任编辑'),'作者：')",
        "navigation": "substring-after(normalize-space(.//*[contains(text(),'现在位置')]),'现在位置：')",
        "content": ".//*[@class='j-content']/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[contains(text(),'发布日期')]),'责任编辑：')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@class='title'])",
        "news_date": "substring-after(normalize-space(.//*[contains(text(),'来源')]),'发布日期：')",
        "source": "substring-before(substring-after(normalize-space(.//*[contains(text(),'来源')]),'来源：'),'发布')",
        "author": "substring-after(normalize-space(.//*[contains(text(),'作者')]),'作者：')",
        "navigation": "normalize-space(.//*[contains(@class,'lanmuPlace')]//a[contains(text(),'首页')]/parent::td)",
        "content": ".//*[@class='content']/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[contains(text(),'责任编辑')]),'责任编辑：')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(html/body/table[2]/tbody/tr/td[2]/table[2]/tbody/tr[2]/td/table/tbody/tr[1]/td/div/span[2]/b)",
        "news_date": "substring(substring-after(normalize-space(.//*[contains(text(),'发布日期')]),'发布日期：'),1,11)",
        "source": "substring-after(normalize-space(.//*[contains(text(),'来源于')]),'来源于：')",
        "author": "substring-after(normalize-space(.//*[contains(text(),'发布日期')]),'记者')",
        "navigation": "substring-after(normalize-space(.//*[contains(text(),'现在位置')]/parent::div),'位置：')",
        "content": "html/body/table[2]/tbody/tr/td[2]/table[2]/tbody/tr[2]/td/table/tbody/tr[3]/td/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },

]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d*\.[s]*htm[l]*'

