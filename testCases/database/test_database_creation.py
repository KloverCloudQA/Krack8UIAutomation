import logging

from pageObjects.database.pom_database import Database
from utilities.readProperties import ReadConfig
import utilities.customLogger as cl


class Test_New_User_Creation:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    # logger object
    logger = cl.LogGen.customLogger(logging.DEBUG)

    def test_simple_nonAdmin_user_creation(self, setup):
        self.logger.info("****************** start user creation ****************")
        self.driver = setup
        self.ob = Database(self.driver)
        self.ob.logIn()  # login
        self.ob.go_to_create_database_page()
        self.ob.choose_database_framework()
        self.ob.set_access_team()

        self.ob.set_namespace()
        self.ob.set_database_server_name()
        self.ob.set_initial_admin_password()

        self.ob.set_confirm_password()
        self.ob.click_on_next_button()
        self.ob.click_on_next_button()
        self.ob.click_on_button_confirm()
        self.ob.wait_to_complete_creation()
