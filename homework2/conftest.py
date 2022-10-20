import logging
import shutil
import sys

from ui.fixtures import *

def pytest_addoption(parser):
    parser.addoption('--headless', action='store_true')
    parser.addoption('--url', default='https://target-sandbox.my.com/')
    parser.addoption('--debug_log', action='store_true')


@pytest.fixture(scope='session')
def config(request):
    headless = request.config.getoption('--headless')
    url = request.config.getoption('--url')
    return {'headless': headless, 'url': url}


@pytest.fixture(scope='session')
def base_temp_dir():
    if sys.platform.startswith('win'):
        base_dir = 'C:\\tests'
    else:
        base_dir = '/tmp/tests'
    if os.path.exists(base_dir):
        shutil.rmtree(base_dir)
    return base_dir


@pytest.fixture(scope='function')
def temp_dir(base_temp_dir, request):
    test_dir = os.path.join(base_temp_dir, (request._pyfuncitem.nodeid).
                            replace('::', '_'))
    print(base_temp_dir)
    print(request._pyfuncitem.nodeid)
    print(test_dir)
    os.makedirs(test_dir)
    return test_dir


@pytest.fixture(scope='session')
def repo_root():
    return os.path.abspath(os.path.join(__file__, os.path.pardir))


@pytest.fixture(scope='function')
def logger(temp_dir, config):
    log_formatter = logging.Formatter(
        '%(asctime)s — %(filename)s — %(levelname)s - %(name)s — %(message)s')
    log_file = os.path.join(temp_dir, 'uitest.log')
    log_level = logging.DEBUG if config['debug_log'] else logging.INFO

    file_handler = logging.FileHandler(log_file, 'w')
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(log_level)

    log = logging.getLogger()
    log.propagate = False
    log.setLevel(log_level)
    log.handlers.clear()
    log.addHandler(file_handler)

    yield log

    for handler in log.handlers:
        handler.close()