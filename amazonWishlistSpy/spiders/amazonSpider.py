#!/usr/bin/python
#-*- coding: utf-8 -*-

from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from amazonWishlistSpy.items import AmazonwishlistspyItem


class AmazonSpider(BaseSpider):
	name = "amazonSpider"
	allowed_domains = ["amazon.com"]
	start_urls = [
		"http://www.amazon.com/gp/registry/wishlist/12XDZWAFB377I"
	]
	
	def parse(self, response):
		sel = Selector(response)
		items = sel.xpath("//div[starts-with(@id,'itemInfo_')]")
		extraction = []
		for item in items:
			spyItem = AmazonwishlistspyItem()
			spyItem['title'] = item.xpath(".//a[starts-with(@id,'itemName')]/@title").extract()
			spyItem['price'] = item.xpath(".//span[contains(@class,'a-color-price')][1]/text()").extract()
			spyItem['link'] = item.xpath(".//a[starts-with(@id,'itemName')]/@href").extract()
                        extraction.append(spyItem)
                print str(len(items)) + " items extracted"
                return extraction
