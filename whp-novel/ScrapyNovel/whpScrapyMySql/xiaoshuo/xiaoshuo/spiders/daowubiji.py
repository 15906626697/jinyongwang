# -*- coding: utf-8 -*-
import scrapy
from ..items import XiaoshuoItem

class DaowubijiSpider(scrapy.Spider):
    name = 'daowubiji'
    allowed_domains = ['www.daomubiji.com']
    start_urls = ['http://www.daomubiji.com/']

    def parse(self, response):
        # 基准xpath
        li_list = response.xpath('//li[contains(@id,"menu-item-20")]/a')
        print(li_list)
        for li in li_list:
            item = XiaoshuoItem()
            item['title'] = li.xpath('./text()').get()
            link = li.xpath('./@href').get()
            # 把link交给调度器入队列
            yield scrapy.Request(
                url=link,
                # 不同的解析函数之间传递数据
                meta={'item': item},
                callback=self.parse_two_page
            )

        # 二级页面解析函数: 名称+链接

    def parse_two_page(self, response):
        # 接收item
        item = response.meta['item']
        article_list = response.xpath('//article')
        for article in article_list:
            # item['name'] = article.xpath('./a/text()').get()
            name = article.xpath('./a/text()').get()
            two_link = article.xpath('./a/@href').get()
            item['content_url'] =article.xpath('./a/@href').get()
            yield scrapy.Request(
                url=two_link,
                meta={'item': item, 'name': name},
                callback=self.parse_three_page
            )
        # 三级二面解析

    def parse_three_page(self, response):
        # 接收item
        item = response.meta['item']
        item['name'] = response.meta['name']
        # content_list : ['p1','p2']
        content_list = response.xpath('//article[@class="article-content"]//p/text()').extract()
        item['content'] = '\n'.join(content_list)

        yield item
