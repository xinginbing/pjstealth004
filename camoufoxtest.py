import requests

url = 'https://125700.shop/ecdd30e7e8f019717fb8/2643f1413f/?placementName=default'
apikey = '9ff6d18370ad67f79b0193ccf8c9145bc608a3b9'
params = {
    'url': url,
    'apikey': apikey,
	'js_render': 'true',
	'premium_proxy': 'true',
	'proxy_country': 'us',
	'wait': '35000',
	'session_id': '22345',
}
response = requests.get('https://api.zenrows.com/v1/', params=params)
print(response.text)
	  


















