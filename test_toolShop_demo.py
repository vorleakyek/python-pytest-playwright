import pytest 
import pytest_asyncio
from playwright.async_api import async_playwright, Browser, Page, expect


@pytest.mark.asyncio
async def test_login(page, test_data):
    # Login and verify the user name is displayed 
    await page.goto("https://practicesoftwaretesting.com/")
    await page.get_by_role("link", name="Sign in").click()
    await page.get_by_label("Email address").fill(test_data['email'])
    await page.locator('[data-test="password"]').fill(test_data['password'])
    await page.get_by_role("button", name="Login").click() 
    await page.locator('[data-test="nav-menu"]').inner_text()
    await expect(page.locator('[data-test="nav-menu"]')).to_contain_text(test_data['user'])

    # click on the logo to go back to the main page
    await page.locator('nav a[title="Practice Software Testing - Toolshop"]').click()  

    # Search for a plier 
    await page.locator('[data-test="search-query"]').fill(test_data['search-term'])
    await page.locator('[data-test="search-submit"]').click() 

    # Select the item with name "Pliers" 
    await page.wait_for_load_state("networkidle")
    search_result_links = page.locator('div[data-test="search_completed"] a')    
    count = await search_result_links.count()

    for i in range(count):
        product_link = search_result_links.nth(i)
        product_name = await product_link.locator('[data-test="product-name"]').inner_text()
        print(product_name)
        
        if product_name.lower().strip() == test_data['product-name-selected'].strip().lower():
            await product_link.click()
            break  # Optional: stop after clicking the first match
    
    product_name_header = await page.locator('[data-test="product-name"]').inner_text()
    product_name_header_lower_case = product_name_header.lower().strip()

    assert product_name_header_lower_case == test_data['product-name-selected'] 


    
    

    

    
