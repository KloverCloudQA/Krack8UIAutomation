import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.ie.service import Service as IEService
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setup(browser):
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


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to method
    return request.config.getoption("--browser")


# -------------- To Generate pytest HTML Report ---------------

# It is hooke for Adding Environment info to HTML Report
# It is hooke for Adding Environment info to HTML Report
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'cluster'
#     config._metadata['Module Name'] = 'Login'
#     config._metadata['Tester'] = 'Porag'
#
#
# # It is hooke for delete/Modify Environment info to HTML Report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)
