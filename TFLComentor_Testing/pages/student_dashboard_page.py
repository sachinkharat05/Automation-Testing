from playwright.sync_api import Page

class StudentDashboardPage:
    def __init__(self, page: Page):
        self.page = page
        
        self.upcoming_assessments_card = page.get_by_text("Upcoming Assessments", exact=True)
        self.start_button = page.get_by_role("button", name="Start")
        
        self.next_button = page.get_by_role("button", name="Next")
        self.submit_all_answers_button = page.get_by_role("button", name="Submit All Answers")

    def click_upcoming_assessments(self):
        self.upcoming_assessments_card.scroll_into_view_if_needed()
        self.upcoming_assessments_card.click(force=True)

    def click_start_assessment(self):
        self.start_button.scroll_into_view_if_needed()
        self.start_button.click(force=True)

    def complete_all_five_questions(self):
        # Q1
        q1_opt = self.page.get_by_text("B. extends", exact=True)
        q1_opt.scroll_into_view_if_needed()
        q1_opt.click(force=True)
        self.next_button.scroll_into_view_if_needed()
        self.next_button.click(force=True)

        # Q2
        q2_opt = self.page.get_by_text("C. List", exact=True)
        q2_opt.scroll_into_view_if_needed()
        q2_opt.click(force=True)
        self.next_button.scroll_into_view_if_needed()
        self.next_button.click(force=True)

        # Q3
        q3_opt = self.page.get_by_text("A. Object", exact=True)
        q3_opt.scroll_into_view_if_needed()
        q3_opt.click(force=True)
        self.next_button.scroll_into_view_if_needed()
        self.next_button.click(force=True)

        # Q4
        q4_opt = self.page.get_by_text("A. new", exact=True)
        q4_opt.scroll_into_view_if_needed()
        q4_opt.click(force=True)
        self.next_button.scroll_into_view_if_needed()
        self.next_button.click(force=True)

        # Q5
        q5_opt = self.page.get_by_text("B. java.util", exact=True)
        q5_opt.scroll_into_view_if_needed()
        q5_opt.click(force=True)

        # Final Submit Button
        if self.submit_all_answers_button.is_visible():
            self.submit_all_answers_button.scroll_into_view_if_needed()
            self.submit_all_answers_button.click(force=True)