# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # 数据来源
    source = scrapy.Field()
    # 抓取时间
    time = scrapy.Field()
    # 新闻标题
    title = scrapy.Field()
    # 报导时间
    reported_time = scrapy.Field()
    # 新闻内容
    content = scrapy.Field()
    # 关键词
    keywords = scrapy.Field()
