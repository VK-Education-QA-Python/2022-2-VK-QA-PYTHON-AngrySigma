from os import getenv
from time import sleep

import pytest
from dotenv import load_dotenv
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from base import BaseCase
from locators import header_locators, login_locators

load_dotenv()


class TestUi(BaseCase):
    @pytest.mark.UI
    def test_login(self, driver):
        sleep(5)
        self.click(login_locators.LOGIN_LOCATOR)
        assert 'authForm' in driver.page_source, (
            'Authentication form did not appear')
        self.enter_email(getenv('EMAIL'))
        assert getenv('EMAIL') in driver.page_source, (
            'Email field does not allow input')
        self.enter_password(getenv('PASSWORD'))
        assert getenv('PASSWORD') in driver.page_source, (
            'Password field does not allow input')
        self.click_login()
        assert self.find(login_locators.USERNAME_LOCATOR), (
            'Did not get redirect to dashboard')

    @pytest.mark.UI
    def test_logout(self, driver):
        self.login()
        self.find(header_locators.DASHBOARD_ACTIVE_LOCATOR)
        self.open_right_menu()
        sleep(0.5)
        self.click(login_locators.LOGOUT_LOCATOR)
        assert self.find(login_locators.LOGIN_LOCATOR)

    @pytest.mark.UI
    def test_login_without_email(self, driver):
        self.login(email='not_email_or_phone_number')
        try:
            self.find(login_locators.USERNAME_LOCATOR)
        except TimeoutException:
            pass
        else:
            pytest.fail(
                'Redirected to dashboard while'
                ' having wrong credentials format')
        assert self.find(login_locators.LOGIN_EMAIL_OR_PHONE_ERROR), (
            'No notification of wrong credentials format')

    @pytest.mark.UI
    def test_wrong_password(self, driver):
        self.login(password='wrong_password')
        assert self.find(login_locators.WRONG_LOGIN_OR_PASSWORD_LOCATOR), (
            'Did not get redirect to auth page')

    @pytest.mark.UI
    @pytest.mark.parametrize('email, password', [('', ''),
                                                 ('email@mail.com', ''),
                                                 ('', 'password')])
    def test_login_inactive_without_credentials(self, email, password):
        try:
            self.login(email=email, password=password)
        except TimeoutException:
            pass
        else:
            pytest.xfail('Login button clickable without credentials')

    @pytest.mark.UI
    def test_redact_contacts(self, driver, random_fullname, random_ordinn,
                             random_phone):
        self.login()
        driver.get('https://target-sandbox.my.com/profile/contacts')
        self.fill_contacts(fullname=random_fullname, ordinn=random_ordinn,
                           phone=random_phone)
        self.save_contacts()
        driver.refresh()
        assert self.find((By.XPATH,
                          f'//*[@title="{random_fullname}"'
                          f' and contains(text(), "{random_fullname}")]'))

    @pytest.mark.UI
    @pytest.mark.parametrize(
        'locator, check_locator', [(
                header_locators.DASHBOARD_LOCATOR,
                header_locators.DASHBOARD_ACTIVE_LOCATOR),
            (
                    header_locators.SEGMENTS_LOCATOR,
                    header_locators.SEGMENTS_ACTIVE_LOCATOR),
            (
                    header_locators.BILLING_LOCATOR,
                    header_locators.BILLING_ACTIVE_LOCATOR),
            (
                    header_locators.STATISTICS_LOCATOR,
                    header_locators.STATISTICS_ACTIVE_LOCATOR),
            (
                    header_locators.PRO_LOCATOR,
                    header_locators.PRO_ACTIVE_LOCATOR),
            (
                    header_locators.PROFILE_LOCATOR,
                    header_locators.PROFILE_ACTIVE_LOCATOR),
            (
                    header_locators.TOOLS_LOCATOR,
                    header_locators.TOOLS_ACTIVE_LOCATOR),
            (
                    header_locators.HELP_LOCATOR,
                    header_locators.HELP_ACTIVE_LOCATOR)])
    def test_header_links(self, driver, locator, check_locator):
        self.login()
        self.click(locator)
        if len(driver.window_handles) > 1:
            driver.switch_to.window(driver.window_handles[1])
        assert self.find(check_locator, timeout=15)
