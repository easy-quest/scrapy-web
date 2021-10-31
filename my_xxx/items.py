# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class MyXxxItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id               = Field()
    region           = Field()
    district         = Field()
    type             = Field()
    name             = Field()
    post             = Field()
    phone            = Field()
    director         = Field()
    bank             = Field()
    parent           = Field()
    foundation       = Field()
    activities       = Field()
    history          = Field()
    staff            = Field()
    publications     = Field()
    children         = Field()
    age              = Field()
    orphans          = Field()
    deviated         = Field()
    principle        = Field()
    education        = Field()
    treatment        = Field()
    holidays         = Field()
    communication    = Field()
    buildings        = Field()
    vehicles         = Field()
    farming          = Field()
    working_cabinet  = Field()
    library          = Field()
    computers        = Field()
    toys             = Field()
    patronage        = Field()
    needs            = Field()
    volunteers       = Field()
    url              = Field()