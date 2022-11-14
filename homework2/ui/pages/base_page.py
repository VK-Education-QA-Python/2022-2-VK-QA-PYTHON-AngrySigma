from time import sleep

from dotenv import load_dotenv
from selenium.common.exceptions import (ElementClickInterceptedException,
                                        StaleElementReferenceException)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from ui.locators import login_page_locators

load_dotenv()

TIMEOUT = 15
CLICK_RETRY = 5


class BasePage:
    locators = login_page_locators.LoginPageLocators()

    def __init__(self, driver):
        self.driver = driver

    def wait(self, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout=timeout)

    def present(self, locator, timeout=TIMEOUT):
        return self.wait(timeout).until(
            EC.presence_of_element_located(locator))

    def find(self, locator, timeout=TIMEOUT):
        return self.wait(timeout).until(
            EC.element_to_be_clickable(locator))

    def click(self, locator, timeout=TIMEOUT):
        for i in range(CLICK_RETRY):
            try:
                elem = self.find(locator, timeout=timeout)
                elem.click()
                return
            except (ElementClickInterceptedException,
                    StaleElementReferenceException):
                if i == CLICK_RETRY:
                    raise
            sleep(0.25)
