# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Article(scrapy.Item):
    title = scrapy.Field()
    location = scrapy.Field()
    text = scrapy.Field()
    source = scrapy.Field()
    source_url = scrapy.Field()
    date = scrapy.Field()
