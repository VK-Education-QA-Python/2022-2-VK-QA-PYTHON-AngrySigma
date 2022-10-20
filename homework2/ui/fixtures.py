import os
import string
from os import getenv
from random import choice, choices, randint, sample

import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage
from ui.pages.start_page import StartPage

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


@pytest.fixture(scope='function')
def random_ad_link():
    domain = "".join(choices((string.ascii_lowercase + string.digits),
                             k=randint(2, 15)))
    return f'https://'f'{domain}.com'


@pytest.fixture(scope='function')
def random_object_name():
    return ''.join(choices(string.ascii_letters + string.digits,
                           k=randint(2, 20)))
# once returned link to banned resource
# better fix later or switch to ugandan urls
# (or use faker)


@pytest.fixture(scope='function')
def random_sex():
    return choice(['male', 'female', 'both'])


@pytest.fixture(scope='function')
def random_age_set():
    return ', '.join(sample([str(x) for x in range(12, 76)],
                            randint(1, 64)))


@pytest.fixture(scope='function')
def random_age_restriction():
    return choice(['0+', '6+', '12+', '16+', '18+'])


@pytest.fixture(scope='function')
def random_segments():
    return sample(range(1, 11), randint(1, 10))


@pytest.fixture(scope='function')
def random_showtime():
    return choice(['allDays', 'weekDays', 'weekends', 'workTime'])


@pytest.fixture(scope='function')
def random_user_shows_limit():
    return choice(['day', 'week', 'month'])


@pytest.fixture(scope='function')
def random_campaign_shows_limit():
    return choice(range(32))


@pytest.fixture(scope='function')
def random_ads_shows_limit():
    return choice(range(32))


@pytest.fixture(scope='function')
def random_budget_per_day():
    return randint(0, 1000) + 100


@pytest.fixture(scope='function')
def random_budget_total():
    return randint(1, 100) * 100


@pytest.fixture(scope='session')
def credentials():
    email = getenv('EMAIL')
    password = getenv('PASSWORD')
    return email, password


@pytest.fixture(scope='session')
def cookies(credentials, config):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path=ChromeDriverManager(
        version='105.0.5195.19').install(), options=chrome_options)
    driver.get(config['url'])
    login_page = LoginPage(driver)
    login_page.login(*credentials)
    cookies = driver.get_cookies()
    driver.quit()
    return cookies


@pytest.fixture()
def image_path(repo_root):
    return os.path.join(repo_root, 'files', 'image.jpg')


@pytest.fixture()
def audio_path(repo_root):
    return os.path.join(repo_root, 'files', 'audio.mp3')
