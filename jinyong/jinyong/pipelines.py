# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import datetime
from twisted.enterprise import adbapi
import pymysql.cursors
import logging
from scrapy.exporters import JsonItemExporter

class JinyongPipeline(object):
    def open_spider(self, spider):
        # 可选实现，当spider被开启时，这个方法被调用。
        # 输出到tongcheng_pipeline.json文件
        self.file = open('jingyongBook.json', 'wb')
        self.exporter = JsonItemExporter(self.file, encoding='utf-8')
        self.exporter.start_exporting()

    def close_spier(self, spider):
        # 可选实现，当spider被关闭时，这个方法被调用
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

class MySQLPipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host='127.0.0.1',  # 数据库地址
            port=3306,  # 数据库端口
            db='scrapy',  # 数据库名
            user='root',  # 数据库用户名
            passwd='wang123456',  # 数据库密码
            charset='utf8',  # 编码方式
            use_unicode=True)
        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor();

    def process_item(self, item, spider):
        self.cursor.execute(
            """insert into novel(book_name, book_url, title_name, title_url ,book_status, author,publish_time, Publishing_house, content)
            value (%s, %s, %s, %s, %s, %s, %s, %s, %s)""",  # 纯属python操作mysql知识，不熟悉请恶补
            (item['book_name'],
            item['book_url'],
            item['title_name'],
            item['title_url'],
            item['book_status'],
            item['author'],
            item['publish_time'],
            item['Publishing_house'],
            item['content']))


        # 提交sql语句
        self.connect.commit()
        return item  # 必须实现返回