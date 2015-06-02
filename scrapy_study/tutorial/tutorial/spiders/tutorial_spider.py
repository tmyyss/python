import scrapy
from tutorial.items import TutorialItem
class TutorialSpider(scrapy.Spider):
    name = "tutorial"
    allowed_domains = ["localhost"]
    start_urls = [
        #"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        #"http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
	'http://127.0.0.1:8000'
    ]

    def parse(self, response):
        print response.xpath('//div')
	    
            
