import string
from random import choices, randint

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def random_fullname():
    return ''.join(choices(string.ascii_letters, k=10))


@pytest.fixture(scope='function')
def random_ordinn():
    return randint(100000000000, 999999999999)


@pytest.fixture(scope='function')
def random_phone():
    return f'+{randint(1000000000, 99999999999)}'


def pytest_addoption(parser):
    parser.addoption('--headless', action='store_true')
    parser.addoption('--url', default='https://target-sandbox.my.com/')


@pytest.fixture
def config(request):
    headless = request.config.getoption('--headless')
    url = request.config.getoption('--url')
    return {'headless': headless, 'url': url}


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
