# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
import  pymysql

class XiaoshuoPipeline(object):
    # def process_item(self, item, spider):
    #     # /home/tarena/盗墓笔记小说/
    #     directory = 'D:\\giteeStudy\\explore\\Daomu\\novel\\{}\\'.format(item['title'])
    #     # 创建文件夹
    #     if not os.path.exists(directory):
    #         os.makedirs(directory)
    #     filename = directory + item['name'].replace(' ', '_') + '.txt'
    #     with open(filename, 'w') as f:
    #         f.write(item['content'])
    #
    #     return item
    # def __init__(self):
    #     # 连接MySQL数据库
    #     self.connect = pymysql.connect(host='localhost', user='root', password='wang123456', db='spiders', port=3306)
    #     self.cursor = self.connect.cursor()
    #
    # def process_item(self, item, spider):
    #     # 往数据库里面写入数据
    #     self.cursor.execute(
    #         'insert into novel_content(novel_content_title,novel_content,novel_content_url)VALUES ("{}","{}","{}")'.format(item['name'], item['content'], item['content_url']))
    #     self.connect.commit()
    #     print(self.cur._last_executed)
    #     return item
    #
    # # 关闭数据库
    # def close_spider(self, spider):
    #     self.cursor.close()
    #     self.connect.close()


    def open_spider(self, spider):
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', db='spiders', password='wang123456',
                                    charset='utf8')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            sql = 'insert into novel_content (novel_content_title,novel_content,novel_content_url) VALUES (%s,%s,%s)'
            self.cursor.execute(sql, (item['name'], item['content'], item['content_url']))
            self.conn.commit()
            print('一条数据插入成功')
        except Exception as e:
            print(e)

        return item

    def close_spider(self, spider):
        print('close', spider)