import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage
from ui.pages.start_page import StartPage
from random import choices, randint
import string
from os import getenv
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope='function')
def driver(config):
    chrome_options = Options()
    headless = config['headless']
    if headless:
        chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(executable_path=ChromeDriverManager(
        version='105.0.5195.19').install(), options=chrome_options)
    driver.get(config['url'])
    yield driver
    driver.quit()


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def login_page(driver):
    return LoginPage(driver=driver)


@pytest.fixture
def start_page(driver):
    return StartPage(driver=driver)


@pytest.fixture(scope='function')
def random_ordinn():
    return randint(100000000000, 999999999999)


@pytest.fixture(scope='function')
def random_phone():
    return f'+{randint(1000000000, 99999999999)}'


@pytest.fixture(scope='function')
def random_fullname():
    return ''.join(choices(string.ascii_letters, k=10))


@pytest.fixture(scope='session')
def credentials():
        email = getenv('EMAIL')
        password = getenv('PASSWORD')
        return email, password


@pytest.fixture(scope='session')
def cookies(credentials, config):
    chrome_options = Options()
    headless = config['headless']
    if headless:
        chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path=ChromeDriverManager(
        version='105.0.5195.19').install(), options=chrome_options)
    driver.get(config['url'])
    login_page = LoginPage(driver)
    login_page.login(*credentials)
    cookies = driver.get_cookies()
    driver.quit()
    return cookies

@pytest.fixture(scope='session')
def credentials():
    email = getenv('EMAIL')
    password = getenv('PASSWORD')
    return email, password