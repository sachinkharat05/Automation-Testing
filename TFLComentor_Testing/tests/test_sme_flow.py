from playwright.sync_api import sync_playwright, expect
from pages.login_page import LoginPage
from pages.sme_dashboard_page import SMEDashboardPage

def test_sme_complete_flow():
    with sync_playwright() as p:
        # 1. Open Chrome browser
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()

        # 2. Open Website & Go to Login
        page.goto("http://localhost:8081/")
        page.locator("text=Sign In").click()
        page.wait_for_url("**/models/membership/Login")

        # 3. Perform Login as SME (Credentials: 7972520102 / 12345)
        login_page = LoginPage(page)
        login_page.login(contact="7972520102", role="SME", password="12345")
        print("SME logged in successfully!")

        # 4. Verify SME Dashboard
        page.wait_for_url("**/models/membership/dashboard")
        expect(page.get_by_text("SME Dashboard", exact=False)).to_be_visible()
        expect(page.get_by_text("Nirjala Naik", exact=False)).to_be_visible()
        print("SME Dashboard loaded successfully!")

        # 5. Click on 'Tests Created' card
        sme_dashboard = SMEDashboardPage(page)
        sme_dashboard.click_tests_created()
        print("Clicked on 'Tests Created' card successfully!")

        # 6. Click on '+ Create Test' button
        page.wait_for_url("**/models/created-assessments")
        sme_dashboard.click_create_test_button()
        print("Navigated to Create New Test page successfully!")

        # 7. Fill the New Test Form and Submit
        page.wait_for_url("**/models/create-test")
        sme_dashboard.fill_and_create_test(
            test_name="Python",
            difficulty="BEGINNER",
            description="oops concept",
            duration="5"
        )
        print("New Test created successfully!")

        # 8. Click 'Select Questions' button on Question Setup page
        page.wait_for_url("**/models/question-options")
        sme_dashboard.click_select_questions_button()
        print("Clicked on 'Select Questions' button successfully!")

        # 9. Select questions from the list
        sme_dashboard.select_questions_and_save()
        print("Questions selected and SME flow completed successfully!")

        # Keep browser open to verify
        input("Press ENTER to close browser...")
        browser.close()

if __name__ == "__main__":
    test_sme_complete_flow()