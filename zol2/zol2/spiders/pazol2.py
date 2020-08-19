# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from zol2.items import Zol2Item


class Pazol2Spider(scrapy.Spider):
    name = 'pazol2'
    # allowed_domains = ['desk.zol.com.cn']
    start_urls = ['http://desk.zol.com.cn/fengjing/1920x1080/']
    from_url = "http://desk.zol.com.cn"

    rules = (
        # 1.解决翻页
        Rule(LinkExtractor(allow=r'/fengjing/1920x1080/[0-1]?[0-9]?.html'), callback='parse_album', follow=True),
        # 2.进入各个图库的每一张图片页
        Rule(LinkExtractor(allow=r'/bizhi/\d+_\d+_\d+.html', restrict_xpaths=(
        "//div[@class='main']/ul[@class='pic-list2  clearfix']/li", "//div[@class='photo-list-box']")), follow=True),
        # 3.点击各个图片1920*1080按钮，获得html
        Rule(LinkExtractor(allow=r'/showpic/1920x1080_\d+_\d+.html'), callback='get_img', follow=True),
    )

    def get_img(self, response):
        item = Zol2Item()
        item['image_urls'] = response.xpath("//body/img[1]/@src").extract_first()
        item['image_title'] = str(self.num)
        self.num += 1
        yield item
