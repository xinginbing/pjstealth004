import requests
import urllib.parse
import random

token = "54e88bca11504c90b8a184e06c3d89ac7814f7e9a4d"

link = "https://httpbin.co/anything"

targetUrl = urllib.parse.quote(link)

super = "true"

geoCode = "us"

#regionalGeoCode = "europe"
#asia 亚洲 europe 欧洲 africa 非洲  oceania 大洋洲 northamerica 北美 southamerica 南美洲  
sessionId = str(random.randint(2000, 4000))

timeout = "1200000"   # 5000 毫秒和 120000 毫秒

device = "mobile"   # desktop 和 mobile 

customWait = "35000"

render = "true"

height = "1280"
width = "720"

blockResources = "false"

forwardHeaders = "true"

payload = {}

url = "http://api.scrape.do?token={}&url={}".format(token, targetUrl, super, geoCode, sessionId, timeout, device, customWait, render, blockResources, forwardHeaders, height, width)

headers = {
  'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.81 Mobile Safari/537.36',
  'Test-Header-Key': 'TestValue'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
















