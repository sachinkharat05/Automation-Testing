from playwright.sync_api import Page

class AdminDashboardPage:
    def __init__(self, page: Page):
        self.page = page
        
        # 1. Admin डॅशबोर्डवरील 'Assign Assessment' कार्ड
        self.assign_assessment_card = page.locator("text=Assign Assessment")
        
        # 2. Assign Assessment फॉर्ममधील इनपुट फिल्ड्स आणि बटणे
        self.test_input = page.locator("input[type='text']").nth(0)  # Select Test input
        self.student_input = page.locator("input[type='text']").nth(1)  # Select Students input
        self.assigned_status_button = page.get_by_role("button", name="Assigned")  # Status: Assigned
        self.assign_assessment_submit_button = page.get_by_role("button", name="Assign Assessment")  # Submit Button

    def click_assign_assessment_card(self):
        """'Assign Assessment' कार्डवर क्लिक करते"""
        self.assign_assessment_card.click()

    def fill_and_assign_assessment(self, test_name: str, student_name: str):
        """टेस्ट नाव, विद्यार्थ्याचे नाव भरून फॉर्म सबमिट करते"""
        # Test चे नाव टाकणे
        self.test_input.fill(test_name)
        
        # विद्यार्थ्याचे नाव टाकणे
        self.student_input.fill(student_name)
        
        # 'Assigned' स्टेटस सिलेक्ट करणे
        if self.assigned_status_button.is_visible():
            self.assigned_status_button.click()
            
        # 'Assign Assessment' बटणावर क्लिक करणे
        self.assign_assessment_submit_button.click()