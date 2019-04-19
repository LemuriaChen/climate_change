# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from wosspider.items import WosspiderItem
from lxml import etree


class WosspiderSpider(CrawlSpider):
    name = 'wosspider'
    allowed_domains = ['apps.webofknowledge.com']
    start_urls = ['http://apps.webofknowledge.com/summary.do?product=UA&parentProduct=UA&search_mode=GeneralSearch&parentQid=&qid=3&SID=5EpTgjfkjTrGh8RQwsR&&update_back2search_link_param=yes&page=1']


    rules = (
        Rule(LinkExtractor(allow=r'.+summary.do\?.+&qid=3.+&page=\d'),follow=True),
        Rule(LinkExtractor(allow=r'.+full_record.do\?.+&qid=3.+&page=\d&doc=\d'), callback="parse_item", follow=True)
    )

    def parse_item(self, response):
        htmlElement = etree.HTML(response.text)
        alls = htmlElement.xpath("//div[@class='block-record-info']/p[@class='FR_field']")
        data = []
        for a in alls:
            # print(''.join(a.xpath(".//text()")))
            data.append(''.join(a.xpath(".//text()")))
            # print('*' * 30)
        title = ''.join(htmlElement.xpath("//div[@aria-label='Main content']//div[@class='title']//text()"))
        print(title)
        # print(data)
        # print(response.url)
        author = ''.join([s for s in data if "By" in s]).strip().replace("\n", "")
        abstract = ''.join(data[1]).strip().replace("\n", "")
        authorkeywords = ''.join([s for s in data if "Author Keywords" in s]).strip().replace("\n", "")
        keywordsplus = ''.join([s for s in data if "KeyWords Plus" in s]).strip().replace("\n", "")
        researchareas = ''.join([s for s in data if "Research Areas" in s]).strip().replace("\n", "")
        woscategories = ''.join([s for s in data if "Web of Science Categories" in s]).strip().replace("\n", "")
        lang = ''.join([s for s in data if "Language" in s]).strip().replace("\n", "")
        issn = ''.join([s for s in data if "ISSN" in s]).strip().replace("\n", "")
        refer = ''.join([s for s in data if "Cited References in Web of Science Core Collection" in s]).strip().replace("\n", "")
        cited = ''.join([s for s in data if "Times Cited in Web of Science Core Collection" in s]).strip().replace("\n", "")
        url = response.url

        item = WosspiderItem(
            title=title,
            author=author,
            abstract=abstract,
            authorkeywords=authorkeywords,
            keywordsplus=keywordsplus,
            researchareas=researchareas,
            woscategories=woscategories,
            lang=lang,
            issn=issn,
            refer=refer,
            cited=cited,
            url=url
        )
        yield item

