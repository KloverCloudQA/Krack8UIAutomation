import logging
from pageObjects.application.pom_new_application_creation import Application
from utilities.readProperties import ReadConfig
import utilities.customLogger as cl


class Test_Create_Application:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    # logger object
    logger = cl.LogGen.customLogger(logging.DEBUG)

    def test_new_application_creation(self, setup):
        self.logger.info("****************** Verifying successfully sign in  with valid credentials ****************")
        self.driver = setup
        self.driver = setup
        self.ob = Application(self.driver)
        self.ob.logIn()  # login
        self.ob.new_application_creation()  # New Application Creation

