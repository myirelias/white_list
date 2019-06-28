# 央视网
TASK_NAME = 'cctv'

# 起始URL
START_URL = 'http://www.cctv.com/'

# 控制域，必须为list格式
DOMAIN = ['cctv.com', 'cctv.cn', 'cntv.cn']
# 请求头
HEADERS = {
    'Host': 'www.cctv.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0',
}

# xpath规则
XPATHER_HREF = ".//*/@href"
# 字段模版
# {
#     "title": "",
#     "publish_time": "",
#     "source": "",
#     "author": "",
#     "belong": "",
#     "content": "",
#     "editor": "",
# },
XPATHER_NEWS_LIST = [
    {
        "title": ".//*[@class='cnt_bd']/h1/text()",
        "publish_time": "substring-after(.//*[@class='info'], '网')",
        "soruce": "substring-before(substring-after( .//*[@class='info'],'来源'),' ')",
        "author": "",
        "belong": "",
        "content": ".//*[@class='cnt_bd']/p/text()",
        "editor": "",
    },
    {
        "title": ".//*[@class='cnt_nav']/h3/text()",
        "publish_time": "substring-after(.//*[text()='更新时间：']/parent::p,'更新时间：')",
        "soruce": "substring-after(.//*[text()='来源：']/parent::p,'：')",
        "author": "",
        "belong": "",
        "content": ".//*[text()='视频简介：']/parent::p/descendant::text()",
        "editor": "",

    },
    {
        "title": ".//*/h1/text()",
        "publish_time": "substring-after(substring-before(.//*[contains(text(),'来源')],'来源'),'期')",
        "source": "substring-after(.//*[contains(text(),'来源')],'来源：')",
        "author": "",
        "belong": "",
        "content": ".//*[@id='page_body']/descendant::p[starts-with(@style,'text')]/text()",
        "editor": "",
    },
    {
        "title": ".//*[@id='bt']/h3[1]/text()",
        "publish_time": "substring-after(.//*[contains(text(),'来源')],'网')",
        "source": "substring-before(substring-after(.//*[contains(text(),'来源')],'来源:'),' ')",
        "author": "",
        "belong": "",
        "content": ".//*[@class='font_nr'][1]/div[1]/descendant::text()",
        "editor": "",
    },
    {
        "title": "string(.//*[@class='title']/h3)",
        "publish_time": "substring-after(.//*[contains(text(),'来源')],'网')",
        "source": "substring-before(substring-after(.//*[contains(text(),'来源')],'来源：'),' ')",
        "author": "",
        "belong": "",
        "content": ".//*[@class='image']/descendant::p/text()",
        "editor": "",
    }

]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{4}/\d{2}/\d{2}/.*?\.shtml'

