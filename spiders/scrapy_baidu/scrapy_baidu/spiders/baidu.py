import scrapy
from scrapy_baidu.items import ScrapyBaiduItem
import re


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.baidu.com']

    def parse(self, response):
        # # 提取数据
        # title = "百度"
        # link = "链接"
        #
        # # 实例化 Item 并填充数据
        # for i in range(10):
        #     item = ScrapyBaiduItem()
        #     item['title'] = title
        #     item['link'] = link
        #     item['desc'] = "sdsdsddsdsd"
        #
        #     yield item

        _resHtml = response.text
        # print(_resHtml)
        # print(_resHtml)
        match = re.search(r'<!--s-data:(.*?)-->', _resHtml)
        if match:
            print(888888888888888888)
            json_str = match.group(1)
            json_res = json.loads(json_str)

            for card in json_res['data']['cards']:
                for k, v in enumerate(card['content']):
                    # temp_arr.append({
                    #     'index': k + 1,
                    #     'title': v['word'],
                    #     'desc': v['desc'],
                    #     'pic': v['img'],
                    #     'url': v['url'],
                    #     # 'hot': round(v['hotScore'] / 10000, 1) * 10000,  # Convert to '万' format
                    #     'mobilUrl': v['appUrl']
                    # })
                    print(k + 1, v['word'], v['desc'], v['img'], v['url'])
                    # yield ScrapyBaiduItem(temp_arr)
# scrapy crawl baidu
