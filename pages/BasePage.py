import logging
import allure
from selenium import common
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains



class BasePage:
    ENTRY_PATH = '/'

    def __init__(self, driver, wait=5, go_to_entrypoint=False):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait)
        self.__config_logger()
        if go_to_entrypoint:
            self.go_to_entrypoint()

    def __config_logger(self):
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.addHandler(logging.FileHandler(f"logs/{self.driver.test_name}.log"))
        self.logger.setLevel(level=self.driver.log_level)

    def open(self, url):
        self.logger.info("Opening url: {}".format(url))
        self.driver.get(url)

    def click(self, locator):
        self.logger.info("Clicking element: {}".format(locator))
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def _verify_link_presence(self, link_text):
        try:
            return WebDriverWait(self.driver, self.driver.t) \
                .until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
        except TimeoutException:
            raise AssertionError("Cant find element by link text: {}".format(link_text))

    def _verify_element_presence(self, locator: tuple):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except common.exceptions.NoSuchElementException:
            allure.attach(
                name=self.session_id,
                body=self.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )

            raise AssertionError("Cant find element by locator: {}" . format(locator))

    def _element(self, locator: tuple):
        return self._verify_element_presence(locator)

    def _click_element(self, element):
        ActionChains(self.driver).pause(0.3).move_to_element(element).click().perform()

    def _simple_click_element(self, element):
        element.click()

    def _click(self, locator: tuple):
        element = self._element(locator)
        ActionChains(self.driver).pause(0.3).move_to_element(element).click().perform()

    def _click_in_element(self, element, locator: tuple, index: int = 0):
        element = element.find_elements(*locator)[index]
        self._click_element(element)

    def click_link(self, link_text):
        self._click((By.LINK_TEXT, link_text))
        return self

    def go_to_entrypoint(self):
        self.driver.open(self.ENTRY_PATH)

    def reload_page(self):
        self.go_to_entrypoint()
