import os

from scrapy.exporters import BaseItemExporter
from scrapy.utils.python import to_bytes
from scrapy.utils.serialize import ScrapyJSONEncoder

from kick_starter import settings
from kick_starter.items import ProjectsItem

items = []


class CumulativeJsonExporter(BaseItemExporter):
	"""
	Saves all the items in a list and export then at once when finished
	"""
	def __init__(self, file, **kwargs):
		super()._configure(kwargs, dont_fail=True)
		self.file = file
		self.kwargs = kwargs

		json_indent = self.indent if self.indent is not None and self.indent > 0 else None
		kwargs.setdefault('indent', json_indent)
		kwargs.setdefault('ensure_ascii', not self.encoding)
		self.encoder = ScrapyJSONEncoder(**kwargs)

		self.first_item = True

	def _beautify_newline(self):
		if self.indent is not None:
			self.file.write(b'\n')

	def start_exporting(self):
		if settings.FEED_OVERWRITE_FILE:
			self.file.close()
			os.remove(self.file.name)
			self.file = open(self.file.name, 'ab')

	def finish_exporting(self):
		items.sort(key=lambda item: int(item['id']))
		self._export_item({"projects": ProjectsItem(project=items)})

	def export_item(self, item):
		items.append(item)
		print(f'\rProgress: {len(items)}/{settings.ITEMS_LIMIT}', end='', flush=True)

	def _export_item(self, item):
		if self.first_item:
			self.first_item = False
		else:
			self.file.write(b',')
			self._beautify_newline()
		item_dict = dict(self._get_serialized_fields(item))
		data = self.encoder.encode(item_dict)
		self.file.write(to_bytes(data, self.encoding))

