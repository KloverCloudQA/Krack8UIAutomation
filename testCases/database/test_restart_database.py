import logging
import time

from pageObjects.database.pom_restart_database import DatabaseRestart
from utilities.readProperties import ReadConfig
import utilities.customLogger as cl


class Test_Database_Restarting:
    # logger object
    logger = cl.LogGen.customLogger(logging.DEBUG)

    def test_database_restarting(self, setup):
        self.driver = setup
        self.ob = DatabaseRestart(self.driver)
        self.ob.logIn()  # login
        self.ob.database_restarting_by_id()

    def test_database_restarting_by_name(self, setup):
        self.driver = setup
        self.ob = DatabaseRestart(self.driver)
        self.ob.logIn()  # login
        self.logger.info("Database is restarting")
        self.ob.go_database_list_page()
        self.ob.click_on_database_by_name_from_list()
        self.ob.click_on_settings()
        self.ob.click_on_restart_button()
        self.ob.click_on_okay_button()
        self.ob.wait_to_complete_database_restarting()
