import time
import logging

from pageObjects.application.pom_deploy_application import DeployApplication
from utilities.readProperties import ReadConfig
import utilities.customLogger as cl


class Test_Create_Namespace:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    # logger object
    logger = cl.LogGen.customLogger(logging.DEBUG)

    def test_application_deployment_by_id(self, setup_chrome_with_sessions):
        # self.driver = setup  # to run incognito mode
        self.driver = setup_chrome_with_sessions  # to run with session
        self.ob = DeployApplication(self.driver)
        self.ob.logIn()  # login
        self.ob.test_application_deployment_by_id()
