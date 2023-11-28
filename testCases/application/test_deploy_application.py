import time
import logging
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.pom_deploy_application import Application
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import utilities.customLogger as cl
from src.Locators.Locators import Locator


class Test_Create_Namespace:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    # logger object
    logger = cl.LogGen.customLogger(logging.DEBUG)

    def test_application_deployment(self, setup):
        self.logger.info("****************** Verifying successfully sign in  with valid credentials ****************")
        self.driver = setup
        self.driver = setup
        self.ob = Application(self.driver)
        self.ob.logIn()     # login

        self.ob.test_application_deployment()
        time.sleep(2)




