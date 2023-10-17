import scrapy


class DigikeyspiderSpider(scrapy.Spider):
    name = "digikeySpider"
    start_urls = ["https://www.digikey.co.uk/product-detail/sitemap.xml"]

    def parse(self, response):
        urls = response.xpath("//div[@class='opened']")
        for i in urls:
            print(i)
            print('=='*20)

