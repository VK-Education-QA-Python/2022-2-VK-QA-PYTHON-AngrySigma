from ui.locators import start_page_locators
from ui.pages.base_page import BasePage
from ui.pages.campaign_creation_page import CampaignCreationPage
from ui.pages.segment_creation_page import SegmentCreationPage


class StartPage(BasePage):

    locators = start_page_locators.StartPageLocators()

    def go_to_campaign_creation_page(self):
        self.click(self.locators.CAMPAIGN_CREATION)
        return CampaignCreationPage(self.driver)

    def go_to_segment_creation_page(self):
        self.click(self.locators.SEGMENT_CREATION)
        return SegmentCreationPage(self.driver)
