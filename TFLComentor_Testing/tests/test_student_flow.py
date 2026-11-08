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
        expect(page.locator("text=Hello, Sachin Kharat (Student)")).to_be_visible()
        print("Student Dashboard loaded successfully!")

        # 5. Handle Upcoming Assessment click
        student_dashboard = StudentDashboardPage(page)
        
        try:
            # प्रथम Upcoming Assessments कार्डवर क्लिक करण्याचा प्रयत्न
            page.locator("text=Upcoming Assessments").click(force=True)
            print("Clicked on 'Upcoming Assessments' successfully!")
        except Exception as e:
            print("Trying to click via notification...", e)
            try:
                # जर कार्डवर क्लिक नाही झाले, तर नोटिफिकेशनवर क्लिक करणे
                page.locator("text=Assessment Scheduled").first.click(force=True)
                print("Clicked on Assessment Notification successfully!")
            except Exception as ex:
                print("Click failed:", ex)

        # Keep browser open to verify
        input("Press ENTER to close browser...")
        browser.close()

if __name__ == "__main__":
    test_student_assessment_flow()