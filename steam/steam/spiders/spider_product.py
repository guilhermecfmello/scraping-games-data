# -*- coding: utf-8 -*-
import scrapy


class SpiderProductSpider(scrapy.Spider):
    name = 'spider_product'
    allowed_domains = ['store.steampowered.com/search/?filter=topsellers/']
    start_urls = ['https://store.steampowered.com/search/?filter=topsellers//']

    def parse(self, response):
        links = response.xpath('//a[@class="search_result_row ds_collapse_flag"]/@href')
        print('\n\nINICIANDO VARREDURA DE ITENS NO SEGUINTE RANGE: {}'.format(len(links)))


        for i in range(len(links)):
        	link = links[i].extract()
        	print("\n\nENTRANDO UMA VEZ NO ITEM: "+link)
        	response.follow(link, self.product_info)
        # for i in range(len(links)):
        	# response.follow(links[i],self.product_info)

        	# scrapy.Request(links[i], callback=self.product_info)
        	# callback(self.product_info,)
        	# yield Request(links[i],callback=self.product_info)


        print('\n\nPRIMEIRA PAGINA PASSADA COM SUCESSO\n\n')
        # if(len(response.xpath('//h2'))<=1):

    def product_info(self,response):
		print('\n\nENTROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOU\n\n')
		if(len(response.xpath('//h2'))<=1):
			print('\n\n=========================== ERRO DE HIDE GATE AGE ======================')
		else:
			print('\n\n=========================== NOVO ITEM =============================\n')
			print('			Nome:'+response.xpath('//div[@class="apphub_AppName"]').extract())