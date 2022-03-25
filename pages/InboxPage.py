from selenium.webdriver.common.by import By
from .BasePage import BasePage



class InboxPage(BasePage):
    ENTRY_PATH = '/inbox'
    COMPOSE_EMAIL_BUTTON = (By.CSS_SELECTOR, "span.compose-button__txt")
    MAIL_FORM_INPUT_TO_WHOM = (By.CSS_SELECTOR, ".container--ItIg4 > .inputContainer--nsqFu > .container--H9L5q")
    MAIL_FORM_INPUT_BODY = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div[3]/div[5]/div/div/div[2]/div[1]/div[1]")
    MAIL_FORM_INPUT_SEND_BUTTON = (By.CSS_SELECTOR, "span.button2__txt")


    def create_new_email(self):
        conf = self.config('mail')
        self.click(self.COMPOSE_EMAIL_BUTTON)
        to_whom_field = self.click(self.MAIL_FORM_INPUT_TO_WHOM)
        to_whom_field.send_keys(conf.MAIL_TO)
        email_body_input = self.click(self.MAIL_FORM_INPUT_BODY)
        email_body_input.send_keys(conf.MAIL_CONTENT)




