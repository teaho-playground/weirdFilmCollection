import scrapy


# {
#   "directors": [
#     "弗兰克·德拉邦特"
#   ],
#   "rate": "9.6",
#   "cover_x": 2000,
#   "star": "50",
#   "title": "肖申克的救赎",
#   "url": "https://movie.douban.com/subject/1292052/",
#   "casts": [
#     "蒂姆·罗宾斯",
#     "摩根·弗里曼",
#     "鲍勃·冈顿",
#     "威廉姆·赛德勒",
#     "克兰西·布朗"
#   ],
#   "cover": "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p480747492.webp",
#   "id": "1292052",
#   "cover_y": 2963
# },
class MovieInfoItem(scrapy.Item):
    # douban id
    id = scrapy.Field()
    # 电影名称
    title = scrapy.Field()
    # 评分
    rate = scrapy.Field()
    # url
    url = scrapy.Field()
    # directors
    directors = scrapy.Field()
    #casts
    casts = scrapy.Field()
    # rating number
    number = scrapy.Field()

    imdburl = scrapy.Field()
    #imdb rate
    imdbRate = scrapy.Field()
    #imdb rating number
    imdbRateNumber = scrapy.Field()
