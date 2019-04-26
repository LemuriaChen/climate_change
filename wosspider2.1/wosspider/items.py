# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WosspiderItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    author2 = scrapy.Field()
    reprintauthor = scrapy.Field()
    journal = scrapy.Field()
    volume = scrapy.Field()
    issue = scrapy.Field()
    page = scrapy.Field()
    doi = scrapy.Field()
    pubdate = scrapy.Field()
    documenttype = scrapy.Field()
    publisher = scrapy.Field()
    researchdomain = scrapy.Field()
    abstract = scrapy.Field()
    authorkeywords = scrapy.Field()
    keywordsplus = scrapy.Field()
    reprintaddress = scrapy.Field()
    address = scrapy.Field()
    emailaddress = scrapy.Field()
    fund = scrapy.Field()
    researchareas = scrapy.Field()
    woscategories = scrapy.Field()
    lang = scrapy.Field()
    wosnum = scrapy.Field()
    issn = scrapy.Field()
    eissn = scrapy.Field()
    idsnum = scrapy.Field()
    refer = scrapy.Field()
    cited = scrapy.Field()
    url = scrapy.Field()
    referarticles = scrapy.Field()
    authorrefer = scrapy.Field()
    journalrefer = scrapy.Field()
    othersrefer = scrapy.Field()
    coauthors = scrapy.Field()
    authorlistkey = scrapy.Field()
    impact = scrapy.Field()
    authorid = scrapy.Field()

