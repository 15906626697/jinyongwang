# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from . import settings

class MaoyanPipeline(object):
    def process_item(self, item, spider):
        print( '*' * 50 )
        print( dict( item ) )
        print( '*' * 50 )

        return item

# 新建管道类,存入mysql
class MaoyanMysqlPipeline(object):
    # 开启爬虫时执行,只执行一次
    def open_spider(self,spider):
        print('我是open_spider函数')
        # 一般用于开启数据库
        self.db = pymysql.connect(
            settings.MYSQL_HOST,
            settings.MYSQL_USER,
            settings.MYSQL_PWD,
            settings.MYSQL_DB,
            charset = 'utf8'
        )
        self.cursor = self.db.cursor()

    def process_item(self,item,spider):
        ins = 'insert into film(name,star,time) ' \
              'values(%s,%s,%s)'
        L = [
            item['name'].strip(),
            item['star'].strip(),
            item['time'].strip()
        ]
        self.cursor.execute(ins,L)
        # 提交到数据库执行
        self.db.commit()
        return item

    # 爬虫结束时,只执行一次
    def close_spider(self,spider):
        # 一般用于断开数据库连接
        print('我是close_spider函数')
        self.cursor.close()
        self.db.close()