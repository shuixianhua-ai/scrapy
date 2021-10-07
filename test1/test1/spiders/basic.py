import scrapy
#from test1.test1.items import Test1Item
class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['test1.com']
    start_urls = ['http://so.news.cn/#search/0/%E6%96%B0%E5%86%A0/1/']

    def parse(self,response):
        html=response.text
        news_list=response.xpath('//div[@class="search_result"]/div[@class="resultCnt"]/div[@class="resultList"]/div[@class="news"]')
        for news in news_list:
            #item=Test1Item()
            #item["title"]=news.xpath('./h2/a/text()').extract_first()
            title=news.xpath('./h2/a/text()').extract_first()
            #item["date"]=news.xpath('./div[@class="easynews"]/div[@class="newstime"]/span').extract_first()
            date=news.xpath('./div[@class="easynews"]/div[@class="newstime"]/span').extract_first()
            #item["lab"]=news.xpath('./div[@class="easynews"]/div[@class="newstime"]/p[@class="tag"]/span').extract_first()
            lab=news.xpath('./div[@class="easynews"]/div[@class="newstime"]/p[@class="tag"]/span').extract_first()
            print(title)
            print(date)
            print(lab)


