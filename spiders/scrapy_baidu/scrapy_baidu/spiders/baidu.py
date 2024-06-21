import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.baidu.com']
    print("sdddddddddddddddddddddddddddddddddddddddddd")

    def parse(self, response):
        print("baidu4555555555555555555555555555555555555555555555555555555")
        # 根据实际页面结构调整XPath选择器
        t = response.xpath('//*[@id="lm-new"]/a/span').extract_first()
        print(t)
        print(11)

# 运行爬虫
# scrapy crawl baidu