# !/usr/bin/env python
# coding=utf-8
"""
白名单数据处理：
- 清空过滤器
- 已经抓取的数据读url
- 已抓取的url放到过滤器
- 删除抓取失败的数据
- 重新抓取
"""
import redis
from hashlib import md5
import os

try:
    from pymongo import MongoClient
except:
    import pymongo
from tqdm import tqdm

redis_host = '192.168.2.91'
redis_port = 6379
redis_psw = 'daqsoft2019'
mongo_host = '192.168.2.91'
mongo_port = 27017
local_mongo_host = '127.0.0.1'
local_mongo_port = 27017
COLNAMES = ['banyuetan_news',
 'cac_news',
 'cankaoxiaoxi_news',
 'ccdi_news',
 'cctv_news',
 'ce_news',
 'china_news',
 'chinanews_news',
 'chinaso_news',
 'chinatoday_news',
 'cnjiwang_news',
 'cnr_news',
 'cri_news',
 'dbw_news',
 'eastday_news',
 'enorth_news',
 'gmw_news',
 'gov_news',
 'hebei_news',
 'hebnews_news',
 'huanqiu_news',
 'k618_news',
 'lnd_news',
 'lwdf_news',
 'mct_news',
 'mof_news',
 'mofcom_news',
 'my399_news',
 'ndrc_news',
 'nen_news',
 'news_news',
 'nhfpc_news',
 'nmgnews_news',
 'people_news',
 'qianlong_news',
 'sxgov_news',
 'wenming_news',
 'xfrb_news',
 'xinmin_news',
 'yicai_news',
 'youth_news',
 'zgjx_news',
 '01ny_news',
 '020cf_news',
 '10jqka_news',
 '110_news',
 '123_news',
 '163_news',
 '21jrr_news',
 '35mc_news',
 '3773_news',
 '3news_news',
 '51credit_news',
 'agri_news',
 'ahwang_news',
 'aijinling_news',
 'altxw_news',
 'baike_news',
 'bbtnews_news',
 'bestb2b_news',
 'bjnews_news',
 'bznews_news',
 'cbea_news',
 'ccdy_news',
 'ccgp_news',
 'cdyee_news',
 'cfi_news',
 'changsha_news',
 'chemcp_news',
 'chinacourt_news',
 'chinadevelopment_news',
 'cj_news',
 'cnci_news',
 'cnfol_news',
 'cnhan_news',
 'cnii_news',
 'cnnb_news',
 'cnncw_news',
 'cntgol_news',
 'cps_news',
 'crnews_news',
 'crntt_news',
 'csfdc_news',
 'cssn_news',
 'ctnews_news',
 'cyol_news',
 'eastmoney_news',
 'etest8_news',
 'exam8_news',
 'fangtoo_news',
 'farmer_news',
 'gansudaily_news',
 'gzw_news',
 'hangzhou_news',
 'hefei_news',
 'hexun_news',
 'heze_news',
 'hnr_news',
 'hxtcpp_news',
 'ifensi_news',
 'ijia360_news',
 'iyaxin_news',
 'jcrb_news',
 'jiangxi_news',
 'jiaodong_news',
 'laoqianzhuang_news',
 'leju_news',
 'lijiangtv_news',
 'loupan_news',
 'lyrb_news',
 'minieastday_news',
 'my68_news',
 'northnews_news',
 'nvsheng_news',
 'nxing_news',
 'nyjx_news',
 'ocn_news',
 'offcn_news',
 'ofweek_news',
 'qdcaijing_news',
 'qing5_news',
 'qingdaonews_news',
 'qlwb_news',
 'qtv_news',
 'rmlt_news',
 'rmzxb_news',
 'scdaily_news',
 'southmoney_news',
 'sq1996_news',
 'sssc_news',
 'stcn_news',
 'stnn_news',
 'stockstar_news',
 'sxrb_news',
 'taizhou_news',
 'tianqi_news',
 'wdzj_news',
 'wxrb_news',
 'x3cn_news',
 'xinjr_news',
 'xjbs_news',
 'xjxnw_news',
 'xuanwww_news',
 'ybrbnews_news',
 'ycnews_news',
 'ynet_news',
 'ynfzb_news',
 'ynolw_news',
 'yntv_news',
 'zhifang_news',
 'zjj_news',
 'zjqiye_news',
 'zkxww_news',
 'zsnews_news',
 'zznews_news',
 '010lm_news',
 '022china_news',
 '0735_news',
 '10yan_news',
 '51zouqi_news',
 '730700_news',
 '95579_news',
 'asiaott_news',
 'bandao_news',
 'bdzx_news',
 'btzx_news',
 'cb_news',
 'cjshw_news',
 'cncn_news',
 'cnena_news',
 'cpnn_news',
 'cppcc_news',
 'cqrb_news',
 'ddnews_news',
 'dhtjb_news',
 'ditiezu_news',
 'dlxww_news',
 'ettoday_news',
 'gold_news',
 'hebdaily_news',
 'hebgcdy_news',
 'hf365_news',
 'ht139_news',
 'ht88_news',
 'hyqss_news',
 'icnkr_news',
 'ihk_news',
 'jingmen_news',
 'jygxw_news',
 'kelamayi_news',
 'lanzhou_news',
 'lcxw_news',
 'ljdb_news',
 'lsol_news',
 'lzbs_news',
 'mizhai_news',
 'ometal_news',
 'senn_news',
 'sjzdaily_news',
 'sportscn_news',
 'taihainet_news',
 'tiexue_news',
 'tpy888_news',
 'trjcn_news',
 'tuanjiebao_news',
 'wangchao_news',
 'wj001_news',
 'wsimen_news',
 'xashangwang_news',
 'xjsghdf_news',
 'xker_news',
 'xsnet_news',
 'xwdi_news',
 'yaan_news',
 'ytnews_news',
 'zggjysw_news',
 'zgkashi_news',
 'zx58_news']


class BloomFilter(object):

    def __init__(self, host='localhost', port=6379, db=0, psw='', blockNum=1,
                 key='bloomfilter_pub', bit_size=1 << 32):

        """

        :param host: the host of Redis

        :param port: the port of Redis

        :param db: witch db in Redis

        :param blockNum: one blockNum for about 90,000,000; if you have more strings for filtering, increase it.

        :param key: the key's name in Redis

        """

        self.server = redis.Redis(host=host, port=port, db=db, password=psw)

        self.bit_size = bit_size  # Redis的String类型最大容量为512M

        # self.seeds = [5, 7, 11, 13, 31, 37, 61]
        self.seeds = [5, 11, 31]

        self.key = key

        self.blockNum = blockNum

        self.hashfunc = []

        for seed in self.seeds:
            self.hashfunc.append(SimpleHash(self.bit_size, seed))

    def isContains(self, str_input):

        if not str_input:
            return False

        m5 = md5()

        m5.update(str_input.encode('utf-8'))

        str_input = m5.hexdigest()

        ret = True

        name = self.key + str(int(str_input[0:2], 16) % self.blockNum)

        for f in self.hashfunc:
            loc = f.hash(str_input)

            ret = ret & self.server.getbit(name, loc)

        return ret

    def insert(self, str_input):

        m5 = md5()

        m5.update(str_input.encode('utf-8'))

        str_input = m5.hexdigest()

        name = self.key + str(int(str_input[0:2], 16) % self.blockNum)

        for f in self.hashfunc:
            loc = f.hash(str_input)

            self.server.setbit(name, loc, 1)


class SimpleHash(object):
    """
    简单的hash算法
    """

    def __init__(self, cap, seed):
        self.cap = cap

        self.seed = seed

    def hash(self, value):
        ret = 0

        for i in range(len(value)):
            ret += self.seed * ret + ord(value[i])

        return (self.cap - 1) & ret


def bloomfilter(urls=[]):
    bloom_urls = BloomFilter(host=redis_host, port=redis_port, psw=redis_psw,
                             blockNum=6, key='bloomfilter_pub')
    for each in urls:
        bloom_urls.insert(each.get('news_url'))


def data_mongo(dbname='public_news'):
    mgclient = MongoClient(host=mongo_host, port=mongo_port)
    db = mgclient[dbname]
    for colname in tqdm(COLNAMES):
        col = db[colname]
        urls_res = col.find({}, {'_id': 0, 'news_url': 1}, no_cursor_timeout=True)
        bloomfilter(urls_res)


def clear_data():
    """
    清空抓取失败的数据
    :return:
    """
    mgclient = MongoClient(host=mongo_host, port=mongo_port)
    db = mgclient['public_news_failed']
    for colname in tqdm(COLNAMES):
        colname_failed = f'{colname}_failed'
        col = db[colname_failed]
        del_res = col.drop()
        if not del_res:
            print(f'{colname_failed} 删除失败')
    mgclient.close()


def tarans_mongo():
    """
    数据转移,单个转移
    :return:
    """
    while 1:
        total = 0
        localcol = input('本地集合[退出：q]：')
        servicecol = input('服务器集合[退出：q]：') if localcol != 'q' else 'q'
        if localcol == 'q' or servicecol == 'q':
            break
        local_client = MongoClient(host=local_mongo_host, port=local_mongo_port)
        service_client = MongoClient(host=mongo_host, port=mongo_port)
        localdb = local_client['db_public_opinion']
        servicedb = service_client['public_news']
        # local_colnames = localdb.collection_names()
        local_datas = localdb[localcol].find({}, {'_id': 0})
        for eachdata in tqdm(local_datas):
            total += 1
            servicedb[servicecol].insert_one({'title': eachdata.get('title', ''),
                                              'news_date': eachdata.get('publish_time', ''),
                                              'source': eachdata.get('source', ''),
                                              'author': eachdata.get('author', ''),
                                              'navigation': eachdata.get('belong', ''),
                                              'content': eachdata.get('content', ''),
                                              'editor': eachdata.get('editor', ''), 'tags': eachdata.get('tags', ''),
                                              'news_url': eachdata.get('url', ''),
                                              'crawl_date': eachdata.get('get_time', '')})
        print(f'{localcol}\t|\t{total}')


def check_mongo():
    # colnames = ['01ny_news',
    #             '020cf_news',
    #             '10jqka_news',
    #             '110_news',
    #             '123_news',
    #             '163_news',
    #             '21jrr_news',
    #             '35mc_news',
    #             '3773_news',
    #             '3news_news',
    #             '51credit_news',
    #             'agri_news',
    #             'ahwang_news',
    #             'aijinling_news',
    #             'altxw_news',
    #             'baike_news',
    #             'bbtnews_news',
    #             'bestb2b_news',
    #             'bjnews_news',
    #             'bznews_news',
    #             'cbea_news',
    #             'ccdy_news',
    #             'ccgp_news',
    #             'cdyee_news',
    #             'cfi_news',
    #             'changsha_news',
    #             'chemcp_news',
    #             'chinacourt_news',
    #             'chinadevelopment_news',
    #             'cj_news',
    #             'cnci_news',
    #             'cnfol_news',
    #             'cnhan_news',
    #             'cnii_news',
    #             'cnnb_news',
    #             'cnncw_news',
    #             'cntgol_news',
    #             'cps_news',
    #             'crnews_news',
    #             'crntt_news',
    #             'csfdc_news',
    #             'cssn_news',
    #             'ctnews_news',
    #             'cyol_news',
    #             'eastmoney_news',
    #             'etest8_news',
    #             'exam8_news',
    #             'fangtoo_news',
    #             'farmer_news',
    #             'gansudaily_news',
    #             'gzw_news',
    #             'hangzhou_news',
    #             'hefei_news',
    #             'hexun_news',
    #             'heze_news',
    #             'hnr_news',
    #             'hxtcpp_news',
    #             'ifensi_news',
    #             'ijia360_news',
    #             'iyaxin_news',
    #             'jcrb_news',
    #             'jiangxi_news',
    #             'jiaodong_news',
    #             'laoqianzhuang_news',
    #             'leju_news',
    #             'lijiangtv_news',
    #             'loupan_news',
    #             'lyrb_news',
    #             'minieastday_news',
    #             'my68_news',
    #             'northnews_news',
    #             'nvsheng_news',
    #             'nxing_news',
    #             'nyjx_news',
    #             'ocn_news',
    #             'offcn_news',
    #             'ofweek_news',
    #             'qdcaijing_news',
    #             'qing5_news',
    #             'qingdaonews_news',
    #             'qlwb_news',
    #             'qtv_news',
    #             'rmlt_news',
    #             'rmzxb_news',
    #             'scdaily_news',
    #             'southmoney_news',
    #             'sq1996_news',
    #             'sssc_news',
    #             'stcn_news',
    #             'stnn_news',
    #             'stockstar_news',
    #             'sxrb_news',
    #             'taizhou_news',
    #             'tianqi_news',
    #             'wdzj_news',
    #             'wxrb_news',
    #             'x3cn_news',
    #             'xinjr_news',
    #             'xjbs_news',
    #             'xjxnw_news',
    #             'xuanwww_news',
    #             'ybrbnews_news',
    #             'ycnews_news',
    #             'ynet_news',
    #             'ynfzb_news',
    #             'ynolw_news',
    #             'yntv_news',
    #             'zhifang_news',
    #             'zjj_news',
    #             'zjqiye_news',
    #             'zkxww_news',
    #             'zsnews_news',
    #             'zznews_news',
    #             'banyuetan_news',
    #             'cac_news',
    #             'cankaoxiaoxi_news',
    #             'ccdi_news',
    #             'cctv_news',
    #             'ce_news',
    #             'china_news',
    #             'chinanews_news',
    #             'cnr_news',
    #             'chinaso_news',
    #             'chinatoday_news',
    #             'cnjiwang_news',
    #             'cri_news',
    #             'dbw_news',
    #             'eastday_news',
    #             'enorth_news',
    #             'gmw_news',
    #             'gov_news',
    #             'hebei_news',
    #             'hebnews_news',
    #             'huanqiu_news',
    #             'k618_news',
    #             'lnd_news',
    #             'lwdf_news',
    #             'mct_news',
    #             'mof_news',
    #             'mofcom_news',
    #             'my399_news',
    #             'ndrc_news',
    #             'nen_news',
    #             'news_news',
    #             'nhfpc_news',
    #             'nmgnews_news',
    #             'people_news',
    #             'qianlong_news',
    #             'sxgov_news',
    #             'wenming_news',
    #             'xfrb_news',
    #             'xinmin_news',
    #             'yicai_news',
    #             'youth_news',
    #             'zgjx_news']
    colnames = ['cnr_news', 'chinanews_news', 'zhifang_news', 'chinaso_news', 'dbw_news']
    mgclient = MongoClient(host=mongo_host, port=mongo_port)
    db = mgclient['public_news']
    count = 0
    for eachcol in colnames:
        print('' if db[eachcol].find({}).count() > 0 else f'{eachcol}不存在\n', end='')
    mgclient.close()


def count_total():
    """
    计算下总数
    :return:
    """
    mgclient = MongoClient(host=mongo_host, port=mongo_port)
    db = mgclient['public_news']
    count = 0
    for eachcol in COLNAMES:
        cunum = db[eachcol].find({}).count()
        count += cunum
        print(f'{eachcol}\t|\t{cunum}')
    print(f'==============================\n总计已抓取{count}')
    mgclient.close()


def out_bat_file():
    """
    生成bat批处理文件中的部分内容
    :return:
    """
    taskname = ['01ny',
                '020cf',
                '10jqka',
                '110',
                '123',
                '163',
                '21jrr',
                '35mc',
                '3773',
                '3news',
                '51credit',
                'agri',
                'ahwang',
                'aijinling',
                'altxw',
                'baike',
                'bbtnews',
                'bestb2b',
                'bjnews',
                'bznews',
                'cbea',
                'ccdy',
                'ccgp',
                'cdyee',
                'cfi',
                'changsha',
                'chemcp',
                'chinacourt',
                'chinadevelopment',
                'cj',
                'cnci',
                'cnfol',
                'cnhan',
                'cnii',
                'cnnb',
                'cnncw',
                'cntgol',
                'cps',
                'crnews',
                'crntt',
                'csfdc',
                'cssn',
                'ctnews',
                'cyol',
                'eastmoney',
                'etest8',
                'exam8',
                'fangtoo',
                'farmer',
                'gansudaily',
                'gzw',
                'hangzhou',
                'hefei',
                'hexun',
                'heze',
                'hnr',
                'hxtcpp',
                'ifensi',
                'ijia360',
                'iyaxin',
                'jcrb',
                'jiangxi',
                'jiaodong',
                'laoqianzhuang',
                'leju',
                'lijiangtv',
                'loupan',
                'lyrb',
                'minieastday',
                'my68',
                'northnews',
                'nvsheng',
                'nxing',
                'nyjx',
                'ocn',
                'offcn',
                'ofweek',
                'qdcaijing',
                'qing5',
                'qingdaonews',
                'qlwb',
                'qtv',
                'rmlt',
                'rmzxb',
                'scdaily',
                'southmoney',
                'sq1996',
                'sssc',
                'stcn',
                'stnn',
                'stockstar',
                'sxrb',
                'taizhou',
                'tianqi',
                'wdzj',
                'wxrb',
                'x3cn',
                'xinjr',
                'xjbs',
                'xjxnw',
                'xuanwww',
                'ybrbnews',
                'ycnews',
                'ynet',
                'ynfzb',
                'ynolw',
                'yntv',
                'zhifang',
                'zjj',
                'zjqiye',
                'zkxww',
                'zsnews',
                'zznews']
    taskname_old = ['banyuetan',
                    'cac',
                    'cankaoxiaoxi',
                    'ccdi',
                    'cctv',
                    'ce',
                    'china',
                    'chinanews',
                    'chinaso',
                    'chinatoday',
                    'cnjiwang',
                    'cnr',
                    'cri',
                    'dbw',
                    'eastday',
                    'enorth',
                    'gmw',
                    'gov',
                    'hebei',
                    'hebnews',
                    'huanqiu',
                    'k618',
                    'lnd',
                    'lwdf',
                    'mct',
                    'mof',
                    'mofcom',
                    'my399',
                    'ndrc',
                    'nen',
                    'news',
                    'nhfpc',
                    'nmgnews',
                    'people',
                    'qianlong',
                    'sxgov',
                    'wenming',
                    'xfrb',
                    'xinmin',
                    'yicai',
                    'youth',
                    'zgjx']  # 2018第四季度的脚本
    pattern_kill = "taskkill /f /im python.exe"
    pattern_ping = "ping 127.0.0.1 -n 28800"  # 8小时切换一次
    pattern_end = "exit"
    count = 0
    for each in taskname:
        count += 1
        pattern_nr = f"start python run_engine.py '{each}'"
        print(pattern_nr)
        if count >= 20:
            count = 0
            print(pattern_ping)
            # print(pattern_kill)
    print(pattern_kill)
    print(pattern_end)


if __name__ == '__main__':
    # check_mongo()
    # data_mongo()
    bloomfilter()
    # tarans_mongo()
    # clear_data()
    # count_total()
    # out_bat_file()
