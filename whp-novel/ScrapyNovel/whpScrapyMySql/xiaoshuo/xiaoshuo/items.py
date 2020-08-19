# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class XiaoshuoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 最终pipelins 里面需要什么
    title = scrapy.Field()
    name = scrapy.Field()
    content = scrapy.Field()
    content_url = scrapy.Field()