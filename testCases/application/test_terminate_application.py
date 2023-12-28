import time
import logging

from pageObjects.application.pom_terminate_application import TerminateApplication
from utilities.readProperties import ReadConfig
import utilities.customLogger as cl


class Test_Create_Namespace:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    # logger object
    logger = cl.LogGen.customLogger(logging.DEBUG)

    def test_terminate_application(self, setup_chrome_with_sessions):
        # self.driver = setup  # to run incognito mode
        self.driver = setup_chrome_with_sessions  # to run with session
        self.ob = TerminateApplication(self.driver)
        self.ob.logIn()  # login
        self.ob.test_terminate_application()
