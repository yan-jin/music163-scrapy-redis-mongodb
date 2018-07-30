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
        self.ip_list = ['112.95.191.21:9797', '121.13.54.86:9797', '124.193.85.88:8080', '113.200.56.13:8010', '122.72.18.35:80', '203.130.46.108:9090', '180.101.205.253:8888', '218.60.8.98:3129', '114.215.95.188:3128', '122.72.18.34:80', '218.60.8.83:3129', '218.60.8.99:3129', '124.235.208.252:443', '119.29.252.90:3128', '221.217.53.131:9000', '121.43.170.207:3128', '118.190.210.227:3128', '180.168.198.141:18118', '116.62.194.248:3128']
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
