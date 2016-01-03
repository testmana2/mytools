# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShadowscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    server = scrapy.Field()
    server_port = scrapy.Field()
    local_port = scrapy.Field()
    password = scrapy.Field()
    timeout = scrapy.Field()
    method = scrapy.Field()
