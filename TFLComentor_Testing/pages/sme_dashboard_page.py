from playwright.sync_api import Page, TimeoutError

class SMEDashboardPage:
    def __init__(self, page: Page):
        self.page = page
        
        self.tests_created_card = page.locator("text=Tests Created")
        self.create_test_button = page.get_by_role("button", name="+ Create Test")
        
        # New Test Form Elements
        self.test_name_input = page.locator("input[placeholder='Enter test name']")
        self.difficulty_dropdown = page.locator("select")
        self.description_input = page.locator("textarea[placeholder='Enter description']")
        self.duration_input = page.locator("input[type='number']")
        self.submit_test_button = page.get_by_role("button", name="Create New Test")
        
        # Question Setup Elements
        self.add_questions_button = page.get_by_role("button", name="Add Questions")
        self.select_questions_button = page.get_by_role("button", name="Select Questions")
        self.question_checkboxes = page.locator("input[type='checkbox']")
        self.save_questions_button = page.get_by_role("button", name="Save")

    def click_tests_created(self):
        self.tests_created_card.scroll_into_view_if_needed()
        self.tests_created_card.click(force=True)

    def click_create_test_button(self):
        self.create_test_button.scroll_into_view_if_needed()
        self.create_test_button.click(force=True)

    def fill_and_create_test(self, test_name: str, difficulty: str, description: str, duration: str):
        self.test_name_input.fill(test_name)
        self.difficulty_dropdown.select_option(difficulty)
        self.description_input.fill(description)
        self.duration_input.fill(duration)
        
        self.submit_test_button.scroll_into_view_if_needed()
        try:
            with self.page.expect_navigation(timeout=10000):
                self.submit_test_button.click(force=True)
        except Exception:
            self.submit_test_button.click(force=True)

    def click_select_questions_button(self):
       
        try:
            self.page.locator("select").nth(0).select_option(label="MCQ")
        except:
            try:
                self.page.get_by_text("Select question type").click(force=True)
                self.page.get_by_text("MCQ", exact=True).click(force=True)
            except:
                pass

        try:
            self.page.locator("select").nth(1).select_option(label="Beginner")
        except:
            try:
                self.page.get_by_text("Select skill level").click(force=True)
                self.page.get_by_text("Beginner", exact=True).click(force=True)
            except:
                pass

        try:
            self.page.locator("select").nth(2).select_option(label="Approved")
        except:
            try:
                self.page.get_by_text("Select status").click(force=True)
                self.page.get_by_text("Approved", exact=True).click(force=True)
            except:
                pass

        try:
            if self.add_questions_button.is_visible():
                self.add_questions_button.scroll_into_view_if_needed()
                self.add_questions_button.click(force=True)
        except Exception as e:
            print(f"Add Questions click skipped: {e}")

    def select_questions_and_save(self):
        
        try:
            self.page.wait_for_selector("input[type='checkbox']", timeout=5000)
        except TimeoutError:
            pass
        
        try:
            count = self.question_checkboxes.count()
            print(f"Total questions available: {count}")
            for i in range(min(5, count)):
                cb = self.question_checkboxes.nth(i)
                cb.scroll_into_view_if_needed()
                if not cb.is_checked():
                    cb.click(force=True)
        except Exception as e:
            print(f"Checkbox selection error: {e}")


        try:
            if self.select_questions_button.is_visible():
                self.select_questions_button.scroll_into_view_if_needed()
                self.select_questions_button.click(force=True)
        except:
            pass

        try:
            if self.save_questions_button.is_visible():
                self.save_questions_button.scroll_into_view_if_needed()
                self.save_questions_button.click(force=True)
        except:
            pass