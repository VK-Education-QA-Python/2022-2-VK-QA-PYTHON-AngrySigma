import pytest
from dotenv import load_dotenv
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By

from base import BaseCase

load_dotenv()


class TestCampaign(BaseCase):
    @pytest.mark.UI
    def test_campaign_creation(self,
                               random_ad_link,
                               random_object_name,
                               random_sex,
                               random_age_set,
                               random_age_restriction,
                               random_segments,
                               random_showtime,
                               random_user_shows_limit,
                               random_campaign_shows_limit,
                               random_ads_shows_limit,
                               random_budget_per_day,
                               random_budget_total,
                               image_path,
                               audio_path,
                               temp_dir):
        self.campaign_creation_page = (
            self.start_page.go_to_campaign_creation_page())
        self.campaign_creation_page.choose_audio_campaign_type()
        self.campaign_creation_page.enter_link(random_ad_link)
        self.campaign_creation_page.enter_campaign_name(random_object_name)
        self.campaign_creation_page.pick_sex(random_sex)
        self.campaign_creation_page.pick_age(random_age_set)
        self.campaign_creation_page.pick_age_restriction(
            random_age_restriction)
        self.campaign_creation_page.pick_ab_test(random_segments)
        self.screenshot_to_allure(temp_dir, 'ab_test_filled')
        self.campaign_creation_page.pick_time_to_show(random_showtime)
        self.campaign_creation_page.pick_shows_limit(
            random_user_shows_limit,
            random_campaign_shows_limit,
            random_ads_shows_limit)
        self.campaign_creation_page.pick_budget(random_budget_per_day,
                                                random_budget_total)
        self.campaign_creation_page.pick_interests()
        self.campaign_creation_page.pick_soc_dem()
        self.campaign_creation_page.upload_image(image_path)
        self.campaign_creation_page.upload_audio(audio_path)
        self.campaign_creation_page.submit_banner()
        self.screenshot_to_allure(temp_dir, 'banner_created')
        self.campaign_creation_page.submit_campaign()

        assert self.base_page.find((By.XPATH,
                                    f'//a[@title="{random_object_name}"]'))


class TestSegments(BaseCase):
    @pytest.mark.UI
    def test_create_apps_games(self, random_object_name, temp_dir):
        self.segment_page = self.start_page.go_to_segment_creation_page()
        self.segment_page.open_segment_creation()
        self.segment_page.open_segment_apps_and_games()
        self.segment_page.open_played_and_payed_on_platform_list()
        self.segment_page.mark_target_app_users()
        self.segment_page.submit_segment(random_object_name)
        self.screenshot_to_allure(temp_dir, 'segment_created')
        assert self.segment_page.find((By.XPATH,
                                       f'//a[@title="{random_object_name}"]'))

    @pytest.mark.UI
    def test_create_delete_ok_vk(self, random_object_name, temp_dir):
        self.segment_page = self.start_page.go_to_segment_creation_page()
        self.segment_page.add_group()
        self.screenshot_to_allure(temp_dir, 'group_added')
        self.segment_page.open_segment_creation()
        self.segment_page.open_segment_vk_ok()
        self.segment_page.mark_group()
        self.segment_page.submit_segment(random_object_name)
        self.screenshot_to_allure(temp_dir, 'segment_added')
        assert self.segment_page.find((By.XPATH,
                                       f'//a[@title="{random_object_name}"]'))
        self.segment_page.delete_segment(random_object_name)
        self.screenshot_to_allure(temp_dir, 'segment_deleted')
        with pytest.raises(WebDriverException):
            self.segment_page.find((
                By.XPATH, f'//a[@title="{random_object_name}"]'), timeout=3)
        self.segment_page.delete_group()
        self.screenshot_to_allure(temp_dir, 'group_deleted')
