# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WosspiderItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    abstract = scrapy.Field()
    authorkeywords = scrapy.Field()
    keywordsplus = scrapy.Field()
    researchareas = scrapy.Field()
    woscategories = scrapy.Field()
    lang = scrapy.Field()
    issn = scrapy.Field()
    refer = scrapy.Field()
    cited = scrapy.Field()
    url = scrapy.Field()
