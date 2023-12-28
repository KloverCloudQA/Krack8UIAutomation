import logging
import time

from pageObjects.application.pom_onboard_application import Application
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

    def test_onboard_app(self, setup_chrome_with_sessions):
        # self.driver = setup  # to run incognito mode
        self.driver = setup_chrome_with_sessions  # to run with session
        self.ob = Application(self.driver)
        self.ob.logIn()  # login
        self.ob.go_to_application_list_page()  # New Application Creation
        self.ob.click_on_onboard_existing_app_button()
        self.ob.choose_git_account_from_list()
        self.ob.choose_repository_location()
        self.ob.choose_repository_name()
        self.ob.choose_branch()
        self.ob.choose_language_and_application_type()
        self.ob.click_on_next_button_on_board()
        self.ob.input_application_name()
        self.ob.input_application_port()
        self.ob.choose_container_registry()
        self.ob.click_next_button()
        self.ob.again_click_next_button()
        self.ob.Choose_A_Namespace()
        self.ob.click_on_save_button()
        self.ob.click_on_create_application_button()
        self.ob.wait_to_complete_app_creation()
        self.ob.application_build_status_check()
        time.sleep(5)

