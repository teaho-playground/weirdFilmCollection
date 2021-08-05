from scrapy import Request
from scrapy.spiders import Spider

from weirdFilmCollection.spiders.doubanMovie.DoubanMovieItem import DoubanMovieItem


class DoubanMovieTop250Spider(Spider):
    name = 'douban_movie_top250'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    # cookies = {}
    #
    # meta = {
    #     'dont_redirect': True,  # 禁止网页重定向
    #     'handle_httpstatus_list': [301, 302]  # 对哪些异常返回进行处理
    # }

    def start_requests(self):
        url = 'https://movie.douban.com/top250'
        yield Request(url, headers=self.headers)

        # 带着headers、cookies去请求self.start_urls[0],返回的response会被送到
        # 回调函数parse中
        # yield Request(self.start_urls[0], callback=self.parse, headers=self.headers,
        #               cookies=self.cookies, meta=self.meta)

    def parse(self, response):
        item = DoubanMovieItem()
        movies = response.xpath('//ol[@class="grid_view"]/li')
        for movie in movies:
            item['ranking'] = movie.xpath(
                './/div[@class="pic"]/em/text()').extract()[0]
            item['movie_name'] = movie.xpath(
                './/div[@class="hd"]/a/span[1]/text()').extract()[0]
            item['score'] = movie.xpath(
                './/div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
            item['score_num'] = movie.xpath(
                './/div[@class="star"]/span/text()').re('(\d+)人评价')[0]
            yield item

        next_url = response.xpath('//span[@class="next"]/a/@href').extract()
        if next_url:
            next_url = 'https://movie.douban.com/top250' + next_url[0]
            yield Request(next_url, headers=self.headers)