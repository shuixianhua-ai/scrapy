import scrapy
from first.items import FirstItem
import time
from scrapy import Selector
import string

class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['search.sina.com.cn']
    #start_urls = ['http://www.gov.cn/fuwu/zt/yqfkzq/']
    start_urls = ['https://search.sina.com.cn/?q=%E6%96%B0%E5%86%A0+%E7%96%AB&c=news&from=channel&col=&range=all&source=&country=&size=10&stime=&etime=&time=&dpc=0&a=&ps=0&pf=0&page=1']
    pageNum = 1
    url = [
        'https://search.sina.com.cn/?q=%E6%96%B0%E5%86%A0+%E7%96%AB&c=news&from=channel&col=&range=all&source=&country=&size=10&stime=&etime=&time=&dpc=0&a=&ps=0&pf=0&page=%s']

    def parse(self, response):
        html = response.text
        print("1")
        news_list = response.xpath("//div[@class='result']/div[@class='box-result clearfix']")
        #news_list = response.xpath("//div[@class='news_list']")
        #print(news_list)

        print("2")

        for news in news_list:
            item=FirstItem()
            #item={}
            str = news.xpath(".//h2/a//text()").extract()
            item['news'] = ''.join(str)
            times = news.xpath(".//h2/span[@class='fgray_time']/text()").extract_first()
            item['date'] = times[-19:]
            print(item)
            yield item
        purl = response.xpath(
            "//div[@class='result']/table//div[@class='pagebox']/a[@title='下一页']/@href").extract_first()
        next_url = 'https://search.sina.com.cn/' + purl
        print(next_url)
        if self.pageNum < 10:
            self.pageNum = self.pageNum + 1
            yield scrapy.Request(next_url, callback=self.parse,dont_filter=True)





















