# -*- coding: utf-8 -*-

# Scrapy settings for weirdFilmCollection project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'weirdFilmCollection'

SPIDER_MODULES = ['weirdFilmCollection.spiders']
NEWSPIDER_MODULE = 'weirdFilmCollection.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'weirdFilmCollection (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 7

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 15
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_DOMAIN = 1
CONCURRENT_REQUESTS_PER_IP = 1

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'weirdFilmCollection.middlewares.WeirdfilmcollectionSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 543,
    'weirdFilmCollection.middlewares.MyCustomDownloaderMiddleware': 125,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'weirdFilmCollection.pipelines.WeirdfilmcollectionPipeline': 300,
#}

ITEM_PIPELINES = {
    'weirdFilmCollection.pipelines.MysqlPipeline': 300,#保存到mysql数据库
}

#Mysql数据库的配置信息
MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'test'         #数据库名字，请修改
MYSQL_USER = 'root'             #数据库账号，请修改
MYSQL_PASSWD = 'sa'         #数据库密码，请修改

MYSQL_PORT = 3306               #数据库端口，在dbhelper中使用

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

IPPOOL=[
    {"ipaddr":"114.227.87.125:808"},
    {"ipaddr":"60.255.230.185:808"},
    {"ipaddr":"171.39.42.246:8123"},
    {"ipaddr":"122.140.57.243:8118"},
    {"ipaddr":"125.72.5.194:4310"},
    {"ipaddr":"220.166.240.171:8118"},
    {"ipaddr":"182.88.177.79:8118"}
]