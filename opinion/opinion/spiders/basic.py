import scrapy


class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['basic.cn']
    start_urls = ['http://basic.cn/']

    def parse(self, response):
        pass
