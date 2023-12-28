import logging
import time

from pageObjects.application.pom_new_application_creation import Application
from utilities.readProperties import ReadConfig
import utilities.customLogger as cl


class Test_Create_Application:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    # logger object
    logger = cl.LogGen.customLogger(logging.DEBUG)

    # def test_new_application_creation(self, setup_incognito_mode):
    #     self.driver = setup_incognito_mode
    #     self.ob = Application(self.driver)
    #     self.ob.logIn()  # login
    #     # self.ob.new_application_creation()  # New Application Creation

    def test_application_creation_with_advanced_feature(self, setup_chrome_with_sessions):
        # self.driver = setup  # to run incognito mode
        self.driver = setup_chrome_with_sessions  # to run with session
        self.ob = Application(self.driver)
        self.ob.logIn()  # login
        self.ob.application_creation_with_advanced_feature()  # New Application Creation

    # def test_application_create_and_build(self, setup_chrome_with_sessions):
    #     # self.driver = setup  # to run incognito mode
    #     self.driver = setup_chrome_with_sessions  # to run with session
    #     self.ob = Application(self.driver)
    #     self.ob.logIn()  # login
    #     self.ob.application_create_and_build()  # New Application Creation

    # def test_application_create_build_and_deploy(self, setup_chrome_with_sessions):
    #     # self.driver = setup  # to run incognito mode
    #     self.driver = setup_chrome_with_sessions  # to run with session
    #     self.ob = Application(self.driver)
    #     self.ob.logIn()  # login
    #     self.ob.application_create_build_deploy()  # New Application Creation
