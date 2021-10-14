import scrapy


class KubnewsSpider(scrapy.Spider):
    name = 'kubnews'
    allowed_domains = ['kubnews.ru']
    start_urls = ['http://kubnews.ru/proisshestviya/']

    def parse(self, response):
        pass
