from playwright.sync_api import sync_playwright, expect
from pages.login_page import LoginPage
from pages.sme_dashboard_page import SMEDashboardPage
from pages.admin_dashboard_page import AdminDashboardPage
from pages.student_dashboard_page import StudentDashboardPage

def test_complete_end_to_end_workflow():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto("http://localhost:8081/")

        print("\n================ STEP 1: SME FLOW ================")
        page.locator("text=Sign In").click()
        page.wait_for_url("**/models/membership/Login")
        
        login_page = LoginPage(page)
        login_page.login(contact="7972520102", role="SME", password="12345")
        
        page.wait_for_url("**/models/membership/dashboard")
        expect(page.get_by_text("SME Dashboard", exact=True)).to_be_visible()
        
        sme_dashboard = SMEDashboardPage(page)
        sme_dashboard.click_tests_created()
        
        page.wait_for_url("**/models/created-assessments")
        sme_dashboard.click_create_test_button()
        
        page.wait_for_url("**/models/create-test")
        sme_dashboard.fill_and_create_test(
            test_name="Python",
            difficulty="BEGINNER",
            description="oops concept",
            duration="5"
        )
        
        page.wait_for_url("**/models/question-options")
        sme_dashboard.click_select_questions_button()
        sme_dashboard.select_questions_and_save()
        print("✅ SME Flow Completed Successfully!")

        page.goto("http://localhost:8081/")

        print("\n================ STEP 2: ADMIN FLOW ================")
        page.locator("text=Sign In").click()
        page.wait_for_url("**/models/membership/Login")
        
        login_page.login(contact="7972542628", role="Admin", password="12345")
        
        page.wait_for_url("**/models/membership/dashboard")
        expect(page.get_by_text("Admin Dashboard", exact=False)).to_be_visible()

        admin_dashboard = AdminDashboardPage(page)
        admin_dashboard.click_assign_assessment_card()
        
        page.wait_for_url("**/models/assign-assessment")
        admin_dashboard.fill_and_assign_assessment(student_name="sachin kharat")
        admin_dashboard.click_ok_button()
        print("✅ Admin Flow Completed Successfully!")

        page.goto("http://localhost:8081/")

        print("\n================ STEP 3: STUDENT FLOW ================")
        page.locator("text=Sign In").click()
        page.wait_for_url("**/models/membership/Login")
        
        login_page.login(contact="9637661382", role="Student", password="12345")
        
        page.wait_for_url("**/models/membership/dashboard")
        expect(page.get_by_text("Hello, Sachin Kharat (Student)", exact=True)).to_be_visible()

        student_dashboard = StudentDashboardPage(page)
        student_dashboard.click_upcoming_assessments()
        
        page.wait_for_url("**/models/upcoming-assessment")
        student_dashboard.click_start_assessment()
        
        page.wait_for_url("**/models/assessment/start/**")
        student_dashboard.complete_all_five_questions()
        print("✅ Student Flow Completed Successfully!")

        print("\n🎉 ALL E2E STEPS PASSED SUCCESSFULLY! 🎉")
        input("Press ENTER to close browser...")
        browser.close()

if __name__ == "__main__":
    test_complete_end_to_end_workflow()