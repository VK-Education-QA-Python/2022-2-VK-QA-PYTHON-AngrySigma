from dotenv import load_dotenv
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from ui.locators import login_locators

TIMEOUT = 5

load_dotenv()


class BasePage:
    locators = login_locators.LoginLocators()

    def __init__(self, driver):
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

