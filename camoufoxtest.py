import requests
import urllib.parse
import random

isStop = 10
countrylist =['nl','sg','us','gb','ca','nl','us','th','ca','my','us','my','gb','nl','fr','th','in','vn','jp','ph','id','us','hk','us','hk','au','my','fr','us','au','nz','hk','us','nz','vn','th','gb','sg','kr','ph','gb','jp','kr','us','ca','sg','sg','it','in','es','id','es','au','gb','us','gb','th','ph','jp','tw','sg','my','gb','sg','es','au','id','jp','jp','tw','jp','au','vn','in','jp','vn','au','jp','sg','sg','ph','ca','jp','jp','id','sg','fr','au','de','it','us','jp','th','us','gb','au','fr','us','nz','jp','my','ca','us','id','ca','de','jp','id','sg','tw','au','kr','gb','ch','au','jp','jp','nl','us','kr','sg','ch','us','nz','th','jp','jp','us','it','tw','it','kr','ca','kr','tw','de','us','nl','ch','nz','my','ph','au','jp','th','ch','my','au','vn','tw','us','nz','jp','in','kr','jp','de','au','tw','de','au','sg','my','sg','au','au','my','nz','in','au','ph','id','sg','ph','jp','ca','sg','nz','kr','it','vn','kr','au','hk','us','my','sg','nl','vn','nz','ca','tw','kr','nl','us','kr','nl','in','ch','au','nl','hk','ch','fr','ch','nl','tw','ca','ch','vn']
token = "54e88bca11504c90b8a184e06c3d89ac7814f7e9a4d"

link = "https://luglawhaulsano.net/4/8605030"

targetUrl = urllib.parse.quote(link)

super = "true"
timeout = "120000"   # 5000 毫秒和 120000 毫秒

device = "mobile"   # desktop 和 mobile 
customWait = "35000"
render = "true"
height = "1280"
width = "720"
blockResources = "false"

while isStop > 0:
    geoCode = countrylist[random.randint(0, 209)]

#regionalGeoCode = "europe"
#asia 亚洲 europe 欧洲 africa 非洲  oceania 大洋洲 northamerica 北美 southamerica 南美洲  
    sessionId = str(random.randint(2000, 4000))

    url = "http://api.scrape.do?token={}&url={}&super={}&geoCode={}&sessionId={}&timeout={}&device={}&customWait={}&render={}&blockResources={}&height={}&width={}".format(token, targetUrl, super, geoCode, sessionId, timeout, device, customWait, render, blockResources, height, width)
#url = "http://api.scrape.do?token={}&url={}&geoCode={}&sessionId={}&timeout={}&device={}&customWait={}&render={}&blockResources={}&height={}&width={}".format(token, targetUrl, geoCode, sessionId, timeout, device, customWait, render, blockResources, height, width)
    response = requests.request("GET", url)

    print(response.text)
    if int(response.status_code) != 200:
	      isStop = isStop - 1
    time.sleep(5)
















