from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_LOCATOR = (By.XPATH,
                     '//*[contains(@class, "responseHead-module-button")]')
    EMAIL_LOCATOR = (By.NAME, 'email')
    PASSWORD_LOCATOR = (By.NAME, 'password')
    LOGIN_BUTTON_LOCATOR = (By.XPATH,
                            '//*[contains(@class, "authForm-module-button")'
                            ' and not(contains(@class, "disabled"))]')
    USERNAME_LOCATOR = (By.XPATH, '//*[contains(@class, "right-module-mail")]')
    LOGIN_EMAIL_OR_PHONE_ERROR = (By.XPATH,
                                  '//*[contains(@class,'
                                  '"authForm-module-notify")]'
                                  '//child::div'
                                  '[contains(@class, "notify-module-error")]')
    WRONG_LOGIN_OR_PASSWORD_LOCATOR = (By.XPATH,
                                       '//*[@id="login_form"]'
                                       '//*[contains(@class, "formMsg_title")]'
                                       '//following::div'
                                       '[contains(@class, formMsg_text)]')
    INACTIVE_LOGIN_BUTTON_LOCATOR = (By.XPATH,
                                     '//*[contains'
                                     '(@class, "authForm-module-disabled")]')
    LOGOUT_LOCATOR = (By.XPATH, '//*[@href="/logout"]')
