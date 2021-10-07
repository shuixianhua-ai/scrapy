# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from datetime import datetime
from jieba import analyse

import pymysql

class KeyswordPipeline(object):
    """
    添加数据来源及抓取时间；
    结合textrank算法，抽取新闻中最重要的5个词，作为关键词
    """
    def process_item(self, item, spider):

        # 抓取时间
        item['time'] = str(datetime.now())

        content = item['content']
        keywords = ' '.join(analyse.textrank(content, topK=5))

        # 关键词
        item['keywords'] = keywords

        return item

class NewschinaPipeline(object):
     def __init__(self):
         self.conn = pymysql.connect(
             host='localhost',
             #port=3306,
             database='public_opinion',
             user='root',
             password='root',
             charset='utf8',
             use_unicode=True
         )
         # 实例一个游标
         self.cursor = self.conn.cursor()

     def process_item(self, item, spider):
         sql = """
               insert into opinion(news,date)
                values (%s, %s);"""

         values = [
             item['title'],
             item['time']
         ]

         self.cursor.execute(sql, values)
         self.conn.commit()

         return item

     def close_spider(self, spider):
         self.cursor.close()
         self.conn.close()
