from selenium.webdriver.common.by import By

MORE_BUTTON_LOCATOR = (By.XPATH, '//*[contains(@class, "center-module-more")]')
DASHBOARD_LOCATOR = (By.XPATH, '//*[contains(@class, "pageHead")]//'
                               'descendant::a[@href="/dashboard"]')
SEGMENTS_LOCATOR = (By.XPATH, '//*[contains(@class, "pageHead")]//'
                              'descendant::a[@href="/segments"]')
BILLING_LOCATOR = (By.XPATH, '//*[contains(@class, "pageHead")]//'
                             'descendant::a[@href="/billing"]')
STATISTICS_LOCATOR = (By.XPATH, '//*[contains(@class, "pageHead")]//'
                                'descendant::a[@href="/statistics"]')
PRO_LOCATOR = (By.XPATH, '//*[contains(@class, "pageHead")]//'
                         'descendant::a[@href="/pro"]')
PROFILE_LOCATOR = (By.XPATH, '//*[contains(@class, "pageHead")]//'
                             'descendant::a[@href="/profile"]')
TOOLS_LOCATOR = (By.XPATH, '//*[contains(@class, "pageHead")]//'
                           'descendant::a[@href="/tools"]')
HELP_LOCATOR = (By.XPATH,
                '//*[contains(@class, "pageHead")]//'
                'descendant::a[contains(@href, "//'
                'target.my.com/help/advertisers/")]')


DASHBOARD_ACTIVE_LOCATOR = (By.XPATH,
                            '//*[contains(@class, "instruction-module")]')
SEGMENTS_ACTIVE_LOCATOR = (By.XPATH,
                           '//*[@data-class-name="NavigationMenuView"]')
BILLING_ACTIVE_LOCATOR = (By.XPATH, '//*[@class="billing-page"]')
STATISTICS_ACTIVE_LOCATOR = (By.XPATH,
                             '//*[@data-translated="Create a campaign"]')
PRO_ACTIVE_LOCATOR = (By.XPATH, '//*[contains(text(), "404")]')
PROFILE_ACTIVE_LOCATOR = (By.XPATH, '//*[@data-name="username"]')
TOOLS_ACTIVE_LOCATOR = (By.XPATH, '//*[@data-class-name="FeedsView"]')
HELP_ACTIVE_LOCATOR = (By.XPATH, '//*[contains(@class, "search-icon")]')
