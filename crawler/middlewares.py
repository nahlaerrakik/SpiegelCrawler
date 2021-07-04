__author__ = 'nahla.errakik'

from scrapy import signals


class CrawlerSpiderMiddleware:
    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    @staticmethod
    def spider_opened(spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class CrawlerDownloaderMiddleware:

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    @staticmethod
    def spider_opened(spider):
        spider.logger.info('Spider opened: %s' % spider.name)
