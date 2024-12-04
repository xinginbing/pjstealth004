from scrapingbee import ScrapingBeeClient
import random


url = 'https://t.co/CQDM8aFMYH'
key = 'NP3Q403JMJFWI0VMW1GIHIYY45MM58KJFQCKFFM25XELQSE6EQ2WRHVALN68DBSPDDDQJWK0JG6P2I7O'
id = str(random.randint(20000, 25000))

client = ScrapingBeeClient(api_key=key)

response = client.get(url,
    params = { 
        #等待时间 0 到 35000
        'wait': '35000', 
        'premium_proxy': 'True',
        #修改国家
        'country_code': 'us',
        #所有使用相同session_id API 请求将通过相同的 IP 地址进行路由，持续时间为5 分钟，id 使用 0 到 10,000,000
        'session_id': id,
        #选择将请求发送到服务器的设备类型。只有两个选项可用： desktop （默认）和mobile 。
        'device': 'mobile',
        'block_resources': 'False',
        'js_scenario': {
	    "instructions": [
		{"scroll_y": 100},
		{"wait": 5000},
		{"scroll_y": 1000},
		{"wait": 8000},
	    ]
	},
    }

)

print('Response HTTP Status Code: ', response.status_code)
print('Response HTTP Response Body: ', response.content)

















