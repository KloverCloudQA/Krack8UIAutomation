import time
import logging

from pageObjects.application.pom_delete_application import Application
from utilities.readProperties import ReadConfig
import utilities.customLogger as cl


class Test_Create_Namespace:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    # logger object
    logger = cl.LogGen.customLogger(logging.DEBUG)

    def test_application_deletion(self, setup):
        self.logger.info("****************** Verifying successfully sign in  with valid credentials ****************")
        self.driver = setup
        self.ob = Application(self.driver)
        self.ob.logIn()     # login

        self.ob.go_applicationList_page()
        self.ob.click_application_from_list()
        self.ob.click_on_settings()
        self.ob.click_on_delete()
        self.ob.provide_application_name()
        self.ob.click_on_Delete_permanently_button()
        time.sleep(20)
        self.ob.validate_application_deletion()
