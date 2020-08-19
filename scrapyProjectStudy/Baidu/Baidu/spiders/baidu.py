# -*- coding: utf-8 -*-
import scrapy

# https://www.cnblogs.com/maplethefox/p/11379149.html
class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        result = response.xpath('/html/head/title/text()').extract_first()
        print('*'*50)
        print(result)
        print( '*' * 50 )
        # pass
