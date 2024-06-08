import scrapy


class GoerSperSpider(scrapy.Spider):
    name = "goer_sper"
    allowed_domains = ["www.topgoer.com"]
    start_urls = ["https://www.topgoer.com"]

    def parse(self, response):
        for item in response.xpath('/html/body/div/div[1]/nav/ul/li'):
            title = item.xpath('./a/text()').extract_first()
            print(title)
        pass
