# -*- coding: utf-8 -*-
import scrapy
from games.items import GamesItem

class NuuvemSpiderSpider(scrapy.Spider):
	name = 'nuuvem_spider'
	allowed_domains = ['nuuvem.com']
	start_urls = ['https://www.nuuvem.com/catalog/sort/bestselling/sort-mode/desc/page/1']

	def parse(self, response):
		for page in range(11):
			links = response.xpath('//a[@class="product-card--wrapper"]/@href').extract()
			for link in links:
				yield response.follow(link, callback = self.trata_produto)
			page = page + 1
			next_page = 'https://www.nuuvem.com/catalog/sort/bestselling/sort-mode/desc/page/{}'.format(page+2)
			yield response.follow(next_page, callback = self.parse)

	def trata_produto(self, response):
		name = response.xpath('//h1[@class="product-title"]/span/text()').extract_first()
		price = response.xpath('//meta[@itemprop="price"]/@content').extract_first()
		date = response.xpath('//ul[@class="product-widget--list"]/li/span/text()').extract_first()
		dev = response.xpath('//ul[@class="product-widget--list"]/li[2]/text()')[1].extract().strip()
		pub = response.xpath('//ul[@class="product-widget--list"]/li[3]/text()')[1].extract().strip()
		cat = response.xpath('//a[@class="label"]/text()').extract() #Lista de categorias
		game = GamesItem(name = name, price = price, date = date, dev = dev, pub = pub, cat = cat)		
		yield game
