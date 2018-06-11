# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NuuvemItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    date = scrapy.Field()
    dev = scrapy.Field()
    pub = scrapy.Field()
    cat = scrapy.Field()