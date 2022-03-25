from selenium.webdriver.common.by import By
from .BasePage import BasePage
import time


class MainPage(BasePage):
    ENTRY_PATH = '/'
    LOGIN_BUTTON = (By.XPATH, "//div[@id='mailbox']/div[1]/button")