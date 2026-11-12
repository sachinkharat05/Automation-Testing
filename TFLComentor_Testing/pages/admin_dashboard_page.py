from playwright.sync_api import Page, TimeoutError

class AdminDashboardPage:
    def __init__(self, page: Page):
        self.page = page
        
        self.assign_assessment_card = page.get_by_text("Assign Assessment", exact=True)
        
        self.python_test_radio = page.locator("input[type='radio']").first
        self.student_search_input = page.locator("input[placeholder*='Search'], input[type='text']").nth(1)
        self.student_checkbox = page.get_by_text("Sachin Kharat", exact=True)
        self.assigned_status_button = page.get_by_role("button", name="Assigned")
        self.assign_assessment_submit_button = page.get_by_role("button", name="Assign Assessment")
        
        self.ok_button = page.locator("button:has-text('OK')").first

    def click_assign_assessment_card(self):
        try:
            self.assign_assessment_card.scroll_into_view_if_needed()
            self.assign_assessment_card.click(force=True)
        except Exception as e:
            print(f"Error clicking assign assessment card: {e}")

    def fill_and_assign_assessment(self, student_name: str = "sachin kharat"):
        try:
            self.page.wait_for_timeout(1500)
            if self.python_test_radio.is_visible():
                self.python_test_radio.scroll_into_view_if_needed()
                self.python_test_radio.click(force=True)
        except:
            pass

        try:
            self.student_search_input.scroll_into_view_if_needed()
            self.student_search_input.fill(student_name)
        except:
            pass

        try:
            if self.student_checkbox.is_visible():
                self.student_checkbox.scroll_into_view_if_needed()
                self.student_checkbox.click(force=True)
        except:
            pass

        try:
            if self.assigned_status_button.is_visible():
                self.assigned_status_button.scroll_into_view_if_needed()
                self.assigned_status_button.click(force=True)
        except:
            pass
            
        try:
            self.assign_assessment_submit_button.scroll_into_view_if_needed()
            self.assign_assessment_submit_button.click(force=True)
        except Exception as e:
            print(f"Error submitting assign assessment: {e}")

    def click_ok_button(self):
        try:
            self.page.wait_for_selector("button:has-text('OK')", timeout=5000)
            if self.ok_button.is_visible():
                self.ok_button.scroll_into_view_if_needed()
                self.ok_button.click(force=True)
        except TimeoutError:
            pass
        self.page.wait_for_timeout(1000) 