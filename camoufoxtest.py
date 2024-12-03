import time
import random
import requests

isStop = 1
url = 'https://browserscan.net'
zenkey = '9ff6d18370ad67f79b0193ccf8c9145bc608a3b9'

while isStop > 0:

    waittime = str(random.randint(15, 30) * 1000)
    id = str(random.randint(20000, 25000))
    countrylist =['nl','sg','us','gb','ca','nl','us','th','ca','my','us','my','gb','nl','fr','th','in','vn','jp','ph','id','us','hk','us','hk','au','my','fr','us','au','nz','hk','us','nz','vn','th','gb','sg','kr','ph','gb','jp','kr','us','ca','sg','sg','it','in','es','id','es','au','gb','us','gb','th','ph','jp','tw','sg','my','gb','sg','es','au','id','jp','jp','tw','jp','au','vn','in','jp','vn','au','jp','sg','sg','ph','ca','jp','jp','id','sg','fr','au','de','it','us','jp','th','us','gb','au','fr','us','nz','jp','my','ca','us','id','ca','de','jp','id','sg','tw','au','kr','gb','ch','au','jp','jp','nl','us','kr','sg','ch','us','nz','th','jp','jp','us','it','tw','it','kr','ca','kr','tw','de','us','nl','ch','nz','my','ph','au','jp','th','ch','my','au','vn','tw','us','nz','jp','in','kr','jp','de','au','tw','de','au','sg','my','sg','au','au','my','nz','in','au','ph','id','sg','ph','jp','ca','sg','nz','kr','it','vn','kr','au','hk','us','my','sg','nl','vn','nz','ca','tw','kr','nl','us','kr','nl','in','ch','au','nl','hk','ch','fr','ch','nl','tw','ca','ch','vn']
    geo = countrylist[random.randint(0, 209)]

    params = {
        'url': url,
        'apikey': zenkey,
        'js_render': 'true',
        'premium_proxy': 'true',
        'proxy_country': geo,
        'wait': waittime,            #最大30000
        'session_id': id,
        'screenshot_fullpage': 'true',
		'block_resources': 'none',
    }
    response = requests.get('https://api.zenrows.com/v1/', params=params)
    print(geo)
    print('Response HTTP Status Code: ', response.status_code)
    print(response.text)
#    if int(response.status_code) != 200:
#	    isStop = isStop - 1
#	time.sleep(5)	
    isStop = isStop - 1	

















