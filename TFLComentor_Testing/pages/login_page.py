from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.contact_input = page.locator("input[type='text'], input[placeholder*='Contact']")
        self.role_select = page.locator("select")
        self.password_input = page.locator("input[type='password']")
        self.login_button = page.get_by_role("button", name="Login")

    def login(self, contact: str, role: str, password: str):
        self.contact_input.fill(contact)
        self.role_select.select_option(label=role)
        self.password_input.fill(password)
        self.login_button.click()