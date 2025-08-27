import re
from playwright.sync_api import Page, expect

# Test Login
def test_login(page: Page):
    page.goto("https://practicesoftwaretesting.com/")
    expect(page).to_have_title(re.compile("practice software test", re.IGNORECASE))
    sign_in_link = page.locator('[data-test="nav-sign-in"]')
    sign_in_link.click()



