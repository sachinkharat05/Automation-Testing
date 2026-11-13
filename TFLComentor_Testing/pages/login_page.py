from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.contact_input = page.locator("input[type='text'], input[type='tel'], input[name*='contact'], input[placeholder*='Contact'], input[placeholder*='Mobile']").first
        self.role_dropdown = page.locator("select").first
        self.password_input = page.locator("input[type='password']").first
        self.login_button = page.get_by_role("button", name="Login")

    def login(self, contact: str, role: str, password: str):
        self.contact_input.fill(contact)
        try:
            self.role_dropdown.select_option(label=role)
        except Exception:
            try:
                self.role_dropdown.select_option(value=role)
            except Exception:
                pass
        self.password_input.fill(password)
        self.login_button.click(force=True)