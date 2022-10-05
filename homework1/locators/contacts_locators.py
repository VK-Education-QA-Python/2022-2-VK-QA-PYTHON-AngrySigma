from selenium.webdriver.common.by import By

FULLNAME_LOCATOR = (By.XPATH, '//*[@data-name="fio"]//child::input')
INN_LOCATOR = (By.XPATH, '//*[@data-name="ordInn"]//child::input')
PHONE_LOCATOR = (By.XPATH, '//*[@data-name="phone"]//child::input')
SUBMIT_BUTTON_LOCATOR = (By.XPATH,
                         '//*[@data-class-name="Submit"]//child::div')
