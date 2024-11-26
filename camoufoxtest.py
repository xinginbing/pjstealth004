import random
from camoufox.sync_api import Camoufox

with Camoufox(
    geoip=True,
    proxy={
        'server': '89.38.98.115:12825'
    }) as browser:
    page = browser.new_page()
    page.goto("https://browserscan.net")
    random_time = random.randint(35, 50)
    print("Wait " + str(random_time) + " Second!" )
    page.wait_for_timeout(random_time*1000)
    texts = page.locator('span').all()
    for t in texts:
        print(t.inner_text())
	  


















