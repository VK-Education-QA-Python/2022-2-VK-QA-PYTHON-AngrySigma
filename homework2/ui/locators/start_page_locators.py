from selenium.webdriver.common.by import By


class StartPageLocators():
    CAMPAIGN_CREATION = (By.XPATH,
                         '//div[contains(@class, "createButtonWrap")]//'
                         'child::div[@data-test="button"]')
    SEGMENT_CREATION = (By.XPATH, '//a[@href="/segments"]')
    USERNAME_LOCATOR = (By.XPATH,
                        '//*[contains(@class, "right-module-mail")]')
