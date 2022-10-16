from ui.pages.base_page import BasePage
from ui.pages.start_page import StartPage
from os import getenv
from dotenv import load_dotenv

load_dotenv()


class LoginPage(BasePage):
    def enter_email(self, email):
        email_field = self.find(self.locators.EMAIL_LOCATOR)
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = self.find(self.locators.PASSWORD_LOCATOR)
        password_field.send_keys(password)

    def click_login(self):
        login_button = self.find(self.locators.LOGIN_BUTTON_LOCATOR)
        login_button.click()

    def login(self, email=getenv('EMAIL'), password=getenv('PASSWORD')):
        self.click(self.locators.LOGIN_LOCATOR)
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()
        return StartPage(self.driver)