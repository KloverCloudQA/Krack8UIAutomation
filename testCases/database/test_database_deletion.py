import logging
import time

from pageObjects.database.pom_delete_database import DatabaseDeletion
from utilities.readProperties import ReadConfig
import utilities.customLogger as cl


class Test_Database_cluster_creation:
    # logger object
    logger = cl.LogGen.customLogger(logging.DEBUG)

    def test_database_deletion_by_name(self, setup):
        self.driver = setup
        self.ob = DatabaseDeletion(self.driver)
        self.ob.logIn()  # login
        self.ob.database_deletion_by_name()

