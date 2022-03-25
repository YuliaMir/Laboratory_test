from selenium import common
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from importlib import import_module


class BasePage:
    ENTRY_PATH = '/'

    def __init__(self, driver, go_to_entrypoint=False):
        self.driver = driver
        self.wait = WebDriverWait(driver, driver.t)
        if go_to_entrypoint:
            self.reload_page()

    def go_to_page(self, path):
        self.driver.open(path)

    def reload_page(self):
        self.go_to_page(self.ENTRY_PATH)

    def element(self, locator: tuple):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except common.exceptions.NoSuchElementException:
            raise AssertionError("Cant find element by locator: {}" . format(locator))

    def click(self, locator:tuple):
        element = self.element(locator)
        self.wait.until(EC.element_to_be_clickable(locator)).click()
        return element

    def switch_to_iframe(self, iframe):
        frame = self.element(iframe)
        self.driver.switch_to.frame(frame)

    def config(self, name):
        module = import_module('configs.' + name)

        try:
            return getattr(module, name.capitalize())
        except AttributeError:
            print('%s: No such class.' % name)
            exit(1)
