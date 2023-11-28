import time
import logging
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.pom_Namespace import Namespace
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

    def test_namespace_deletion(self, setup):
        self.logger.info("****************** Verifying successfully sign in  with valid credentials ****************")
        self.driver = setup
        self.lp = Namespace(self.driver)
        self.logger.info("****************** go to login page ****************")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(5)
        self.logger.info("****************** set username ****************")
        self.lp.setUserName(self.username)
        time.sleep(2)
        self.logger.info("****************** set password ****************")
        self.lp.setPassword(self.password)
        time.sleep(2)
        self.logger.info("****************** click on signin button ****************")
        self.lp.clickLogin()
        time.sleep(10)

        self.lp.go_namespaceList_page()
        self.lp.click_namespace_from_list()
        self.lp.click_on_settings()
        self.lp.click_on_delete()
        self.lp.input_namespace_name()
        self.lp.click_on_Delete_permanently_button()
        time.sleep(20)
        self.lp.validate_namespace_deletion()
