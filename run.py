__author__ = 'nahla.errakik'

import asyncio
import os
from datetime import datetime
from threading import Thread

from crawler.spiders.articles import ArticleSpider


async def main(task):
    while True:
        await asyncio.sleep(5)
        print("Starting crawling", datetime.now())
        task()


if __name__ == '__main__':
    def crawl(): os.system('scrapy crawl {}'.format(ArticleSpider.name))


    """thread = Thread(target=crawl)
    print("Starting crawling", datetime.now())
    thread.start()"""

    loop = asyncio.get_event_loop()
    tasks = [asyncio.ensure_future(main(crawl))]
    loop.run_until_complete(asyncio.wait(tasks))
