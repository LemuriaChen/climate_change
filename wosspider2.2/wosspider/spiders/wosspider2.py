# -*- coding: utf-8 -*-
import scrapy


class Wosspider2Spider(scrapy.Spider):
    name = 'wosspider2'
    allowed_domains = ['webofknowledge.com']
    start_urls = ['http://webofknowledge.com/']

    def parse(self, response):
        pass
