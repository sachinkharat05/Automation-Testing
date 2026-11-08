
from playwright.sync_api import sync_playwright


def test_login(base_url):

    with sync_playwright() as p:

        browser = p.chromium.launch( headless=False,slow_mo=1000)
        page = browser.new_page()
        page.goto(base_url)

        # Registration
        page.locator('input[name="username"]' ).nth(0).fill("Sachin")
        page.locator('input[name="email"]').fill("sachin@gmail.com")
        page.locator('input[name="password"]' ).nth(0).fill("Sachin123")
        page.get_by_role("button",name="Register").click()

        assert page.get_by_text("Registration Successful").is_visible()
        # Login
        page.locator('input[name="username"]').nth(1).fill("Sachin")
        page.locator('input[name="password"]').nth(1).fill("Sachin123")
        page.get_by_role( "button", name="Login").click()

        assert page.get_by_text("Login Successful" ).is_visible()
        print("Login Test Passed")

        # Keep browser open
        input("Press ENTER to close browser...")
        browser.close()
