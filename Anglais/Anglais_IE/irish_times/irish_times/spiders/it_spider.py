#https://www.irishtimes.com/search/search-7.4195619?q=gilets+jaunes&fromDate=16%2F11%2F2018&toDate=20%2F02%2F2019&pageId=2.696&page=0
#https://www.irishtimes.com/search/search-7.4195619?q=gilets+jaunes&fromDate=16%2F11%2F2018&toDate=20%2F02%2F2019&pageId=2.696

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.contrib.exporter import XmlItemExporter
from bs4 import BeautifulSoup

class ItItem(scrapy.Item):
    url = scrapy.Field()
    titre = scrapy.Field()
    date = scrapy.Field()
    article = scrapy.Field()

class ItSpider(CrawlSpider):
    name = "irish_times"
    allowed_domains = ['irishtimes.com']
    start_urls = [
        'https://www.irishtimes.com/search/search-7.4195619?q=gilets+jaunes&fromDate=16%2F11%2F2018&toDate=20%2F02%2F2019&pageId=2.696&page=0',
        'https://www.irishtimes.com/search/search-7.4195619?q=gilets+jaunes&fromDate=16%2F11%2F2018&toDate=20%2F02%2F2019&pageId=2.696&page=1',
        'https://www.irishtimes.com/search/search-7.4195619?q=gilets+jaunes&fromDate=16%2F11%2F2018&toDate=20%2F02%2F2019&pageId=2.696&page=2',
        'https://www.irishtimes.com/search/search-7.4195619?q=gilets+jaunes&fromDate=16%2F11%2F2018&toDate=20%2F02%2F2019&pageId=2.696&page=3',
        'https://www.irishtimes.com/search/search-7.4195619?q=gilets+jaunes&fromDate=16%2F11%2F2018&toDate=20%2F02%2F2019&pageId=2.696&page=4'
    ]
    custom_settings = {'DEPTH_LIMIT': 2,}
    rules = (Rule(LinkExtractor(allow=('news/world/europe/', ), deny=('\.jpg')), callback='parse_item', follow=True),)


    def parse_item(self, response):
        self.logger.info('Hi, this is an item page! %s', response.url)
        item = ItItem()
        item['url'] = response.url
        item['titre'] = response.xpath('//h1//text()').extract_first()
        item['date'] = response.xpath('//time//text()').extract_first()
        item['article'] = response.css('p::text').getall()
        return item
