from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.loader.processor import TakeFirst
from scrapy.contrib.loader import XPathItemLoader
from scrapy.selector import HtmlXPathSelector
from kubnews.items import KubnewsItem

class KubnewsSpider(scrapy.Spider):
    name = 'kubnews'
    allowed_domains = ['kubnews.ru']
    start_urls = ['http://kubnews.ru/proisshestviya/']

    def parse(self, response):
        pass
