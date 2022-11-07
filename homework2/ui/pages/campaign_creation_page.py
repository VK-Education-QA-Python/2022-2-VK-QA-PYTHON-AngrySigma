from os import getenv
from time import sleep

import allure
from dotenv import load_dotenv
from selenium.common.exceptions import TimeoutException

from ui.locators import campaign_page_locators
from ui.pages.base_page import BasePage

load_dotenv()


class CampaignCreationPage(BasePage):

    locators = campaign_page_locators.CampaignPageLocators()

    @allure.step('start campaign creation')
    def choose_audio_campaign_type(self):
        self.click(self.locators.AUDIO_TYPE_CAMPAIGN_BUTTON)

    def enter_link(self, ad_link=getenv('DEFAULT_AD_LINK')):
        self.find(self.locators.AD_URL_INPUT).send_keys(ad_link)

    @allure.step('fill campaign params')
    def enter_campaign_name(self, campaign_name):
        self.find(self.locators.CAMPAIGN_NAME_INPUT).clear()
        self.find(self.locators.CAMPAIGN_NAME_INPUT).send_keys(campaign_name)

    def pick_sex(self, choices='both'):
        self.open_setting_item(self.locators.SEX_CHOICE,
                               self.locators.SEX_CHOICE_OPENED)
        match choices.lower():
            case 'male':
                self.click(self.locators.FEMALE_CHECKBOX)
            case 'female':
                self.click(self.locators.MALE_CHECKBOX)
            case _:
                pass

    def pick_age(self, age_set):
        self.open_setting_item(self.locators.AGE_CHOICE,
                               self.locators.AGE_CHOICE_OPENED)
        self.click(self.locators.AGE_SETTINGS)
        self.click(self.locators.CUSTOM_AGE_SETTING)
        self.find(self.locators.AGE_SETTING_TEXT).clear()
        self.find(self.locators.AGE_SETTING_TEXT).send_keys(age_set)

    def pick_age_restriction(self, age_restriction):
        self.open_setting_item(self.locators.ADDITIONAL_TARGETING,
                               self.locators.ADDITIONAL_TARGETING_OPENED)
        self.open_setting_item(self.locators.AGE_RESTRICTION_CHOICE,
                               self.locators.AGE_RESTRICTION_CHOICE_OPENED)
        self.click(self.locators.AGE_RESTRICTION_MENU)
        self.click(self.locators.AGE_RESTRICTION_AGE[age_restriction])

    def pick_ab_test(self, segments_to_pick):
        self.open_setting_item(self.locators.ADDITIONAL_TARGETING,
                               self.locators.ADDITIONAL_TARGETING_OPENED)
        self.open_setting_item(self.locators.AB_TEST_CHOICE,
                               self.locators.AB_TEST_CHOICE_OPENED)
        for segment in segments_to_pick:
            self.click(self.locators.AB_TEST_SEGMENT[segment])

    def pick_time_to_show(self, time):
        self.open_setting_item(self.locators.FULLTIME_CHOICE,
                               self.locators.FULLTIME_CHOICE_OPENED)
        self.click(self.locators.FULLTIME_CHOICES[time])

    def pick_shows_limit(self, user_limit, campaign_limit, ad_values):
        self.open_setting_item(self.locators.SHOWS_LIMIT_CHOICE,
                               self.locators.SHOWS_LIMIT_CHOICE_OPENED)
        self.click(self.locators.SHOWS_LIMIT_USER)
        self.click(self.locators.SHOWS_LIMIT_USER_VALUES[user_limit])
        self.click(self.locators.SHOWS_LIMIT_CAMPAIGN)
        self.click(self.locators.SHOWS_LIMIT_CAMPAIGN_VALUES[campaign_limit])
        self.click(self.locators.SHOWS_LIMIT_AD)
        self.click(self.locators.SHOWS_LIMIT_AD_VALUES[ad_values])

    def pick_budget(self, budget_per_day, budget_total):
        self.open_setting_item(self.locators.BUDGET_CHOICE,
                               self.locators.BUDGET_CHOICE_OPENED)
        self.find(self.locators.BUDGET_PER_DAY_INPUT).send_keys(budget_per_day)
        self.find(self.locators.BUDGET_TOTAL_INPUT).send_keys(budget_total)

    @allure.step('fill interests and socdem')
    # map sometimes loads and breaks these two while in headless
    def pick_interests(self):
        self.open_setting_item(self.locators.INTERESTS_CHOICE,
                               self.locators.INTERESTS_CHOICE_OPENED)
        self.click(self.locators.INTERESTS_TREE_BRANCH)
        self.click(self.locators.INTERESTS_TREE_ELEMENT)

    def pick_soc_dem(self):
        self.present(self.locators.SOC_DEM_CHOICE)
        self.open_setting_item(self.locators.SOC_DEM_CHOICE,
                               self.locators.SOC_DEM_CHOICE_OPENED)
        sleep(5)
        self.click(self.locators.SOC_DEM_TREE_BRANCH)
        self.click(self.locators.SOC_DEM_TREE_ELEMENT)

    @allure.step('upload files')
    def upload_image(self, path):
        self.upload_file(self.locators.IMAGE_UPLOAD_BUTTON, path)

    def upload_audio(self, path):
        self.upload_file(self.locators.AUDIO_UPLOAD_BUTTON, path)

    def submit_banner(self):
        self.click(self.locators.SUBMIT_BANNER_BUTTON)

    def submit_campaign(self):
        self.click(self.locators.SUBMIT_CAMPAIGN_BUTTON)

    def open_setting_item(self, locator_closed, opened_locator):
        try:
            self.click(locator_closed)
        except TimeoutException:
            assert self.find(opened_locator)

    def upload_file(self, locator, path):
        self.present(locator).send_keys(path)
