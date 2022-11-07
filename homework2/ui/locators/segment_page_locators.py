from os import getenv

from dotenv import load_dotenv
from selenium.webdriver.common.by import By

load_dotenv()


class SegmentPageLocators:
    CREATE_SEGMENT_BUTTON = (By.XPATH,
                             '//div[contains(@class, "segments-list")]//'
                             'child::button')
    APPS_AND_GAMES_SEGMENT = (By.XPATH,
                              '//div[contains(@class,'
                              '"adding-segments-modal")]//div[8]')
    VK_OK_SEGMENT = (By.XPATH, '//div[contains(@class,'
                               '"adding-segments-modal")]//div[10]')
    PLAYED_AND_PAYED_ON_PLATFORM_LIST = (By.XPATH,
                                         '//div[1]'
                                         '[@class="adding-segments-source"]')
    PLAYED_AND_PAYED_ON_PLATFORM_CHECKBOX = (
        By.XPATH,
        '//div[1][@class="adding-segments-source"]//input[@type="checkbox"]')
    SUBMIT_SEGMENT_BUTTON = (By.XPATH,
                             '//button[@class="button button_submit" '
                             'and not(@disabled)]')
    VK_OK_GROUPS = (By.XPATH, '//a[@href="/segments/groups_list"]')
    SEGMENTS_LIST = (By.XPATH, '//a[@href="/segments/segments_list"]')
    VK_OK_SEARCH = (By.XPATH, '//input[@type="text"]')
    VK_OK_CHOOSE_GROUP_FROM_LIST = (
        By.XPATH, f'//span[contains(text(), "{getenv("DEFAULT_VK_GROUP")}")]')
    GROUP_SEGMENT_CHECKBOX = (
        By.XPATH, f'//span[contains(text(),'
                  f'"{getenv("DEFAULT_VK_GROUP")}")]//'
                  f'preceding::input[@type="checkbox"]')
    SHOW_GROUPS_FOUND = (By.XPATH, '//div[@data-test="show"]')
    ADD_SELECTED_ITEMS_BUTTON = (
        By.XPATH, '//div[@data-test="add_selected_items_button"]')
    FINISH_SEGMENT_CREATION = (
        By.XPATH, '//button[contains(@class, "button button_submit")]')
    SEGMENT_NAME_FIELD = (
        By.XPATH,
        '//div[@class="input input_create-segment-form"]//child::input')
    CONFIRM_REMOVE_BUTTON = (
        By.XPATH,
        '//button[@class="button button_confirm-remove button_general"]')
    SLIDER = (By.XPATH, '//div[contains(@class, "horizontal custom-scroll")]')

    @staticmethod
    def segment_deletion_locator(name):
        return (
            By.XPATH,
            f'//a[@title="{name}"]//'
            f'following::span[contains(@class, "removeCell")]')

    @staticmethod
    def group_deletion_locator(name):
        return (
            By.XPATH,
            f'//span[@title="{name}"]//'
            f'following::div[@data-class-name="RemoveView"]')
