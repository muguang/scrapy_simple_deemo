__author__ = 'amu'

#coding: -*-utf-8 -*-
from scrapy import spider
from ..items import SpiderTItem


class Banhui_spuder(spider.Spider):
    name = "banhui"
    allowed_domains = ["http://tieba.baidu.com"]
    start_urls = [
        "http://tieba.baidu.com/p/3723828831",
    ]

    def parse(self, response):
        for sel in response.xpath("//img[@class='BDE_Image']"):
            item = SpiderTItem()
            item['url_img'] = sel.xpath("@src").extract()
            yield item


"""
class Topit_spider(spider.Spider):
    name = "topit"
    allowed_domains = ["http://www.topit.me"]
    start_urls = [
        "http://www.topit.me/tag/%E5%8A%A8%E6%BC%AB?p=1"
    ]

    def parse(self, response):

        print("start spider--------------------------")

        print(response.xpath("//div[@class='e m']"))

        for sel in response.xpath("//div[@class='e m']"):
            print("page 2223333----------------------")
            item = SpiderTItem()

            url_1 = sel.xpath("a/img/@src")
            url_2 = sel.xpath("a/img/@data-original")
           # item['url_img'] = url_1
          #  yield item
            print(url_1)
spider topit should    deal with the problem of 302 redirected;
"""