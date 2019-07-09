
# rabbitmq host  # 需要分布式的时候要修改ip
# HOST = '192.168.2.71'
MQ_HOST = 'localhost'
MQ_PORT = 5672

# 爬虫个数
SPIDER_COUNT = 2

# 休眠时间
SLEEP_TIME = 1

# 需要过滤的url后缀
URL_END = ['mp3', 'mp4', 'css', 'm4a', 'pdf', 'zip', 'RAR', 'exe', 'rm',
           'avi', 'tmp', 'xls', 'mdf', 'txt', 'doc', 'MID', 'jpg']

# rabbitmq队列限制(大约数量)
MQ_MAXSIZE = 10000

# REDIS_HOST = '127.0.0.1'
# REDIS_PORT = 6379
REDIS_PSW = 'daqsoft2019'
# REDIS_DB = 0
REDIS_PARAMS = {
    'startup_nodes': [
        {'host': '192.168.2.44', 'port': 7000},
        {'host': '192.168.2.44', 'port': 7001},
        {'host': '192.168.2.44', 'port': 7002},
        {'host': '192.168.2.167', 'port': 7003},
        {'host': '192.168.2.167', 'port': 7004},
        {'host': '192.168.2.167', 'port': 7005},
        {'host': '192.168.2.91', 'port': 7000},
        {'host': '192.168.2.91', 'port': 7001},
        {'host': '192.168.2.91', 'port': 7002},
        ],
    'password': 'daqsoft2019'
    }


# mongodb
MONGO_HOST = '192.168.2.91'
# MONGO_PORT = 27017
# MONGO_DB = 'admin'
# MONGO_USER = 'spider'
# MONGO_PSW = 'daqsoft'
# MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017
# MONGO_DB = 'admin'
MONGO_USER = 'root'
MONGO_PSW = 'daqsoft2019'
# DBNAME_SUCCESS = 'public_test'
DBNAME_SUCCESS = 'public_news'
DBNAME_FAIL = 'public_news_failed'
# DBNAME_FAIL = 'public_test'


# proxy
PROXY_INFO = {
    'PROXY_HOST': 'http-pro.abuyun.com',
    'PROXY_PORT': '9010',
    'PROXY_USER': 'H2RX754122ED3QQP',
    'PROXY_PASS': '8A57FAD6273DCA10'
}

# max count
MAX_COUNT_LIST = 50000
MAX_COUNT_NEWS = 50000

