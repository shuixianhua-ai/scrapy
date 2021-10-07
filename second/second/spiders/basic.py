import scrapy
from second.items import SecondItem
import threading

import logging
class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['guali.xsnet.cn']
    start_urls = ['http://guali.xsnet.cn/html/ygzw/']
    pageNum = 1  # 起始页码
    url = 'http://guali.xsnet.cn/html/ygzw/%s.html'  # 每页的u

‘https://search.sina.com.cn/?q=%E6%96%B0%E5%86%A0+%E7%96%AB&c=news&sort=time’

    def parse(self, response):
        new_list=response.xpath("//div[@class='main']/div[@class='list']/ul/li")



        for one in new_list:
            item=SecondItem()
            item["title"]=one.xpath(".//span/text()").extract()[0]
            item["date"]=one.xpath(".//a/text()").extract_first()
            item["href"]=one.xpath(".//a/@href").extract_first()
            yield item

        next_url = response.xpath("//div[@class='main']/div[@class='list']//a[text()='下一页']/@href").extract_first()

        next_url = ['http://guali.xsnet.cn' + next_url]
        print(next_url)
        final=['http://guali.xsnet.cn/html/ygzw/9.html']
        #if next_url != final :
         #   yield scrapy.Request(
          #      url=next_url,
           #     callback=self.parse,
            #    dont_filter=True
            #)
        if self.pageNum<9:
            self.pageNum=self.pageNum+1
            url = format(self.url % self.pageNum)
            yield scrapy.Request(url=url, callback=self.parse)








    def parse_con(self,response):
        item = response.meta["item"]
        item["content"] = response.xpath("//div[@class='con']//text()").extract()
        item["img"] = response.xpath("//div[@class='con']//img/@src").extract()
        yield item









