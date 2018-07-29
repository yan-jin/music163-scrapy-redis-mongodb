# -*- coding: utf-8 -*-

# Scrapy settings for music163 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'music163'

SPIDER_MODULES = ['music163.spiders']
NEWSPIDER_MODULE = 'music163.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'music163 (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 500
CONCURRENT_ITEMS = 20

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:

DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': 'ntes_nnid=d2f6439b14da34c7d880f0bfbc786c67,1504517946460; _ntes_nuid=d2f6439b14da34c7d880f0bfbc786c67; mail_psc_fingerprint=6cc70de6b2f9496ddbacab739e0c1b6a; _qddaz=QD.qeqbs9.xx0793.j75z51nn; usertrack=ezq0plqZc+2BL8W/IQbUAg==; _ga=GA1.2.1391936245.1520006126; nts_mail_user=shigang5ban@163.com:-1:1; __gads=ID=61e479d87ba875ce:T=1522915661:S=ALNI_MYWBn6jmeRK6xboA3nTZZQz7u_7WQ; UM_distinctid=16294d9340a2bf-06ba20af1d83f2-336c7b05-13c680-16294d9340b106e; vjuids=9c4f193fa.16294d936b4.0.a3c3772c71ac6; __f_=1524847626698; _iuqxldmzr_=32; hb_MA-BFF5-63705950A31C_source=www.google.com.hk; __utmc=94650624; playerid=56586618; Province=010; City=010; __utmz=94650624.1531558172.3.2.utmcsr=yoghurt-lee.online|utmccn=(referral)|utmcmd=referral|utmcct=/2017/02/17/solve-403-Forbidden/; NTES_YD_SESS=xwFlhcPtot2Fe8a4iBAfRDHhON3raCGMrXZbI.SuI2qFlgDdIRry4UqONUtEayCr0jalpoqtnNkGxNT1X3TXVFrT79mkBfEa4UitjxJhR_s6RqnlOaD636FKO0z1_V7FXoExxWSSAeuibIXd43.JhJgXHGeHwg3y3zkxOPHcakG6us7bTQLKiCIxeGGQmaezAZUbHUN2FEQ4nzaQyPvoS7yEcZEtLYmX1S4pVFd2FdItH; NTES_YD_PASSPORT=5UEfO6hOzAxh5e4Kb5XIMeK0kIDzqjhpP34dqYH79jvsNc6hHt_Vu3wqe3jBDVs_d9DNblwjoePm5TSgb4TbcY1TqgwQjvECwy9OUgMFCiR0AmQnlvywlN0S2v8kcHeIzARhPdrwmCZjA.azw93670L1Ltqz8ZKX.PoJrTho235SQdLKlrYa9njp50iOWAFOuuTSzh74We6UMe.XuDNfZrmga; S_INFO=1531638265|0|3&80##|18501232311; P_INFO=18501232311|1531638265|1|codecombat|00&99|bej&1531226641&study#bej&null#10#0#0|&0||18501232311; hb_MA-92E7-6C2BD5FB5ABF_source=e.codecombat.163.com; ajs_user_id=null; ajs_group_id=null; vjlast=1522915686.1531749130.22; s_n_f_l_n3=85043c88bc18b68f1531749129817; _antanalysis_s_id=1531749130272; ne_analysis_trace_id=1531749134326; NNSSPID=3f43636c993f450289e38ae7c62e93b5; vinfo_n_f_l_n3=85043c88bc18b68f.1.2.1522915686077.1526733862128.1531749138575; __utma=94650624.1391936245.1520006126.1531558172.1531827126.4; JSESSIONID-WYYY=zEJVPmmv6ZpnccnKXJYikOQ3Bv6u1%2Bq%2FkusgyjNrwBudQqfUGw3MsGAI3Y0Vq7kT1nJ31PSvC7aCOI%2Fp8%2Fmm1JvUKjrigxeE%2FRQDsVglk5FhwUoMrrsFMGEN%2BMrQB4Bh16sxTrG9t6Jrw96Y5y7BxjrN5Iwxbh1Sbg62ml8zNaiOSjJV%3A1531830665921; __utmb=94650624.73.10.1531827126; WM_TID=vV16Yewn2B8ZGrxJrJVET4RpKdNDP9%2BZ',
    'DNT': '1',
    'Host': 'music.163.com',
    'Pragma': 'no-cache',
    'Referer': 'http://music.163.com/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'music163.middlewares.Music163SpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'music163.middlewares.MyCustomDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'music163.pipelines.Music163Pipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400
}
MONGO_URI = '58.87.111.39:27017'
MONGO_DB = 'music163'

USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]
# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = [301, 302]
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# Retry when proxies fail
RETRY_TIMES = 5

# Retry on most error codes since proxies fail for different reasons
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]

LOG_LEVEL = 'INFO'
COOKIES_ENABLED = False
DOWNLOAD_TIMEOUT = 3

DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': 90,
    # Fix path to this module
    'music163.middlewares.RandomProxy': 100,
    'music163.middlewares.RandomUserAgent': 1,
}



# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
MYEXT_ENABLED = True
IDLE_NUMBER = 360
EXTENSIONS = {
    'music163.extensions.RedisSpiderSmartIdleClosedExtensions': 500,
}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'music163.pipelines.ScrapyspiderPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


SCHEDULER = "scrapy_redis.scheduler.Scheduler"


SCHEDULER_PERSIST = True


SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderQueue'
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderStack'


SCHEDULER_IDLE_BEFORE_CLOSE = 10

SCHEDULER_ORDER = 'BFO'

REDIS_HOST = '58.87.111.39'
REDIS_PORT = 6379
# Custom redis client parameters (i.e.: socket timeout, etc.)
REDIS_PARAMS = {}
REDIS_URL = 'redis://@58.87.111.39:6379'
# REDIS_PARAMS['password'] = 'itcast.cn'
# Ensure all spiders share same duplicates filter through redis.
DUPEFILTER_CLASS = 'scrapy_redis.dupefilter.RFPDupeFilter'

# The class used to detect and filter duplicate requests.

# The default (RFPDupeFilter) filters based on request fingerprint
# using the scrapy.utils.request.request_fingerprint function.
# In order to change the way duplicates are checked you could subclass RFPDupeFilter
# and override its request_fingerprint method.
# This method should accept scrapy Request object and return its fingerprint (a string).

# By default, RFPDupeFilter only logs the first duplicate request.
# Setting DUPEFILTER_DEBUG to True will make it log all duplicate requests.
DUPEFILTER_DEBUG = True

dont_filter=True
