# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JinyongwangItem(scrapy.Item):
    # define the fields for your item here like:
    book_name = scrapy.Field()
    book_url = scrapy.Field()
    title_name = scrapy.Field()
    title_url = scrapy.Field()
    book_status = scrapy.Field()
    author = scrapy.Field()
    publish_time = scrapy.Field()
    Publishing_house = scrapy.Field()
    content = scrapy.Field()
    # pass