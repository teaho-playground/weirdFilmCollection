from scrapy import Request
from scrapy.spiders import Spider

from weirdFilmCollection.spiders.DoubanAndImdbMovie.MovieInfoItem import MovieInfoItem

import json

class MovieInfoSpider(Spider):
    name = 'movie_info_crawl'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
        'Host': 'movie.douban.com',
        # 'Referer': 'https://movie.douban.com/tag'
    }



    cookies = {}
    #
    # meta = {
    #     'dont_redirect': True,  # 禁止网页重定向
    #     'handle_httpstatus_list': [301, 302]  # 对哪些异常返回进行处理
    # }

    def start_requests(self):
        # url = 'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&start=0'

        cookiesStr = 'bid=t1htc1i0rs0; gr_user_id=f718161f-c37c-4e5a-81a1-201046231536; __yadk_uid=DMpofioi9Q4wtmVE3FkqAwScTODg5zb4; ll="118282"; ue="479255131@qq.com"; _ga=GA1.2.1631231789.1495876888; ct=y; viewed="3344825_27049048_1458561"; ps=y; dbcl2="52248093:km/VRI4gOaQ"; ck=6Xyw; _vwo_uuid_v2=4B804F9BB6998926860B4413511B4344|75b2808571a962b0589eca6e8b38e62f; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1509121713%2C%22https%3A%2F%2Fwww.douban.com%2Fdoulist%2F170032%2F%3Fsort%3Dtime%26sub_type%3D8%22%5D; ap=1; _pk_id.100001.4cf6=2d02d658f45c2d5a.1495960767.126.1509122639.1509112464.; _pk_ses.100001.4cf6=*; __utma=30149280.1631231789.1495876888.1509112464.1509121714.14; __utmb=30149280.2.10.1509121714; __utmc=30149280; __utmz=30149280.1509107783.12.5.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=30149280.5224; __utma=223695111.1514359668.1495960767.1509112465.1509121714.120; __utmb=223695111.0.10.1509121714; __utmc=223695111; __utmz=223695111.1509107784.118.96.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; push_noty_num=0; push_doumail_num=0'

        cookieStrArray = cookiesStr.split(';')

        # for c in cookieStrArray:
        #     cc = c.split('=')
        #     self.cookies[cc[0]] = cc[1]
        #
        # print(self.cookies)

        i = 0
        while(i<=9960): #9960
            url = 'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&start='+str(i)
            yield Request(url, headers=self.headers, cookies=self.cookies)
            i += 20

        # 带着headers、cookies去请求self.start_urls[0],返回的response会被送到
        # 回调函数parse中
        # yield Request(self.start_urls[0], callback=self.parse, headers=self.headers,
        #               cookies=self.cookies, meta=self.meta)

    def parse(self, response):
        data = json.loads(response.body)
        movies = data['data']
        # print(movies)

        for movie in movies:
            movieInfoItem = MovieInfoItem()
            # print(movie['directors'])
            movieInfoItem['id'] = movie['id']
            movieInfoItem['title'] = movie['title']
            movieInfoItem['rate'] = float(movie['rate'])
            movieInfoItem['url'] = movie['url']
            directorStr = ''
            for director in  movie['directors']:
                directorStr = directorStr + ',' + director
            directorStr = directorStr[1:len(directorStr)]
            movieInfoItem['directors'] = directorStr
            castStr = ''
            for cast in movie['casts']:
                castStr = castStr + ',' + cast
            castStr = castStr[1:len(castStr)]
            movieInfoItem['casts'] = castStr

            yield Request(url=movie['url'], meta={'movieInfoItem': movieInfoItem}, headers=self.headers, callback=self.parse_detail,
                                 dont_filter=True, cookies=self.cookies)

            # yield movieInfoItem


    def parse_detail(self, response):
        movieInfoItem = response.meta['movieInfoItem']
        movieInfoItem['number'] = int(response.css('a.rating_people span::text').extract_first().replace(",", ""))
        movieInfoItem['imdburl'] = response.css('div#info a[href*=imdb]::attr(href)').extract_first()

        yield Request(url=movieInfoItem['imdburl'], meta={'movieInfoItem': movieInfoItem},callback=self.parse_imdb,dont_filter=True, cookies=self.cookies, headers=self.headers)


    def parse_imdb(self, response):
        movieInfoItem = response.meta['movieInfoItem']
        movieInfoItem['imdbRate'] = float(response.css('div.ratingValue strong span::text').extract_first())
        movieInfoItem['imdbRateNumber'] = int(response.css('div.imdbRating span[itemprop=ratingCount]::text').extract_first().replace(",", ""))

        yield movieInfoItem




