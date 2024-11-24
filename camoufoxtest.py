from patchright.sync_api import sync_playwright
from pjstealth import stealth_sync
import random

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page(
    user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    proxy=proxy)
    stealth_sync(page)
    page.goto("https://browserscan.net")
    random_time = random.randint(35, 50)
    print("Wait " + str(random_time) + " Second！" )
    page.wait_for_timeout(random_time*1000)
    texts = page.locator('span').all()
    for t in texts:
        print(t.inner_text())
    browser.close()
