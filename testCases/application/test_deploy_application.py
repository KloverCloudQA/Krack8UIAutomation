import time
import logging

from pageObjects.application.pom_deploy_application import Application
from utilities.readProperties import ReadConfig
import utilities.customLogger as cl


class Test_Create_Namespace:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    # logger object
    logger = cl.LogGen.customLogger(logging.DEBUG)

    def test_application_deployment(self, setup):
        self.logger.info("****************** Verifying successfully sign in  with valid credentials ****************")
        self.driver = setup
        self.driver = setup
        self.ob = Application(self.driver)
        self.ob.logIn()     # login

        self.ob.test_application_deployment()
        time.sleep(2)




