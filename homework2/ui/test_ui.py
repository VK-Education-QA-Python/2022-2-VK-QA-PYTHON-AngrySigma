from os import getenv
from time import sleep

import pytest
from dotenv import load_dotenv

from base import BaseCase

load_dotenv()


class TestLogin(BaseCase):
    authorize = False

    @pytest.mark.UI
    def test_login(self, driver):
        self.login_page.login()
        assert self.start_page.find(self.start_page.
                                    locators.USERNAME_LOCATOR), (
            'Did not get redirect to dashboard')


class TestCampaign(BaseCase):
    @pytest.mark.UI
    def test_campaign_creation(self):
        pass


class TestSegments(BaseCase):
    @pytest.mark.UI
    def test_create_apps_games(self):
        pass

    @pytest.mark.UI
    def test_create_delete_ok_vk(self):
        pass
