import logging
import time

from pageObjects.cache.pom_cache_creation import CacheCreation
from utilities.readProperties import ReadConfig
import utilities.customLogger as cl


class Test_Cache_Cluster_Creation:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    # logger object
    logger = cl.LogGen.customLogger(logging.DEBUG)

    def test_simple_cache_creation(self, setup):
        self.driver = setup
        self.ob = CacheCreation(self.driver)
        self.ob.logIn()  # login
        self.logger.info("Starting a simple cache creation")
        self.ob.go_to_create_cache_page()
        self.ob.cache_framework()
        self.ob.set_namespace()
        self.ob.set_cache_server_name()
        self.ob.set_initial_admin_password()
        self.ob.set_confirm_password()
        self.ob.click_on_next_button()
        self.ob.click_on_next_button()
        self.ob.click_on_button_confirm()
        self.ob.wait_to_complete_cache_creation()

