import time
import logging
import pytest
from selenium import webdriver
from pageObjects.pom_application import Application
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import utilities.customLogger as cl


class Test_Create_Namespace:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    # logger object
    logger = cl.LogGen.customLogger(logging.DEBUG)

    # application_name = input("Enter the application name: ")

    def test_easy_fun_login(self, setup):
        self.logger.info("****************** Verifying successfully sign in  with valid credentials ****************")
        self.driver = setup
        self.ob = Application(self.driver)
        self.logger.info("****************** go to login page ****************")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(5)
        self.logger.info("****************** set username ****************")
        self.ob.setUserName(self.username)
        time.sleep(2)
        self.logger.info("****************** set password ****************")
        self.ob.setPassword(self.password)
        time.sleep(2)
        self.logger.info("****************** click on signin button ****************")
        self.ob.clickLogin()
        time.sleep(10)
# -----------------------------------New Application Creation ------------------------------------------------------
#         self.ob.go_to_new_application_creation_form()
        self.driver.get("https://console.kc-cp.klovercloud.io/applications/new")
        time.sleep(5)
        self.ob.choose_framework()
        self.ob.input_application_name()
        self.ob.choose_git_account()
        self.ob.choose_container_registry()
        self.ob.click_next_button()
        self.ob.again_click_next_button()
        self.ob.Choose_A_Namespace()
        self.ob.click_on_save_button()
        self.ob.click_on_create_application_button()
        self.ob.wait_to_complete_app_creation()

