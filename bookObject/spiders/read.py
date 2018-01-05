# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import BookobjectItem

class ReadSpider(CrawlSpider):
    name = 'read'
    allowed_domains = ['www.dushu.com']
    start_urls = ['https://www.dushu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'/book/\d{4}\.html'),follow=True,callback='parse_item'),#设为true才能继续提取
        #Rule(LinkExtractor(allow=r'/book/\d+_\d+\.html'),follow=True,callback='parse_page'),
    )

    def parse_item(self, response):

        bookitem = BookobjectItem()

        bookitem['book_name'] = response.xpath('//div[@class="bookslist"]/ul/li[1]/div/h3/a//text()').extract_first()
        bookitem['book_img'] = response.xpath('//div[@class="bookslist"]/ul/li[1]/div/div/a/img/@src').extract_first()

        book_info = response.xpath('//div[@class="bookslist"]/ul/li[1]/div/p[2]')
        bookitem['book_info'] = book_info.xpath("string(.)").extract_first()
        bookitem['author'] =response.xpath('//div[@class="bookslist"]/ul/li[1]/div/p[1]//text()').extract_first()
        yield bookitem

    def parse_page(self, response):
        print('----------->page')