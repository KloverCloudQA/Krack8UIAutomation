import time
import logging
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.pom_user_creation import UserCreation
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import utilities.customLogger as cl
from src.Locators.Locators import Locator


class Test_New_User_Creation:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    # logger object
    logger = cl.LogGen.customLogger(logging.DEBUG)

    def test_new_user_creation(self, setup):
        self.logger.info("****************** Verifying successfully sign in  with valid credentials ****************")
        self.driver = setup
        self.ob = UserCreation(self.driver)
        self.ob.logIn()  # login
        # self.ob.nonAdmin_user_creation()  # non admin user creation
        # self.ob.secondaryAdmin_user_creation()  # admin user creation
        self.ob.nonAdmin_user_creation_with_team()
