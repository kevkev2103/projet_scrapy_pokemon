# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PokemonscraperItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    pass

class PokemonItem(scrapy.Item):
    url=scrapy.Field()
    name=scrapy.Field()
    price=scrapy.Field()