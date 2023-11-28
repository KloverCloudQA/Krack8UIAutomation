import time
import logging
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.pom_delete_application import Application
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

    def test_application_deletion(self, setup):
        self.logger.info("****************** Verifying successfully sign in  with valid credentials ****************")
        self.driver = setup
        self.ob = Application(self.driver)
        self.ob.logIn()     # login

        self.ob.go_applicationList_page()
        self.ob.click_application_from_list()
        self.ob.click_on_settings()
        self.ob.click_on_delete()
        self.ob.provide_application_name()
        self.ob.click_on_Delete_permanently_button()
        time.sleep(20)
        self.ob.validate_application_deletion()
