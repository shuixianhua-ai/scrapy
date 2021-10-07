# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Test1Item(scrapy.Item):

    title = scrapy.Field()
    href = scrapy.Field()
    date = scrapy.Field()
    lab = scrapy.Field()

