from ui.fixtures import *


def pytest_addoption(parser):
    parser.addoption('--headless', action='store_true')
    parser.addoption('--url', default='https://target-sandbox.my.com/')


@pytest.fixture(scope='session')
def config(request):
    headless = request.config.getoption('--headless')
    url = request.config.getoption('--url')
    return {'headless': headless, 'url': url}


