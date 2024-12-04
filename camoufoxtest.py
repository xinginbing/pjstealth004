import requests
from pprint import pprint


# Structure payload.
payload = {
    "source": "universal", 
    "url": "https://luglawhaulsano.net/4/8605030", 
    "user_agent_type": "mobile_android",    
# desktop_chrome   desktop_chrome   desktop_firefox   desktop_opera  desktop_safari  mobile  mobile_android  mobile_ios  tablet   tablet_android  tablet_ios
    "geo_location": "United States",
    "render": "html",
    "context": [
        {
            "key": "follow_redirects",
            "value": True
        },
        {
            "key": "http_method", "value": "get"
        }]
    
}

# Get response.
response = requests.request(
    'POST',
    'https://realtime.oxylabs.io/v1/queries',
    auth=('lje024_hTJli', 'xiaobai024A002+'),
    json=payload,
)

# Instead of response with job status and results url, this will return the
# JSON response with the result.
pprint(response.json())

















