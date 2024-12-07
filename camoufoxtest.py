import requests
import urllib.parse

token = "54e88bca11504c90b8a184e06c3d89ac7814f7e9a4d"
targetUrl = urllib.parse.quote("https://httpbin.co/headers")
customHeaders = "true"
payload = {}
url = "http://api.scrape.do?token={}&url={}&customHeaders={}".format(token, targetUrl, customHeaders)
headers = {
  'Test-Header-Key': 'TestValue'
}
response = requests.request("GET", url, headers=headers, data=payload)
print(response.text)











