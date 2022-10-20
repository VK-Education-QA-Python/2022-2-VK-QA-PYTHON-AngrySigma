import os

import allure
import pytest
from _pytest.fixtures import FixtureRequest
from dotenv import load_dotenv

from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage
from ui.pages.start_page import StartPage

load_dotenv()


class BaseCase:
    driver = None
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config
        self.login_page = LoginPage(driver)
        if self.authorize:
            cookies = request.getfixturevalue('cookies')
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()
            self.main_page = StartPage(driver)

        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.start_page: StartPage = request.getfixturevalue('start_page')

    @pytest.fixture(scope='function', autouse=True)
    def ui_report(self, driver, request, temp_dir):
        failed_test_count = request.session.testsfailed
        yield
        if request.session.testsfailed > failed_test_count:
            browser_logs = os.path.join(temp_dir, 'browser.log')
            with open(browser_logs, 'w') as f:
                for i in driver.get_log('browser'):
                    f.write(f"{i['level']} - {i['source']}\n{i['message']}\n")
            screenshot_path = os.path.join(temp_dir, 'failed.png')
            self.driver.save_screenshot(filename=screenshot_path)
            allure.attach.file(screenshot_path, 'failed.png',
                               allure.attachment_type.PNG)
            with open(browser_logs, 'r') as f:
                allure.attach(f.read(), 'test.log',
                              allure.attachment_type.TEXT)

    def screenshot_to_allure(self, temp_dir, file_name='fail'):
        screenshot_path = os.path.join(temp_dir, f'{file_name}.png')
        self.driver.save_screenshot(filename=screenshot_path)
        allure.attach.file(screenshot_path, f'{file_name}.png',
                           allure.attachment_type.PNG)
