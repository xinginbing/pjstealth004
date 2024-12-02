import random
import requests

url = 'https://125700.shop/ecdd30e7e8f019717fb8/2643f1413f/?placementName=default'
apikey = '9ff6d18370ad67f79b0193ccf8c9145bc608a3b9'
time = str(random.randint(15, 30) * 1000)
id = str(random.randint(20000, 25000))
params = {
    'url': url,
    'apikey': apikey,
    'js_render': 'true',
    'premium_proxy': 'true',
    'proxy_country': 'us',
    'wait': time,            #最大30000
    'session_id': id,
}
response = requests.get('https://api.zenrows.com/v1/', params=params)
print('Response HTTP Status Code: ', response.status_code)
print(response.text)
	  


















