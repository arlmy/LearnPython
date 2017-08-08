import scrapy

class BaiduSpider(scrapy.Spider):
    name = 'bing.com'
    allowed_domains = ['www.bing.com']
    
