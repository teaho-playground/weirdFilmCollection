# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from twisted.enterprise import adbapi
import pymysql
# import MySQLdb.cursors
import codecs
import json
from logging import log

# class WeirdfilmcollectionPipeline(object):
#     def process_item(self, item, spider):
#         return item
#
#
# class JsonWithEncodingPipeline(object):
#     '''保存到文件中对应的class
#        1、在settings.py文件中配置
#        2、在自己实现的爬虫类中yield item,会自动执行'''
#
#     def __init__(self):
#         self.file = codecs.open('info.json', 'w', encoding='utf-8')  # 保存为json文件
#
#     def process_item(self, item, spider):
#         line = json.dumps(dict(item)) + "\n"  # 转为json的
#         self.file.write(line)  # 写入文件中
#         return item
#
#     def spider_closed(self, spider):  # 爬虫结束时关闭文件
#         self.file.close()

#http://www.jianshu.com/p/44366e9a2ed5
# http://blog.csdn.net/u013082989/article/details/52589791
class MysqlPipeline(object):
    '''保存到数据库中对应的class
       1、在settings.py文件中配置
       2、在自己实现的爬虫类中yield item,会自动执行'''

    def __init__(self, conn):
        self.conn = conn
        ''' 这里注释中采用写死在代码中的方式连接线程池，可以从settings配置文件中读取，更加灵活
            self.dbpool=adbapi.ConnectionPool('MySQLdb',
                                          host='127.0.0.1',
                                          db='crawlpicturesdb',
                                          user='root',
                                          passwd='123456',
                                          cursorclass=MySQLdb.cursors.DictCursor,
                                          charset='utf8',
                                          use_unicode=False)'''

    @classmethod
    def from_settings(cls, settings):
        '''1、@classmethod声明一个类方法，而对于平常我们见到的则叫做实例方法。
           2、类方法的第一个参数cls（class的缩写，指这个类本身），而实例方法的第一个参数是self，表示该类的一个实例
           3、可以通过类来调用，就像C.f()，相当于java中的静态方法'''
        conn = pymysql.connect(
            host=settings['MYSQL_HOST'],  # 读取settings中的配置
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],

            charset='utf8',  # 编码要加上，否则可能出现中文乱码问题
            use_unicode=False
        )
        return cls(conn)  # 相当于dbpool付给了这个类，self中可以得到


    # pipeline默认调用
    def process_item(self, item, spider):
        dbObject = self.conn
        cursor = dbObject.cursor()
        sql = "insert into MOVIE(ID,TITLE,RATE,URL,DIRECTORS,CASTS,NUMBER,IMDBURL,IMDBRATE,IMDBRATENUMBER) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        params = (item["id"], item["title"], item["rate"], item["url"], item["directors"], item["casts"], item["number"], item["imdburl"], item["imdbRate"], item["imdbRateNumber"])

        try:
            cursor.execute(sql, params)
            dbObject.commit()
        except Exception as e:
            print(e)
            dbObject.rollback()

        return item

