from os import getenv

import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

from ui.locators import segment_page_locators
from ui.pages.base_page import BasePage


class SegmentCreationPage(BasePage):

    locators = segment_page_locators.SegmentPageLocators()

    @allure.step('segment creation')
    def open_segment_creation(self):
        self.click(self.locators.CREATE_SEGMENT_BUTTON)

    def open_segment_apps_and_games(self):
        self.click(self.locators.APPS_AND_GAMES_SEGMENT)

    def open_played_and_payed_on_platform_list(self):
        self.click(self.locators.PLAYED_AND_PAYED_ON_PLATFORM_LIST)

    def mark_target_app_users(self):
        self.click(self.locators.PLAYED_AND_PAYED_ON_PLATFORM_CHECKBOX)

    def submit_segment(self, segment_name):
        self.click(self.locators.SUBMIT_SEGMENT_BUTTON)
        self.find(self.locators.SEGMENT_NAME_FIELD).clear()
        self.find(self.locators.SEGMENT_NAME_FIELD).send_keys(segment_name)
        self.click(self.locators.FINISH_SEGMENT_CREATION)

    @allure.step('add group as source')
    def add_group(self, group=getenv('DEFAULT_VK_GROUP')):
        self.go_to_vk_ok_groups()
        self.add_group_to_sources(group)
        self.click(self.locators.SEGMENTS_LIST)

    def go_to_vk_ok_groups(self):
        self.click(self.locators.VK_OK_GROUPS)

    def add_group_to_sources(self, group):
        self.find(self.locators.VK_OK_SEARCH).send_keys(group)
        self.click(self.locators.SHOW_GROUPS_FOUND)
        self.click(self.locators.VK_OK_CHOOSE_GROUP_FROM_LIST)
        self.click(self.locators.ADD_SELECTED_ITEMS_BUTTON)

    def open_segment_vk_ok(self):
        self.click(self.locators.VK_OK_SEGMENT)

    def mark_group(self):
        self.click(self.locators.GROUP_SEGMENT_CHECKBOX)

    @allure.step('segment and group deletion')
    def delete_segment(self, segment_name):
        try:
            self.click(self.locators.segment_deletion_locator(segment_name))
        except TimeoutException:
            scrollbar_width = self.find(self.locators.SLIDER).rect['width']
            ActionChains(self.driver).click_and_hold(self.present(
                self.locators.SLIDER)
            ).move_by_offset(scrollbar_width/2, 0).release().perform()
        self.click(self.locators.segment_deletion_locator(segment_name))
        self.click(self.locators.CONFIRM_REMOVE_BUTTON)

    def delete_group(self, group=getenv('DEFAULT_VK_GROUP')):
        self.go_to_vk_ok_groups()
        self.click(self.locators.group_deletion_locator(group))
        self.click(self.locators.CONFIRM_REMOVE_BUTTON)
