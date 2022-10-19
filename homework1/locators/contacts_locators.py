from selenium.webdriver.common.by import By

FULLNAME_LOCATOR = (By.XPATH, '//*[@data-name="fio"]//descendant::input')
INN_LOCATOR = (By.XPATH, '//*[@data-name="ordInn"]//descendant::input')
PHONE_LOCATOR = (By.XPATH, '//*[@data-name="phone"]//descendant::input')
SUBMIT_BUTTON_LOCATOR = (By.XPATH,
                         '//*[@data-class-name="Submit"]//descendant::div')
