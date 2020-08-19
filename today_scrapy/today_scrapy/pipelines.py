# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import requests

class TodayScrapyPipeline(object):
    def process_item(self, item, spider):
        return item

class TuchongPipeline(object):
    def process_item(self, item, spider):
        img_url = item['img_url'] #从items中得到图片url地址
        img_title= item['title'] #得到图片的名字
        headers = {
            'User-Agnet': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            'cookie':'webp_enabled=1; bad_ide7dfc0b0-b3b6-11e7-b58e-df773034efe4=78baed41-a870-11e8-b7fd-370d61367b46; _ga=GA1.2.1188216139.1535263387; _gid=GA1.2.1476686092.1535263387; PHPSESSID=4k7pb6hmkml8tjsbg0knii25n6'
        }
        if not os.path.exists(img_title):
            os.mkdir(img_title)
        filename =img_url.split('/')[-1]
        with open(img_title+'/'+filename, 'wb+') as f:
            f.write(requests.get(img_url, headers=headers).content)
        f.close()
        return item