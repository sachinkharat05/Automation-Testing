from playwright.sync_api import sync_playwright, expect
from pages.login_page import LoginPage
from pages.student_dashboard_page import StudentDashboardPage

def test_student_assessment_flow():
    with sync_playwright() as p:
        # 1. Open Chrome browser
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()

        # 2. Open Website & Go to Login
        page.goto("http://localhost:8081/")
        page.locator("text=Sign In").click()
        page.wait_for_url("**/models/membership/Login")

        # 3. Perform Login as Student
        login_page = LoginPage(page)
        login_page.login(contact="9637661382", role="Student", password="12345")
        print("Student logged in successfully!")

        # 4. Verify Student Dashboard
        page.wait_for_url("**/models/membership/dashboard")
        expect(page.get_by_text("Hello, Sachin Kharat (Student)", exact=True)).to_be_visible()
        print("Student Dashboard loaded successfully!")

        # 5. Click on 'Upcoming Assessments' card
        student_dashboard = StudentDashboardPage(page)
        student_dashboard.click_upcoming_assessments()
        print("Clicked on 'Upcoming Assessments' card successfully!")

        # 6. Click 'Start' button on Upcoming Assessments page
        page.wait_for_url("**/models/upcoming-assessment")
        student_dashboard.click_start_assessment()
        print("Clicked on 'Start' assessment button successfully!")

        # 7. Answer all 5 questions sequentially and Submit
        page.wait_for_url("**/models/assessment/start/**")
        student_dashboard.complete_all_five_questions()
        print("All 5 questions answered and assessment submitted successfully!")

        # Keep browser open to verify results page
        input("Press ENTER to close browser...")
        browser.close()

if __name__ == "__main__":
    test_student_assessment_flow()