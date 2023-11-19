import time

from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.ie.service import Service as IEService
from webdriver_manager.microsoft import IEDriverManager


@pytest.fixture()
def setup():
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    # driver = webdriver.Ie(service=IEService(IEDriverManager().install()))
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # return driver
    yield driver
    driver.quit()


# import pytest
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
#
#
# @pytest.fixture()
# def setup():
#     options = webdriver.ChromeOptions()
#     options.add_argument("--headless")
#     driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
#
#     # driver = webdriver.Chrome(ChromeDriverManager().install())
#     yield driver
#     driver.quit()

# import pytest
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
#
#
# @pytest.fixture()
# def setup():
#     # Use webdriver_manager to manage ChromeDriver
#     chrome_version = ChromeDriverManager().get_version()
#     driver_path = ChromeDriverManager(chrome_version=chrome_version).install()
#
#     # Set up ChromeOptions if needed
#     chrome_options = webdriver.ChromeOptions()
#     # Add options if necessary, e.g., headless mode: chrome_options.add_argument("--headless")
#
#     driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)
#
#     yield driver
#     driver.quit()
