import os.path

import pytest
from client import MysqlClient


def pytest_configure(config):
    mysql_client = MysqlClient(user='root',
                               password='pass',
                               db_name='TEST_SQL')
    if not hasattr(config, 'workerinput'):
        mysql_client.create_db()
    mysql_client.connect(db_created=True)
    if not hasattr(config, 'workerinput'):
        for table in ('popular_requests',
                      'request_methods',
                      'users_caused_500',
                      'requests_total',
                      'requests_caused_400'):
            mysql_client.create_table(table)

    config.mysql_client = mysql_client


@pytest.fixture(scope='session')
def mysql_client(request):
    client = request.config.mysql_client
    yield client
    client.session.commit()
    client.execute_query('DROP database IF EXISTS test_sql')
    client.connection.close()


@pytest.fixture(scope='session')
def logfile():
    with open(os.path.dirname(__file__) + '/access.log', 'r') as f:
        yield f.readlines()
