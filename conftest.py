import pytest
import datetime
from dotenv import dotenv_values
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.opera.options import Options as OperaOptions


def pytest_addoption(parser):
    project_config = dotenv_values(".env")
    parser.addoption("--maximized", action="store_true", default=True, help="Maximize browser windows")
    parser.addoption("--headless", action="store_true", help="Run headless")
    parser.addoption("--browser", action="store", default=project_config['DEFAULT_BROWSER'], choices=["chrome", "firefox", "opera"])
    parser.addoption("--url", action="store", default=project_config['BASE_URL'], )
    parser.addoption("--wdbasepath", action="store", default=project_config['WEBDRIVER_BASE_PATH'], )
    parser.addoption("--tolerance", type=int, default=project_config['DEFAULT_TOLERANCE'])
    parser.addoption("--executor", action="store", default=project_config['WEBDRIVER_EXECUTOR'], choices=["local", "remote"])


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    driver_base_path = request.config.getoption("--wdbasepath")
    headless = request.config.getoption("--headless")
    maximized = request.config.getoption("--maximized")
    tolerance = request.config.getoption("--tolerance")
    executor = request.config.getoption("--executor")
    driver = None

    if executor == "local":
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            if headless:
                options.headless = True
            driver = webdriver.Chrome(service=Service(driver_base_path + "/chromedriver"), options=options)
        elif browser == "opera":
            options = OperaOptions()
            if headless:
                options.headless = True
            driver = webdriver.Opera(executable_path=driver_base_path + "/operadriver", options=options)
        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            if headless:
                options.headless = True
            driver = webdriver.Firefox(service=Service(driver_base_path + "/geckodriver"), options=options)

    if maximized:
        driver.maximize_window()
    driver.env = dotenv_values(".env")
    driver.executor = executor
    driver.t = tolerance
    driver.base_url = request.config.getoption("--url")

    def open(path=""):
        return driver.get(driver.base_url + path)

    driver.open = open

    def fin():
        driver.quit()

    request.addfinalizer(fin)

    return driver


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--url")
