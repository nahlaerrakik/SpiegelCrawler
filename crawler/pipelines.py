__author__ = 'nahla.errakik'

from crawler.models import Article


class CrawlerPipeline:

    @staticmethod
    def process_item(item, *args, **kwargs):
        article = Article(article_id=item['article_id'],
                          title=item['title'],
                          subtitle=item['subtitle'],
                          abstract=item['abstract'])
        try:
            article.insert()
        except Exception:
            article.update()

        return item
