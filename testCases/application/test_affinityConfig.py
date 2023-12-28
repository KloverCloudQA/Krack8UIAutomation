import logging
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.Locators.Locators import Locator
from selenium.webdriver.common.by import By

from pageObjects.application.affinityConfig.pom_affinityConfig import AffinityConfig
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
        self.ob = AffinityConfig(self.driver)

        self.ob.logIn()  # login
        self.ob.go_affinity_page()
        self.ob.click_on_addAffinity_icon()
        self.ob.input_affinity_name()
