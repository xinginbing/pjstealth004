import requests
import urllib.parse

token = "54e88bca11504c90b8a184e06c3d89ac7814f7e9a4d"
targetUrl = urllib.parse.quote("https://httpbin.co/headers")
#customHeaders = "true"
#payload = {}
device = 'mobile'
#url = "http://api.scrape.do?token={}&url={}&customHeaders={}".format(token, targetUrl, customHeaders)
url = "http://api.scrape.do?token={}&url={}&device={}".format(token, targetUrl, device)
#headers = {
#  'Test-Header-Key': 'TestValue',
#  "Sec-Ch-Ua-Mobile": "?1",
#  "Sec-Ch-Ua-Platform": "\"android\""
#}
#response = requests.request("GET", url, headers=headers, data=payload)
response = requests.request("GET", url)
print(response.text)











