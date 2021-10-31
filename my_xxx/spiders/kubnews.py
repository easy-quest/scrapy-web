from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader.processors import TakeFirst
# from scrapy.loader import XPathItemLoader
# from scrapy.selector import HtmlXPathSelector
# from kubnews.items import KubnewsItem

class KubnewsSpider(CrawlSpider):
    name = 'kubnews'
    allowed_domains = ['www.kubnews.ru']
    start_urls = ['http://kubnews.ru/proisshestviya/']

    # rules = (
    #     Rule(SgmlLinkExtractor(allow=('act=home_reg', 'act=home_zone')), follow=True),
    #     Rule(SgmlLinkExtractor(allow=('act=home_more')), callback='parse_item'),
    # )

    def parse(self, response):
        pass
