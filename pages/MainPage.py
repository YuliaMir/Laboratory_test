from .BasePage import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    ENTRY_PATH = '/'
    LOGIN_BUTTON = (By.XPATH, "//div[@id='mailbox']/div[1]/button")
    LOGIN_POPUP = (By.XPATH, "/html/body/div[3]/div/iframe")
    LOGIN_FORM_ACCOUNT_NAME_INPUT = (By.CSS_SELECTOR, "input.input-0-2-71")
    LOGIN_FORM_MAILBOX_SELECTOR = (By.CSS_SELECTOR, ".base-0-2-25 > span")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, ".inner-0-2-81.innerTextWrapper-0-2-82")
    LOGIN_FORM_ACCOUNT_PASSWORD = (By.CSS_SELECTOR, "input.input-0-2-71.withIcon-0-2-72")
    ENTER_BUTTON = (By.CSS_SELECTOR, "span.inner-0-2-81.innerTextWrapper-0-2-82")

    def open_login_popup(self):
        self.click(self.LOGIN_BUTTON)
        self.switch_to_iframe(self.LOGIN_POPUP)

    def enter_credentials(self):
        account_name_input = self.click(self.LOGIN_FORM_ACCOUNT_NAME_INPUT)
        account_name_input.send_keys(self.driver.env['MAIL_TEST_ACCOUNT_USERNAME'])
        self.click(self.CONTINUE_BUTTON)
        account_password_input = self.click(self.LOGIN_FORM_ACCOUNT_PASSWORD)
        account_password_input.send_keys(self.driver.env['MAIL_TEST_ACCOUNT_PASSWORD'])
        self.click(self.ENTER_BUTTON)
