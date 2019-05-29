# 长沙市住房和城乡建设局
TASK_NAME = 'csfdc'

# 起始URL
START_URL = 'http://www.csfdc.gov.cn/'

# 控制域，必须为list格式
DOMAIN = ['csfdc']
# 请求头
HEADERS = {
    'Host': 'www.csfdc.gov.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Cookie': 'Hm_lvt_0c2282487543a957f83761512b02e0b2=1551163693; Hm_lpvt_0c2282487543a957f83761512b02e0b2=1551163693',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0',
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
        "title": "normalize-space(.//*[@class='content1']/h2)",
        "news_date": "substring-before(substring-after(normalize-space(.//*[@class='con1_time']),'发布时间：'),'作者')",
        "source": "substring-after(normalize-space(.//*[@class='con1_time']),'稿件来源：')",
        "author": "substring-before(substring-after(normalize-space(.//*[@class='con1_time']),'作者：'),'稿件来源')",
        "navigation": "substring-after(normalize-space(.//*[@class='site']),'所在的位置：')",
        "content": ".//*[@class='con1_text']//*[not(@type='text/javascript' )]/descendant::text()",
        "editor": "",
        "tags": ""
    },
    {
        "title": "normalize-space(.//*[contains(text(),'主题名称')]/following-sibling::td)",
        "news_date": "normalize-space(.//*[contains(text(),'提交时间')]/following-sibling::td)",
        "source": "",
        "author": "",
        "navigation": "substring-after(normalize-space(.//*[@class='site']),'您当前所在的位置：')",
        "content": ".//*[contains(text(),'信件内容')]/following-sibling::td/descendant::text()",
        "editor": "",
        "tags": ""
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{4,8}/\w*\d*_\d*\.[s]*htm[l]*'

