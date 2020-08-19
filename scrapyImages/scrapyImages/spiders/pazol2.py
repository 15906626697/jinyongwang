# -*- coding: utf-8 -*-
import scrapy


class Pazol2Spider(scrapy.Spider):
    name = 'pazol2'
    allowed_domains = ['desk.zol.com.cn']
    start_urls = ['http://desk.zol.com.cn/']

    def parse(self, response):
        pass
