import logging
import time

from pageObjects.database.pom_database import Database
from utilities.readProperties import ReadConfig
import utilities.customLogger as cl


class Test_Database_cluster_creation:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    # logger object
    logger = cl.LogGen.customLogger(logging.DEBUG)

    def test_simple_database_creation(self, setup):
        self.driver = setup
        self.ob = Database(self.driver)
        self.ob.logIn()  # login
        self.ob.simple_database_creation()

    def test_database_creation_with_advanced_feature(self, setup):
        self.driver = setup
        self.ob = Database(self.driver)
        self.ob.logIn()  # login
        self.ob.advanced_database_cluster_creation()

