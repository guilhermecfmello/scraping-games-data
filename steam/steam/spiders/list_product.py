# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver

class SteamSpiderSpider(scrapy.Spider):
    name = 'steam_spider'
    allowed_domains = ['store.steampowered.com/search/?filter=topsellers']
    start_urls = ['https://store.steampowered.com/search/?filter=topsellers/']

    def parse(self, response):
        links = response.xpath('//a[@class="search_result_row ds_collapse_flag"]/@href').extract()
        # response.follow(links[4])

        for i in range(len(links)):
        	scrapy.Request(link[i], callback=self.product_info)

        print('\n\nPRIMEIRA PAGINA PASSADA COM SUCESSO')
        # if(len(response.xpath('//h2'))<=1):
        	
        	


    def product_info(self, response):
    	if(len(response.xpath('//h2'))<=1):
    		print('\n\n=========================== ERRO DE HIDE GATE AGE ======================')
    	else:
    		print('\n\n=========================== NOVO ITEM =============================\n')
    		print('			Nome:'+response.xpath('//div[@class="apphub_AppName"]').extract())
