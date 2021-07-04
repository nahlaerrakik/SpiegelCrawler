__author__ = 'nahla.errakik'

import re

import scrapy

from crawler.items import ArticleItem


class ArticleSpider(scrapy.Spider):
    """ Spider class for scraping articles from https://www.spiegel.de/international/"""

    name = 'articles'
    start_urls = [
        'https://www.spiegel.de/international/'
    ]

    def parse(self, response, **kwargs):
        """
        parses the content of the url to scrap
        :param response: response content of the scraped url
        :return: yields article object
        """
        item = ArticleItem()

        articles = response.css('article')
        for article in articles:
            article_id = self._get_id(article=article)
            if article_id is None:
                continue

            title = self._get_title(article=article)
            subtitle = self._get_subtitle(article=article)
            abstract = self._get_abstract(article=article)

            item['article_id'] = article_id
            item['title'] = title
            item['subtitle'] = subtitle
            item['abstract'] = abstract

            yield item

        next_url = self._get_next_url(content=response)
        if next_url is not None:
            yield response.follow(next_url, callback=self.parse)

    @staticmethod
    def _get_id(article):
        """
        Generate the id of an article
        :param article: scrapy selector object containing the html content of an article
        :return: The id of the article
        """
        id1 = article.css('article::attr(data-sara-article-id)').extract()
        if len(id1) > 0:
            return id1[0]

        id2 = article.css('article::attr(ata-sara-article-id)').extract()
        if len(id2) > 0:
            return id2[0]

    @staticmethod
    def _get_title(article):
        """
        Generate the title of an article
        :param article: scrapy selector object containing the html content of an article
        :return: The title of the article
        """
        header = article.css('header')
        titles = header.css('a::attr(title)').extract()
        if len(titles) > 0:
            return titles[0]

    @staticmethod
    def _get_subtitle(article):
        """
        Generate the subtitle of an article
        :param article: scrapy selector object containing the html content of an article
        :return: The subtitle of the article
        """
        header = article.css('header')
        subtitles = header.css('span.text-primary-base::text').extract()
        if len(subtitles) > 0:
            return subtitles[0]

    @staticmethod
    def _get_abstract(article):
        """
        Generate the abstract of an article
        :param article: scrapy selector object containing the html content of an article
        :return: The abstract of the article
        """
        section = article.css('section')
        abstracts = section.css('span.font-serifUI::text').extract()
        if len(abstracts) > 0:
            return abstracts[0]

    @staticmethod
    def _get_next_url(content):
        """
        Generate the subtitle of an article
        :param content: scrapy selector object containing the html content of the url
        :return: next url to scrap
        """
        tag = content.xpath('//span[@title="Ältere Artikel"]')
        url = tag.css('span::attr(onclick)').extract_first()
        url = re.findall(r"https?://[^\s']+", url)
        if len(url) > 0:
            return url[0]
