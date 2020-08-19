# -*- coding: utf-8 -*-
from copy import deepcopy

import scrapy
from jinyongwang.items import JinyongwangItem

class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['www.jinyongwang.com']
    start_urls = ['http://www.jinyongwang.com/book/']

    def parse(self, response):
        item =JinyongwangItem()
        div_list =  response.xpath('//*[@id="main"]/div[@class="booklist"]/ul[@class="list"]/li')
        for div in div_list:
            item["book_url"] = div.xpath('.//p[@class="title"]/a/@href').extract_first()
            item["book_url"] =response.urljoin(item["book_url"])
            # print(item["book_url"] )
            yield scrapy.Request(url=item["book_url"],callback=self.parse_list ,meta={'item':deepcopy(item)})

    def parse_list(self,response):
        item = response.meta['item']
        book_list =response.xpath('//*[@id="pu_box"]/div[@class="main"]/ul[@class="mlist"]/li')
        for book in book_list:
            item["title_name"] = book.xpath('./a/text()').extract_first()
            item["title_url"] = book.xpath('./a/@href').extract_first()
            item["title_url"] = response.urljoin(item["title_url"])
            item["book_name"] =response.xpath('//*[@id="pu_box"]/div[@class="main"]/div[@class="booklist"]/h1[@class="title"]/span/text()').extract_first()
            item["book_status"] = response.xpath(
                '//*[@id="pu_box"]/div[@class="main"]/div[@class="booklist"]/h1[@class="title"]/text()').extract_first()
            item["author"] = response.xpath('//*[@id="pu_box"]/div[@class="main"]/div[@class="booklist"]/p[@class="author"]/a/text()').extract_first()
            item["publish_time"] =response.xpath('//*[@id="pu_box"]/div[@class="main"]/div[@class="booklist"]/p[2]/text()').extract_first()
            item["Publishing_house"] = response.xpath(
                '//*[@id="pu_box"]/div[@class="main"]/div[@class="booklist"]/p[3]/text()').extract_first()
            # print(item)
            yield scrapy.Request(url=item["title_url"], callback=self.parse_detail, meta={'item': deepcopy(item)})

    def parse_detail(self,response):
        item = response.meta['item']
        item["content"] = response.xpath('//*[@id="vcon"]/p/text()').extract()
        item["content"] =''.join(item["content"])

        print(item)
        yield item