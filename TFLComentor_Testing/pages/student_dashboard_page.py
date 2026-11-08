from playwright.sync_api import Page

class StudentDashboardPage:
    def __init__(self, page: Page):
        self.page = page
        
        # डॅशबोर्डवरील 'Upcoming Assessments' कार्ड आणि नोटिफिकेशन
        self.upcoming_assessments_card = page.locator("text=Upcoming Assessments")
        self.assessment_notification = page.locator("text=Assessment Scheduled")

    def click_upcoming_assessments(self):
        """'Upcoming Assessments' कार्डवर फोर्सफुली क्लिक करते"""
        if self.upcoming_assessments_card.is_visible():
            self.upcoming_assessments_card.click(force=True)

    def click_assessment_notification(self):
        """Recent Notifications मधील असेसमेंटवर क्लिक करते"""
        if self.assessment_notification.is_visible():
            self.assessment_notification.first.click(force=True)