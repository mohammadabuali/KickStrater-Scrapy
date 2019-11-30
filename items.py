import scrapy


class ProjectsItem(scrapy.Item):
	project = scrapy.Field()  # list of items


class RewardItem(scrapy.Item):
	Text = scrapy.Field()
	Price = scrapy.Field()
	NumBackers = scrapy.Field()
	TotalPossibleBackers = scrapy.Field()


class KSProjectItem(scrapy.Item):
	id = scrapy.Field()
	currency = scrapy.Field()
	url = scrapy.Field()
	Creator = scrapy.Field()
	Title = scrapy.Field()
	Text = scrapy.Field()
	DollarsPledged = scrapy.Field()
	DollarsGoal = scrapy.Field()
	NumBackers = scrapy.Field()
	DaysToGo = scrapy.Field()
	AllOrNothing = scrapy.Field()
	Rewards = scrapy.Field()  # list of rewards
