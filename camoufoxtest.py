from playwright.sync_api import sync_playwright 
from browserforge.injectors.playwright import NewContext
from browserforge.fingerprints import FingerprintGenerator
import random

fingerprint = FingerprintGenerator()
fingerprint.generate()

with sync_playwright() as playwright:
    browser = playwright.chromium.launch()
    # Create a new context with the injected fingerprint
    context = NewContext(browser, fingerprint=fingerprint)
    page = context.new_page()
    page.goto("https://browserscan.net")
    random_time = random.randint(35, 50)
    print("Wait " + str(random_time) + " Second！" )
    page.wait_for_timeout(random_time*1000)
    texts = page.locator('span').all()
    for t in texts:
        print(t.inner_text())
    browser.close()


















