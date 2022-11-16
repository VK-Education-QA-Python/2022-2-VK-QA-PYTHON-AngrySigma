import pytest


class ApiBase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, api_client, credentials):
        self.api_client = api_client

        if self.authorize:
            self.api_client.post_login(*credentials)
            self.api_client.csrf_token = {'X-CSRFToken': self.api_client.session.cookies.get_dict()['csrftoken']}
