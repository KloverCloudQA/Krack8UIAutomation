import logging
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.Locators.Locators import Locator
from selenium.webdriver.common.by import By

from pageObjects.application.pom_app_build_trigger import Application
from utilities.readProperties import ReadConfig
import utilities.customLogger as cl


class Test_Create_Application:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    # logger object
    logger = cl.LogGen.customLogger(logging.DEBUG)

    def test_custom_build_feature(self, setup_chrome_with_sessions):  # "to run using existing chrom browser just replace
        # chrome_driver instance of setup"
        # self.driver = setup  # to run incognito mode
        self.driver = setup_chrome_with_sessions  # to run with session
        self.ob = Application(self.driver)

        self.ob.logIn()  # login
        self.ob.application_build_trigger_test_by_create_new_app()  # New Application Creation

