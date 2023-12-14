import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.ie.service import Service as IEService
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def setup_incognito_mode(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        print("Launching chrome browser.........")
    elif browser == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.maximize_window()
        print("Launching firefox browser.........")
    elif browser == 'Ie':
        driver = webdriver.Ie(service=IEService(IEDriverManager().install()))
        driver.maximize_window()
        print("Launching Ie browser.........")
    else:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def setup_chrome_with_sessions():
    chrome_options = Options()
    chrome_options.add_argument("--remote-debugging-port=9222")
    chrome_options.add_argument(
        "user-data-dir=C:\\Users\\KloverCloud\\PycharmProjects\\Krack8UIAutomation\\src\\chromedriver\\chromedata")
    chrome_driver = "C:\\Users\\KloverCloud\\PycharmProjects\\Krack8UIAutomation\\src\\chromedriver\\chromedriver.exe"

    # Remove 'executable_path' argument
    driver = webdriver.Chrome(options=chrome_options)

    # Return the driver instance
    yield driver

    # Teardown: Close the driver after the test
    driver.quit()


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to method
    return request.config.getoption("--browser")
