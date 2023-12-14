import logging
import time

from pageObjects.database.pom_manage_snapshot_database import DatabaseSnapshot
from utilities.readProperties import ReadConfig
import utilities.customLogger as cl


class Test_Database_Snapshot:
    # logger object
    logger = cl.LogGen.customLogger(logging.DEBUG)

    def test_enable_snapshot(self, setup):
        self.driver = setup
        self.ob = DatabaseSnapshot(self.driver)
        self.ob.logIn()  # login
        self.logger.info("starting database snapshot checking enable or disable")
        self.ob.go_database_settings_page()
        self.ob.click_on_edit_button_to_enable_manage_snapshot()
        self.ob.enable_manage_snapshot()
