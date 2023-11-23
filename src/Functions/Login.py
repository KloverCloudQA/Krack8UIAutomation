from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.pom_LoginPage import LoginPage
from src.Locators.Locators import Locator
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import logging
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import utilities.customLogger as cl
from src.Locators.Locators import Locator


class Namespace:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = cl.LogGen.customLogger(logging.DEBUG)

    namespace_name = input("Enter the namespace name: ")

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self):
        self.logger.info("****************** Verifying successfully sign in  with valid credentials ****************")
        self.lp = LoginPage(self.driver)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(5)
        self.lp.setUserName(self.username)
        time.sleep(2)
        self.lp.setPassword(self.password)
        time.sleep(2)
        self.lp.clickLogin()
        time.sleep(10)
        act_title = self.driver.title
        print(act_title)
        desired_title = "KloverCloud | Dashboard"
        if act_title == desired_title:
            assert True
            self.driver.close()
            self.logger.info(
                "*********************** Signed in successfully with valid credentials *******************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\Login\\" + "test_PageTitle.png")
            self.driver.close()
            self.logger.info("*********************** Sign In failed *******************")
            assert False


