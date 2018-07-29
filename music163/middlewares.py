# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import requests
import random
from music163 import get_random_ip as ip


class Music163SpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class RandomProxy(object):
    """Custom ProxyMiddleware."""

    def __init__(self):
        self.ip_list = ['221.217.50.222:9000', '101.132.122.230:3128', '111.121.193.214:3128', '203.130.46.108:9090', '122.72.18.35:80', '113.200.56.13:8010', '218.60.8.98:3129', '122.72.18.34:80', '124.193.85.88:8080', '119.29.252.90:3128', '121.42.167.160:3128', '218.60.8.99:3129', '180.101.205.253:8888', '124.235.208.252:443', '218.60.8.83:3129', '1.71.188.37:3128', '118.190.210.227:3128', '182.18.13.149:53281', '183.129.207.77:10000']
        pass

    def parse_request(self, request, spider):
        proxy = random.choice(self.ip_list)
        request.meta['proxy'] = 'http://{}'.format(proxy)


class RandomUserAgent(object):
    """Randomly rotate user agents based on a list of predefined ones"""

    def __init__(self, agents):
        self.agents = agents

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))

    def process_request(self, request, spider):
        # print("**************************" + random.choice(self.agents))
        request.headers.setdefault('User-Agent', random.choice(self.agents))
