
from scrapy import cmdline
# cmdline.execute("scrapy crawl douban_movie_top250 -o douban.csv".split())
cmdline.execute("scrapy crawl movie_info_crawl".split())