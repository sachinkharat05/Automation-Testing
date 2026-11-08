from playwright.sync_api import Page

class SMEDashboardPage:
    def __init__(self, page: Page):
        self.page = page
        
        # 1. SME डॅशबोर्डवरील एलिमेंट्स
        self.tests_created_card = page.locator("text=Tests Created")  # 'Tests Created' कार्ड[cite: 5]
        
        # 2. Created Assessments पेजवरील एलिमेंट्स
        self.create_test_button = page.get_by_role("button", name="Create Test")  # '+ Create Test' बटण[cite: 6]
        
        # 3. Create New Test फॉर्ममधील फिल्ड्स[cite: 4, 5]
        self.test_name_input = page.locator("input[type='text']").first  # Test Name input[cite: 4]
        self.difficulty_select = page.locator("select").first  # Difficulty Level dropdown[cite: 4, 5]
        self.description_textarea = page.locator("textarea")  # Description textarea[cite: 4, 5]
        self.duration_input = page.locator("input[type='number'], input").last  # Duration input[cite: 5]
        self.submit_create_test_button = page.get_by_role("button", name="Create New Test")  # Submit Test button[cite: 5]

        # 4. Question Setup पेजवरील एलिमेंट्स[cite: 6]
        self.add_questions_button = page.get_by_role("button", name="Add Questions")  # 'Add Questions' बटण[cite: 6]

        # 5. Create Question फॉर्ममधील फिल्ड्स[cite: 7, 8]
        self.text_inputs = page.locator("input[type='text']")  # Question text & Options inputs[cite: 7, 8]
        self.dropdowns = page.locator("select")  # Select dropdowns[cite: 7, 8]
        self.submit_question_button = page.get_by_role("button", name="Submit")  # Submit Question button[cite: 8]

    def click_tests_created(self):
        """'Tests Created' कार्डवर क्लिक करते"""
        self.tests_created_card.click()  #[cite: 5]

    def click_create_test_button(self):
        """'+ Create Test' बटणावर क्लिक करते"""
        self.create_test_button.click()  #[cite: 6]

    def fill_and_create_test(self, test_name: str, difficulty: str, description: str, duration: str):
        """नवीन टेस्टची सर्व माहिती भरून 'Create New Test' सबमिट करते"""
        self.test_name_input.fill(test_name)  #[cite: 4]
        self.difficulty_select.select_option(label=difficulty)  #[cite: 4, 5]
        self.description_textarea.fill(description)  #[cite: 4, 5]
        self.duration_input.fill(duration)  #[cite: 5]
        self.submit_create_test_button.click()  #[cite: 5]

    def click_add_questions_button(self):
        """'Add Questions' बटणावर क्लिक करते"""
        self.add_questions_button.click()  #[cite: 6]

    def fill_and_submit_question(self, question_text: str, opt_a: str, opt_b: str, opt_c: str, opt_d: str, correct_opt: str):
        """नवीन प्रश्न, ४ पर्याय आणि योग्य उत्तर निवडून फॉर्म सबमिट करते"""
        # प्रश्न भरणे (उदा. What is a class in Python?)[cite: 7]
        self.text_inputs.nth(0).fill(question_text)  #[cite: 7]
        
        # ऑप्शन्स भरणे (Option A, B, C, D)[cite: 7, 8]
        self.text_inputs.nth(1).fill(opt_a)  #[cite: 7, 8]
        self.text_inputs.nth(2).fill(opt_b)  #[cite: 7, 8]
        self.text_inputs.nth(3).fill(opt_c)  #[cite: 7, 8]
        self.text_inputs.nth(4).fill(opt_d)  #[cite: 7, 8]
        
        # योग्य उत्तर (Correct Option) निवडणे (उदा. Option B)[cite: 8]
        self.dropdowns.last.select_option(label=correct_opt)  #[cite: 8]
        
        # Submit बटणावर क्लिक करणे[cite: 8]
        self.submit_question_button.click()  #[cite: 8]