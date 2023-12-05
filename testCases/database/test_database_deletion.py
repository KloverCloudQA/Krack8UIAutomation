import logging
import time

from pageObjects.database.pom_delete_database import DatabaseDeletion
from utilities.readProperties import ReadConfig
import utilities.customLogger as cl


class Test_Database_cluster_creation:
    # logger object
    logger = cl.LogGen.customLogger(logging.DEBUG)

    def test_database_deletion(self, setup):
        self.driver = setup
        self.ob = DatabaseDeletion(self.driver)
        self.ob.logIn()  # login
        self.logger.info("****************** starting database deletion ****************")
        self.ob.go_database_list_page()
        self.ob.click_on_database_from_list()
        self.ob.click_on_settings()
        self.ob.click_on_delete()
        self.ob.input_database_name()
        self.ob.click_on_delete_permanently_button()
        self.ob.validate_database_deletion()
