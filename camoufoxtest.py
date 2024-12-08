import requests
import urllib.parse

token = "54e88bca11504c90b8a184e06c3d89ac7814f7e9a4d"
targetUrl = urllib.parse.quote("https://browserscan.net/")
#customHeaders = "true"
#payload = {}
device = 'mobile'
super = "true"
geoCode = "us"
customWait = "35000"
render = "true"
height = "720"
width = "1280"

blockResources = "false"
#url = "http://api.scrape.do?token={}&url={}&customHeaders={}".format(token, targetUrl, customHeaders)
url = "http://api.scrape.do?token={}&url={}&device={}&super={}&geoCode={}&customWait={}&render={}&height={}&width={}&blockResources={}".format(token, targetUrl, device, super, geoCode, customWait, render, height, width, blockResources)
#headers = {
#  'Test-Header-Key': 'TestValue',
#  "Sec-Ch-Ua-Mobile": "?1",
#  "Sec-Ch-Ua-Platform": "\"android\""
#}
#response = requests.request("GET", url, headers=headers, data=payload)
response = requests.request("GET", url)
print(response.text)











