# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BettingItem(scrapy.Item):
    # define the fields for your item here like:
    state = scrapy.Field()
    status = scrapy.Field()
    


    def __repr__(self):
        """only print out title after exiting the Pipeline"""
        #return repr({"title": self['title']})
        pass