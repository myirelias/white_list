# 文件位置
FN_OLD_URLS = 'old_urls.txt'

# rabbitmq host  # 需要分布式的时候要修改ip
# HOST = '192.168.2.71'
MQ_HOST = 'localhost'
MQ_PORT = 5672

# 爬虫个数
SPIDERS = 4

# 需要过滤的url后缀
URL_END = ['mp3', 'mp4', 'css', 'm4a', 'pdf', 'zip', 'RAR', 'exe', 'rm',
           'avi', 'tmp', 'xls', 'mdf', 'txt', 'doc', 'MID']


# rabbitmq队列限制(大约数量)
MQ_MAXSIZE = 10000

# redis config
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0

