# Scrapy settings for crawler project

BOT_NAME = 'crawler'

SPIDER_MODULES = ['crawler.spiders']
ARTICLESPIDER_MODULE = 'crawler.spiders'

LOG_ENABLED = False

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
DOWNLOAD_DELAY = 0

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
}

# Configure item pipelines
ITEM_PIPELINES = {
    'crawler.pipelines.CrawlerPipeline': 300,
}

DB = {
    'user': 'root',
    'password': 'root',
    'host': 'spiegel_db',
    'name': 'crawler',
}

