# -*- coding: utf-8 -*-
import scrapy
from nuuvem.items import NuuvemItem

produtos = 0
itens = 0
class ListaProdutosSpider(scrapy.Spider):
	name = 'lista_produtos'
	allowed_domains = ['nuuvem.com']
	start_urls = ['https://www.nuuvem.com/catalog/sort/bestselling/sort-mode/desc/page/1']

	def parse(self, response):
		global itens
		global produtos
		for page in range(11):
			links = response.xpath('//a[@class="product-card--wrapper"]/@href').extract()
			for link in links:
				itens = itens + 1
				yield response.follow(link, callback = self.trata_produto)
			page = page + 1
			next_page = 'https://www.nuuvem.com/catalog/sort/bestselling/sort-mode/desc/page/{}'.format(page+2)
			yield response.follow(next_page, callback = self.parse)
		print('\n\n========================================')
		print('FIM DO CRAWLER, ITENS= {} PRODUTOS= {}'.format(itens,produtos))

	def trata_produto(self, response):
		global produtos
		produtos = produtos + 1
		name = response.xpath('//h1[@class="product-title"]/span/text()').extract_first()
		price = response.xpath('//meta[@itemprop="price"]/@content').extract_first()
		date = response.xpath('//ul[@class="product-widget--list"]/li/span/text()').extract_first()
		dev = response.xpath('//ul[@class="product-widget--list"]/li[2]/text()')[1].extract() #Arrumar formatacao
		pub = response.xpath('//ul[@class="product-widget--list"]/li[3]/text()')[1].extract() #Arrumar formatacao
		cat = response.xpath('//a[@class="label"]/text()').extract() #Lista de categorias
		game = NuuvemItem(name = name, price = price, date = date, dev = dev, pub = pub, cat = cat)
		print ("segmentation fault")
		
		yield game