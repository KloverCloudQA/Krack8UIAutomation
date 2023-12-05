import time
import logging

from pageObjects.application.pom_restart_application import Application
from utilities.readProperties import ReadConfig
import utilities.customLogger as cl


class Test_Create_Namespace:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    # logger object
    logger = cl.LogGen.customLogger(logging.DEBUG)

    def test_restart_application(self, setup):
        self.logger.info("****************** Verifying successfully sign in  with valid credentials ****************")
        self.driver = setup
        self.ob = Application(self.driver)
        self.ob.logIn()     # login
        self.ob.test_restart_application()      # restart application by id
        time.sleep(2)




