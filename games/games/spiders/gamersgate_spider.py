# -*- coding: utf-8 -*-
import scrapy
from games.items import GamesItem

class GamersgateSpiderSpider(scrapy.Spider):
	name = 'gamersgate_spider'
	allowed_domains = ['br.gamersgate.com']
	start_urls = [
		'https://br.gamersgate.com/games?prio=topsellers&pg=1',
		'https://br.gamersgate.com/games?prio=topsellers&pg=2',
		'https://br.gamersgate.com/games?prio=topsellers&pg=3',
		'https://br.gamersgate.com/games?prio=topsellers&pg=4',
		'https://br.gamersgate.com/games?prio=topsellers&pg=5',
		'https://br.gamersgate.com/games?prio=topsellers&pg=6',
		'https://br.gamersgate.com/games?prio=topsellers&pg=7',
		'https://br.gamersgate.com/games?prio=topsellers&pg=8'
		]

	def parse(self, response):
		cond = True
		links = response.xpath('//a[@class="ttl"]/@href').extract()
		for link in links:
			if(link != '/DD-GTAV-GN/'):
				yield response.follow(link, callback = self.trata_produto)
		if(cond):
			yield response.follow('https://br.gamersgate.com/DD-GTAV-GN/',callback = self.trata_produto)
			cond = False


	def trata_produto(self, response):
		name = response.xpath('//div[@class="ttl"]/h1/text()').extract_first()
		price_temp = response.xpath('//div[@class="price_price"]/span/text()').extract_first()
		price = ''
		for i in range(2,len(price_temp)):
			price = price + price_temp[i]
		date_temp = response.xpath('//ins[@class="local-datetime"]/text()').extract_first()
		date = ''
		for i in range(len(date_temp)-18):
			date = date + date_temp[i]
		dev = response.xpath('//ul[@id="PP_gs_list_facts"]/li[4]/span[2]/text()').extract_first().strip()
		pub = response.xpath('//ul[@id="PP_gs_list_facts"]/li[3]/span/meta/@content').extract_first()
		cat = response.xpath('//ul[@id="PP_gs_list_facts"]/li[2]/span/a/text()').extract()
		game = GamesItem(name = name, price = price, date = date, dev = dev, pub = pub, cat = cat)
		yield game

