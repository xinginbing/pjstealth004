import random
from camoufox.sync_api import Camoufox

with Camoufox(
    geoip=True,
    proxy={
        'server': 'http://136.243.174.185:9999',
        'username': '4zylzn2nea-corp.mobile.res-country-RU-state-479119-city-541722-hold-session-session-67481517caddf',
        'password': '0EF1FRQg9N9G3c8G'
    }) as browser:
    page = browser.new_page()
    page.goto("https://browserscan.net")
    random_time = random.randint(35, 50)
    print("Wait " + str(random_time) + " Second!" )
    page.wait_for_timeout(random_time*1000)
    texts = page.locator('span').all()
    for t in texts:
        print(t.inner_text())
	  


















