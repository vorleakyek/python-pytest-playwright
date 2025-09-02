import asyncio
import pytest_asyncio
from playwright.async_api import async_playwright
import pytest
import json

@pytest.fixture
def test_data():
    with open('data.json', 'r') as f:
        return json.load(f)

@pytest_asyncio.fixture
async def browser():
    playwright = await async_playwright().start()
    browser = await playwright.chromium.launch(headless=False)
    yield browser
    # await asyncio.sleep(25)
    await browser.close()
    await playwright.stop()


@pytest_asyncio.fixture
async def page(browser):
    context = await browser.new_context()
    page = await context.new_page()
    yield page
    await context.close()



# import pytest
# from playwright.async_api import async_playwright, Page, Browser
# import pytest_asyncio

# def pytest_addoption(parser):
#     parser.addoption(
#         "--browser_name",
#         action="store",
#         default="chromium",
#         help="Browser selection: chromium, firefox, or webkit",
#         choices=("chromium", "firefox", "webkit")
#     )
#     parser.addoption(
#         "--headless",
#         action="store_true",
#         default=False,
#         help="Run browsers in headless mode"
#     )

# @pytest_asyncio.fixture(scope="session")
# async def browser(pytestconfig):
#     browser_name = pytestconfig.getoption("browser_name")
#     headless = pytestconfig.getoption("headless")  # centralized headless flag
#     playwright = await async_playwright().start()


#     browser_launch_map = {
#         "chromium": playwright.chromium.launch,
#         "firefox": playwright.firefox.launch,
#         "webkit": playwright.webkit.launch
#     }

#     browser = await browser_launch_map[browser_name](headless=False)
#     yield browser
#     await browser.close()
   

# @pytest_asyncio.fixture
# async def page(browser):
#     context = await browser.new_context()
#     page = await context.new_page()
#     yield page
#     await context.close()



# # import pytest_asyncio
# # from playwright.async_api import async_playwright

# # @pytest_asyncio.fixture
# # async def browser():
# #     playwright = await async_playwright().start()
# #     browser = await playwright.chromium.launch()
# #     yield browser
# #     await browser.close()
# #     await playwright.stop()

# # @pytest_asyncio.fixture
# # async def page(browser):
# #     context = await browser.new_context()
# #     page = await context.new_page()
# #     yield page
# #     await context.close()





# # # @pytest.fixture(scope="session")
# # # async def browser():
# # #     async with async_playwright() as p:
# # #         browser = await p.chromium.launch(headless=False)
# # #         yield browser
# # #         await browser.close()

# # # @pytest.fixture
# # # async def page(browser):
# # #     context = await browser.new_context()
# # #     page = await context.new_page()
# # #     yield page
# # #     await context.close()

# # def pytest_addoption(parser):
# #     parser.addoption(
# #         "--browser_name",
# #         action="store",
# #         default="chromium",
# #         help="Browser selection: chromium, firefox, or webkit",
# #         choices=("chromium", "firefox", "webkit")
# #     )
# #     parser.addoption(
# #         "--headless",
# #         action="store_true",
# #         default=False,
# #         help="Run browsers in headless mode"
# #     )