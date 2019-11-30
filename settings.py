# Scrapy settings for kick_starter scraper project

BOT_NAME = 'KickStarter'

SPIDER_MODULES = ['kick_starter.spiders']
NEWSPIDER_MODULE = 'kick_starter.spiders'

ITEMS_LIMIT = 300
TEXT_ALL_HTML = False

ROBOTSTXT_OBEY = True

DOWNLOAD_DELAY = 3

CONCURRENT_REQUESTS = 1

FEED_EXPORT_INDENT = 4
FEED_STORE_EMPTY = True
FEED_FORMAT = "json"
FEED_URI = 'data/kickstarter.json'
FEED_OVERWRITE_FILE = True
FEED_EXPORTERS_BASE = {
	'json': 'kick_starter.exporters.CumulativeJsonExporter'
}

ITEM_PIPELINES = {
	# 'kick_starter.pipelines.ScreenshotsPipeline': 1,  # uncomment to take screenshots of visited projects
}
