import pytest 
import pytest_asyncio
from playwright.async_api import async_playwright, Browser, Page


@pytest.mark.asyncio
async def test_login(page, test_data):
    await page.goto("https://practicesoftwaretesting.com/")
    sign_in_link =  await page.get_by_role("link", name="Sign in").click()
    email_input = await page.get_by_label("Email address").fill(test_data['email'])
    # password_input = await page.get_by_label("Password").fill(test_data['password'])
    password_input = await page.locator('[data-test="password"]').fill(test_data['password'])
    login_button = await page.get_by_role("button", name="Login").click() 
    user_name = await page.locator('[data-test="nav-menu"]').inner_text()
    assert test_data['user'] in user_name
    

    

    
