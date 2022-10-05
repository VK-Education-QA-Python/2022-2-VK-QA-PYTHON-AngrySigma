from os import getenv

import pytest
from dotenv import load_dotenv
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import contacts_locators, login_locators

TIMEOUT = 5

load_dotenv()


class BaseCase:
    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver):
        self.driver = driver

    def wait(self, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=TIMEOUT):
        return self.wait(timeout).until(
            EC.presence_of_element_located(locator))

    def click(self, locator, timeout=TIMEOUT):
        elem = self.wait(timeout).until(
                EC.element_to_be_clickable(locator))
        elem.click()

    def enter_email(self, email):
        email_field = self.find(login_locators.EMAIL_LOCATOR)
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = self.find(login_locators.PASSWORD_LOCATOR)
        password_field.send_keys(password)

    def click_login(self):
        login_button = self.find(login_locators.LOGIN_BUTTON_LOCATOR)
        login_button.click()

    def login(self, email=getenv('EMAIL'), password=getenv('PASSWORD')):
        self.click(login_locators.LOGIN_LOCATOR)
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def fill_fullname_contact(self, fullname='Иванов Иван Иванович'):
        fullname_field = self.find(contacts_locators.FULLNAME_LOCATOR)
        fullname_field.clear()
        fullname_field.send_keys(fullname)

    def fill_ordinn_contact(self, ordinn='123456789012'):
        ordinn_field = self.find(contacts_locators.INN_LOCATOR)
        ordinn_field.clear()
        ordinn_field.send_keys(ordinn)

    def fill_phone_contact(self, phone='+71234567890'):
        phone_field = self.find(contacts_locators.PHONE_LOCATOR)
        phone_field.clear()
        phone_field.send_keys(phone)

    def fill_contacts(self, fullname='Иванов Иван Иванович',
                      ordinn='123456789012',
                      phone='+71234567890'):
        self.fill_fullname_contact(fullname)
        self.fill_ordinn_contact(ordinn)
        self.fill_phone_contact(phone)

    def save_contacts(self):
        save_contacts_button = self.find(
            contacts_locators.SUBMIT_BUTTON_LOCATOR)
        save_contacts_button.click()

    def open_right_menu(self):
        right_menu = self.find(login_locators.USERNAME_LOCATOR)
        right_menu.click()
