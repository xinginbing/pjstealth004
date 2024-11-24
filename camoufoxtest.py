import asyncio
import random
import botright


async def main():
    botright_client = await botright.Botright()
    browser = await botright_client.new_browser()
    page = await browser.new_page()

    # Continue by using the Page
    await page.goto("https://browserscan.net")
    random_time = random.randint(35, 50)
	print("Wait " + str(random_time) + " Second！" )
    await page.wait_for_timeout(random_time*1000)
    texts = page.locator('span').all()
    for t in texts:
        print(t.inner_text())
    await botright_client.close()


if __name__ == "__main__":
    asyncio.run(main())
