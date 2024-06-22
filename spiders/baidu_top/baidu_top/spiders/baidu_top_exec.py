import scrapy
import re
import json

from baidu_top.items import BaiduTopItem


class BaiduTopExecSpider(scrapy.Spider):4
    name = "baidu_top_exec"
    allowed_domains = ["top.baidu.com"]
    start_urls = ["https://top.baidu.com/board?tab=realtime"]

    def parse(self, response):
        _resHtml = response.text.replace('\n', '').replace('\r', '').replace(' ', '')
        match = re.search(r'<!--s-data:(.*?)-->', _resHtml)
        if match:
            json_str = match.group(1)
            json_res = json.loads(json_str)
            for card in json_res['data']['cards']:
                for k, v in enumerate(card['content']):
                    yield {
                        'index': k + 1,
                        'title': v['word'],
                        'desc': v['desc'],
                        'pic': v['img'],
                        'url': v['url'],
                        'mobilUrl': v['appUrl']
                    }
        # scrapy crawl baidu
        pass
