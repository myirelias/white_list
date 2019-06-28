# 网易
TASK_NAME = '163'

# 起始URL
START_URL = 'https://www.163.com/'

# 控制域，必须为list格式
DOMAIN = ['163']
# 请求头
HEADERS = {

'Host': 'www.163.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
'Accept-Encoding': 'gzip, deflate, br',
'Cookie': '_ntes_nnid=feaeb766088e1a1f3ac4d5de0256f867,1533793227242; _ntes_nuid=feaeb766088e1a1f3ac4d5de0256f867; usertrack=ezq0pFtzkQSRXwEPJLyDAg==; _ga=GA1.2.331341228.1534300423; mail_psc_fingerprint=bc830b8c38bf97e4d2ca6aeea4ea4732; P_INFO=18980500107|1536022528|2|yanxuan_web|00&99|null&null&null#sic&510100#10#0#0|&0|null|18980500107; UM_distinctid=165fabe7f06428-0725ae9ca48bd48-12666d4a-1fa400-165fabe7f071cf; vinfo_n_f_l_n3=d046d3cc3155f352.1.3.1537510113926.1547794859622.1551668785920; CNZZDATA1257736923=1503113812-1547786148-%7C1551667848; CNZZDATA1257737079=1226839684-1547786332-%7C1551663542; vjuids=-e68bae49a.1685f88bd55.0.286205507e27e8; vjlast=1547791023.1547791023.30; __gads=ID=8ae095b29f85e421:T=1547791116:S=ALNI_MagXzTJMexPH2OHTucivcrMIAe3VQ; ntes_renjian=; Province=028; City=028; NNSSPID=d338dee05c0a44ea8a8d4d30638ceea7; NTES_hp_textlink1=old; neteaseAD11934channelcookies11323758721529302658160607=2; _antanalysis_s_id=1551668692129; ne_analysis_trace_id=1551668706867; s_n_f_l_n3=d046d3cc3155f3521551668706876; _antanalysis_s_id=1551668708757; __oc_uuid=a36f7510-3e2a-11e9-b9e1-df7179e7a9d7',
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
        "title": "string(.//*/h1)",
        "news_date": "substring(normalize-space(.//*[@class='pub_time']|.//*[@class='post_time_source']),1,20)",
        "source": "translate(substring-after(.//*[contains(text(),'来源')],'来源:'),'举报','')",
        "author": "substring-after(.//*[@class='auth']/parent::p,'作者')",
        "navigation": "string(.//*[@class='post_crumb'])",
        "content": ".//*[@class='post_text']/descendant::p/text()|.//*[@class='endText']/descendant::p/text()",
        "editor": "substring-after(.//*[@class='ep-editor'],'：')",
        "tags": ".//*[@name='keywords']/@content"
    },
    {
        "title": "normalize-space(.//*[@id='h1title'])",
        "news_date": "substring(normalize-space(.//*[contains(@class,'ep-time-soure')]),1,20)",
        "source": "substring-after(normalize-space(.//*[contains(@class,'ep-time-soure')]),'来源:')",
        "author": "substring-after(.//*[contains(text(),'作者：')],'作者：')",
        "navigation": "normalize-space(.//*[contains(@class,'ep-crumb')])",
        "content": ".//*[@id='endText']/descendant::text()",
        "editor": "substring-after(normalize-space(.//*[@class='ep-editor']),'责任编辑：')",
        "tags": ".//*[@name='keywords']/@content"
    },
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d*/\d*/\d*/[\w*\d*]*\.[s]*htm[l]*'

