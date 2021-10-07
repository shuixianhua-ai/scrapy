# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import logging

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import re

class SecondPipeline:
    def process_item(self, item, spider):
        #item["content"]=self.process_content(item["content"])
        logging.warning(item)


        return item

    def process_content(self,content):
        #去掉奇怪的符号
        content=[re.sub(r"\u3000|\s","",i)for i in content]
        #去掉空值
        content=[i for i in content if len(i)>0]
        return content
