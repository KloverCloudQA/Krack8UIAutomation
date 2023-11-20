import time
import logging
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import utilities.customLogger as cl


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    # logger object
    logger = cl.LogGen.customLogger(logging.DEBUG)

    def test_001_PageTitle(self, setup):
        self.logger.info("*************************** Test_001_Login*************************")
        self.logger.info("*********************** Verifying Homepage Title *******************")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(5)
        act_title = self.driver.title
        desired_title = "KloverCloud | Sign In"
        if act_title == desired_title:
            assert True
            self.driver.close()
            self.logger.info("*********************** homepage title test is passed *******************")

        else:
            self.driver.save_screenshot(".\\Screenshots\\Login\\" + "test_PageTitle.png")
            self.driver.close()
            self.logger.info("*********************** homepage title test is failed *******************")
            assert False

    # def test_002_successful_login(self, setup):
    #     self.logger.info("*************************** Test_002_Login*************************")
    #     self.logger.info("*********************** Verifying successfully login *******************")
    #     self.driver = setup
    #     self.lp = LoginPage(self.driver)
    #     self.driver.get(self.baseURL)
    #     self.driver.maximize_window()
    #     time.sleep(5)
    #     self.lp.setUserName(self.username)
    #     time.sleep(2)
    #     self.lp.setPassword(self.password)
    #     time.sleep(2)
    #     self.lp.clickLogin()
    #     time.sleep(10)
    #     act_title = self.driver.title
    #     print(act_title)
    #     desired_title = "KloverCloud | Dashboard"
    #     if act_title == desired_title:
    #         assert True
    #         self.driver.close()
    #         self.logger.info("*********************** homepage title test is passed *******************")
    #     else:
    #         self.driver.save_screenshot(".\\Screenshots\\Login\\" + "test_PageTitle.png")
    #         self.driver.close()
    #         self.logger.info("*********************** homepage title test is failed *******************")
    #         assert False
