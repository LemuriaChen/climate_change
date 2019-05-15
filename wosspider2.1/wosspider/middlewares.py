# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
from selenium import webdriver
import time
from scrapy.http.response.html import HtmlResponse
import requests
import json
from wosspider.models import ProxyModel
from twisted.internet.defer import DeferredLock

class WosspiderSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class WosspiderDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class UserAgentDownloadMiddleware(object):
    # user-agent随机请求头中间件
    USER_AGENTS = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; Avant Browser; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)',
        'Mozilla/5.0 (X11; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0',
        'Mozilla/5.0 (X11; Linux i586; rv:63.0) Gecko/20100101 Firefox/63.0',
        'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.10; rv:62.0) Gecko/20100101 Firefox/62.0'
    ]
    def process_request(self,request,spider):
        user_agent = random.choice(self.USER_AGENTS)
        request.headers['User-Agent'] = user_agent



class SeleniumDownloadMiddleware(object):
    def __init__(self):
        self.driver = webdriver.Chrome()

    def process_request(self,request,spider):
        self.driver.get(request.url)
        time.sleep(0.1)
        try:
            researcherid = self.driver.find_element_by_xpath("//a[@class='snowplow-hide-ResearcherID-and-ORCID']")
            researcherid.click()
            time.sleep(0.3)
        except:
            pass
        try:
            impact = self.driver.find_element_by_xpath("//a[@class='focusable-link snowplow-JCRoverlay']")
            impact.click()
            time.sleep(3)
        except:
            pass
        source = self.driver.page_source
        response = HtmlResponse(url=self.driver.current_url, body=source, request=request, encoding='utf-8')
        return response

# WOS爬到1个多小时会封IP，这里用稳定的芝麻代理
# class IPProxyDownloadMiddleware(object):
#
#     PROXY_URL = 'http://webapi.http.zhimacangku.com/getip?num=1&type=2&pro=&city=0&yys=0&port=11&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=45&mr=1&regions='
#
#     def __init__(self):
#         super(IPProxyDownloadMiddleware, self).__init__()
#         self.current_proxy = None
#         self.lock = DeferredLock()
#
#     def process_request(self, request, spider):
#         if 'proxy' not in request.meta:
#             # 请求代理
#             self.update_proxy()
#
#         request.meta['proxy'] = self.current_proxy.proxy
#
#     def process_response(self, request, response, spider):
#         if response.status != 200 or "twisted.python.failure.Failure twisted.internet.error.ConnectionLost" in response.url:
#             if not self.current_proxy.blacked:
#                 self.current_proxy.blacked = True
#             print('%s这个代理被加入黑名单了'%self.current_proxy.ip)
#             self.update_proxy()
#             # 如果来到这里，说明这个请求已经被识别为爬虫了
#             # 所有这个请求就相当于什么都没有获取到
#             # 如果不返回request，那么这个request就相当于没有获取到数据
#             # 也就是说，这个请求就被废掉了，这个数据就没有被抓取到
#             # 所有要重新返回request，让这个请求重新加入到调度中，
#             # 下次再发送
#             return request
#         # 如果是正常的，那么要记得返回response
#         # 如果不返回，那么这个resposne就不会被传到爬虫那里去
#         # 也就得不到解析
#         return response
#
#     def update_proxy(self):
#         self.lock.acquire()
#         if not self.current_proxy or self.current_proxy.blacked:
#             response = requests.get(self.PROXY_URL)
#             text = response.text
#             print('重新获取了一个代理：', text)
#             result = json.loads(text)
#             if len(result['data']) > 0:
#                 data = result['data'][0]
#                 proxy_model = ProxyModel(data)
#                 self.current_proxy = proxy_model
#         self.lock.release()
