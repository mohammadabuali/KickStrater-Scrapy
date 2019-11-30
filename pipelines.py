import re
from urllib.parse import quote
import os
import scrapy


def clean_file_name(url: str):
	name = url.split('/')[~0]
	return re.sub(r'[\\/:*\"<>|]', '', name)


class ScreenshotsPipeline(object):
	"""Pipeline that uses Splash to render screenshot of
	every Scrapy item.
	Require Splash installed and running
	(sudo docker pull scrapinghub/splash && sudo docker run -it -p 8050:8050 --rm scrapinghub/splash)
	"""

	SPLASH_URL = "http://localhost:8050/render.png?url={}&wait=5&render_all=1&wait=5"

	def process_item(self, item, spider):
		encoded_item_url = quote(item["url"])
		screenshot_url = self.SPLASH_URL.format(encoded_item_url)
		request = scrapy.Request(screenshot_url)
		dfd = spider.crawler.engine.download(request, spider)
		dfd.addBoth(self.return_item, item)
		return dfd

	def return_item(self, response, item):
		if response.status != 200:
			# Error happened, return item.
			return item

		folder = 'data/screenshots'
		if not os.path.isdir(folder):
			os.mkdir(folder)
		url = item["url"]
		filename = f"{folder}/{clean_file_name(url)}.png"
		with open(filename, "wb") as f:
			f.write(response.body)
		return item
