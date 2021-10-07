# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html




from datetime import datetime
from jieba import analyse

import pymysql




class NewschinaPipeline(object):
     def __init__(self):
         self.conn = pymysql.connect(
             host='.......',
             port=3306,
             database='news_China',
             user='....',
             password='.....',
             charset='utf8'
         )
         # 实例一个游标
         self.cursor = self.conn.cursor()

     def process_item(self, item, spider):
         sql = """
               insert into ChinaNews(ID, 标题, 关键词, 正文, 数据来源,报道时间，抓取时间)
                values (%s, %s, %s, %s, %s,%s, %s);"""

         values = [
             item['title'],
             item['keywords'],
             item['content'],
             item['source'],
#             item['reported_time']
             item['time']
         ]
#
         self.cursor.execute(sql, values)
         self.conn.commit()

         return item

     def close_spider(self, spider):
         self.cursor.close()
         self.conn.close()