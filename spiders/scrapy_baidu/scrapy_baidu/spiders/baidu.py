import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.baidu.com']
    print("sdddddddddddddddddddddddddddddddddddddddddd")

    def parse(self, response):
        print("sdddddddddddddddddddddddddddddddddddddddddd")
        # 根据实际页面结构调整XPath选择器
        news_hot_search_list_selector = '//*[@id="s_xmancard_news_new"]/div/div[1]/div/div/ul/li'

        # 提取新闻热搜列表
        for item in response.xpath(news_hot_search_list_selector):
            print(99898)
            print("sdds")

# 运行爬虫
# scrapy crawl baidu