import os.path

from api.client import ApiClient
from api.fixtures import *


def pytest_addoption(parser):
    parser.addoption('--url', default='https://target-sandbox.my.com/')
    parser.addoption('--authurl', default='https://auth-ac.my.com/auth')


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    auth_url = request.config.getoption('--authurl')
    return {
        'url': url,
        'auth_url': auth_url
    }


@pytest.fixture(scope='session')
def repo_root():
    return os.path.abspath(os.path.join(__file__, os.path.pardir))


@pytest.fixture(scope='session')
def api_client(credentials, config):
    return ApiClient(base_url=config['url'], auth_url=config['auth_url'], email=credentials[0], password=credentials[1])
