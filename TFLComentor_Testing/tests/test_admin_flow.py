from playwright.sync_api import sync_playwright, expect
from pages.login_page import LoginPage
from pages.admin_dashboard_page import AdminDashboardPage

def test_admin_flow():
    with sync_playwright() as p:
        # 1. Open Chrome Browser
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()

        # 2. Open Website & Go to Login
        page.goto("http://localhost:8081/")
        page.locator("text=Sign In").click()
        page.wait_for_url("**/models/membership/Login")

        # 3. Perform Admin Login
        login_page = LoginPage(page)
        login_page.login(contact="7972542628", role="Admin", password="12345")
        print("Admin logged in successfully!")

        # 4. Verify Admin Dashboard
        page.wait_for_url("**/models/membership/dashboard")
        expect(page.locator("text=Hello, SAHIL KAMBLE")).to_be_visible()
        print("Admin Dashboard loaded successfully!")

        # 5. Open Assign Assessment Page
        dashboard_page = AdminDashboardPage(page)
        dashboard_page.click_assign_assessment_card()
        
        # 6. Fill Details and Assign Assessment
        page.wait_for_url("**/models/assign-assessment")
        dashboard_page.fill_and_assign_assessment(test_name="Python", student_name="sachin kharat")
        print("Assessment assigned successfully to sachin kharat!")

        # Keep browser open to verify
        input("Press ENTER to close browser...")
        browser.close()

if __name__ == "__main__":
    test_admin_flow()