# -*- coding: utf-8 -*-
import scrapy
from steam.items import SteamItem

games_lost = 0

class ListaProdutosSpider(scrapy.Spider):
    name = 'lista_produtos'
    allowed_domains = ['store.steampowered.com']
    start_urls = ['https://store.steampowered.com/search/?filter=topsellers&page=1']

    def parse(self, response):
    	global games_lost
        for page in range(12):
        	links = response.xpath('//a[@class="search_result_row ds_collapse_flag"]/@href').extract()
        	for link in links:
        		yield response.follow(link, callback = self.trata_produto)
        	page = page + 1
        	next_page = 'https://store.steampowered.com/search/?filter=topsellers&page={}'.format(page+2)
        	yield response.follow(next_page, callback = self.parse)

        print('\n\n\n\n\n============================================\n')
        print('				Total de jogos perdidos: {}'.format(games_lost))

    def trata_produto(self,response):
    	global games_lost
    	# Se ao tentar capturar item, o crawler ser travado na verificacao de idade
    	if(len(response.xpath('/div[@class="agegate_text_container btns"]'))>0):
    		games_lost = games_lost + 1
    	else:
    		price = response.xpath('//div[@class="game_purchase_price price"]/text()').extract_first()
    		#Caso o item apareca na pagina de promoção especial
    		if(price == None):
    			# price = response.xpath('//div[@class="game_purchase_action_bg"]//div[@class="discount_final_price"]/text()').extract_first()
    			# name = response.xpath('//div[@class="page_title_area game_title_area"]/h2/text()').extract_first()
    			# date = 
    			games_lost = games_lost + 1
    		#Caso o item esteja na pagina de game padrao	
    		else:
    			name = response.xpath('//div[@class="apphub_AppName"]/text()').extract_first()
    			price = price.strip()
    			date = response.xpath('//div[@class="date"]/text()').extract_first() #Formatar data
    			dev = response.xpath('//div[@class="dev_row"]//a/text()')[0].extract()
    			pub = response.xpath('//div[@class="dev_row"]//a/text()')[1].extract()
    			cat = response.xpath('//div[@class="block_content_inner"]/div[1]/a/text()').extract()
    			game = SteamItem(name=name,price=price,date=date,dev=dev,pub=pub,cat=cat)
    			yield game
