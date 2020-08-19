# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TodayScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class TuchongItem(scrapy.Item):
    title = scrapy.Field() #图片名字
    views = scrapy.Field() #浏览人数
    favorites = scrapy.Field()#点赞人数
    img_url = scrapy.Field()#图片地址

     # def get_insert_sql(self):
     #     # 存储时候用的sql语句
     #     sql = 'insert into tuchong(title,views,favorites,img_url)'
     #           ' VALUES (%s, %s, %s, %s)'
     #     # 存储的数据
     #     data = (self['title'], self['views'], self['favorites'], self['img_url'])
     #     return (sql, data)