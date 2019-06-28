# 映象网
TASK_NAME = 'hnr'

# 起始URL
START_URL = 'http://www.hnr.cn/'

# 控制域，必须为list格式
DOMAIN = ['hnr']
# 请求头
HEADERS = {
    'Host': 'www.hnr.cn',
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
        "title": "string(.//*[@class='f32 lh48 mrg_t_30'])",
        "news_date": "normalize-space(.//*[contains(text(),'来源')]/parent::p/span[1])",
        "source": "substring(normalize-space(.//*[contains(text(),'来源')]),4,50)",
        "author": "",
        "navigation": "normalize-space(.//*[@class='left mrg_l_40 pad_t_10'])",
        "content": ".//*[@id='text_content']/descendant::text()",
        "editor": "substring(normalize-space(.//*[contains(text(),'责编')]),4,50)",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@id='txt_left']/h2)",
        "news_date": "normalize-space(.//*[contains(@class,'time')])",
        "source": "substring-after(normalize-space(.//*[contains(@class,'source')]),'来源：')",
        "author": "translate(substring-after(normalize-space(.//*[contains(text(),'作者')]),'作者：'),')','')",
        "navigation": "normalize-space(.//*[@class='left logo_fr_font lh32'])",
        "content": ".//*[@class='ZKHN_Editor']//*[not(@type='text/css')]/descendant::text()",
        "editor": "",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{4,6}/\d{1,2}/\d*\.[s]*htm[l]*'

