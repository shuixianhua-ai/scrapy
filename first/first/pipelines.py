# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import logging
from first.items import FirstItem
import pymysql
class JobspiderPipeline(object):
    def __init__(self):
        # 1. 建立数据库的连接
        self.connect = pymysql.connect(
	    # localhost连接的是本地数据库
            #host='10.186.132.99',
            host='127.0.0.1',
            # mysql数据库的端口号
            port=3306,
            # 数据库的用户名
            user='root',
            # 本地数据库密码
            #passwd='password',
            passwd='root',
            #passwd='root',
            # 表名
            #db='webgisdb',
            db='public_opinion',
            # 编码格式
            charset='utf8',
            use_unicode=True

        )
        # 2. 创建一个游标cursor, 是用来操作表。
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        # 3. 将Item数据放入数据库，默认是同步写入。
        self.cursor.execute(
            """insert into opinion(news,date)
            value (%s,%s)""",
            (item['news'],item['date']
            ))
        self.connect.commit()




        #insert_sql = "INSERT INTO opinion(news) VALUES ('%s')" % (item["news"])
        #self.cursor.execute(insert_sql)

        # 4. 提交操作

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()
