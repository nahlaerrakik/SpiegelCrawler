__author__ = 'nahla.errakik'

import scrapy


class ArticleItem(scrapy.Item):
    """
    scrapy.Item class for storing an article fields
    """
    article_id = scrapy.Field()
    title = scrapy.Field()
    subtitle = scrapy.Field()
    abstract = scrapy.Field()
