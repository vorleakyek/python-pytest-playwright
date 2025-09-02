# import re
# import pytest
# from playwright.async_api import Page, expect

# @pytest.mark.asyncio
# async def test_has_title(page: Page):
#     await page.goto("https://playwright.dev/")
#     await expect(page).to_have_title(re.compile("Playwright"))

import asyncio
from playwright.async_api import async_playwright

async def main():
   async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("http://google.com")
        await asyncio.sleep(5)
        await browser.close()

asyncio.run(main())