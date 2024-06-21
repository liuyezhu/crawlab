import requests
import re
import json
from datetime import datetime


def baiduredian():
    url = 'https://top.baidu.com/board?tab=realtime'
    response = requests.get(url)
    _resHtml = response.text.replace('\n', '').replace('\r', '').replace(' ', '')

    match = re.search(r'<!--s-data:(.*?)-->', _resHtml)
    if match:
        json_str = match.group(1)
        json_res = json.loads(json_str)

        temp_arr = []
        for card in json_res['data']['cards']:
            for k, v in enumerate(card['content']):
                temp_arr.append({
                    'index': k + 1,
                    'title': v['word'],
                    'desc': v['desc'],
                    'pic': v['img'],
                    'url': v['url'],
                    # 'hot': round(v['hotScore'] / 10000, 1) * 10000,  # Convert to '万' format
                    'mobilUrl': v['appUrl']
                })

        return {
            'success': True,
            'title': '百度热点',
            'subtitle': '指数',
            'update_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'data': temp_arr
        }
    else:
        return {
            'success': False,
            'error': 'Failed to find the data in the response'
        }


# Example usage
result = baiduredian()
print(result)
