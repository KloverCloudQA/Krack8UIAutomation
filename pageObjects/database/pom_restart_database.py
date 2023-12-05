import time
import logging
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
import utilities.customLogger as cl
from src.Locators.Locators import Locator
from pageObjects.auth.pom_LoginPage import LoginPage


class DatabaseRestart:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    # logger object
    logger = cl.LogGen.customLogger(logging.DEBUG)

    button_restart_xpath = Locator.button_restart_database_xpath
    button_okay_xpath = Locator.button_okay_database_xpath

    database_Id = input("Enter the database Id that you want to delete: ")

    def __init__(self, driver):
        self.driver = driver

    def logIn(self):
        self.lp = LoginPage(self.driver)
        self.lp.logIn()

    # -----------------------------------------Restart Application---------------------------------------------------

    def go_database_settings_page(self):
        self.driver.get(self.baseURL + "database/" + self.database_Id + "/settings")
        time.sleep(8)
        self.logger.info("****************** opened database's settings page ****************")

    def click_on_restart_button(self):
        self.driver.find_element(By.XPATH, self.button_restart_xpath).click()
        time.sleep(3)
        self.logger.info("****************** clicked on restart button ****************")

    def click_on_okay_button(self):
        self.driver.find_element(By.XPATH, self.button_okay_xpath).click()
        time.sleep(3)
        self.logger.info("****************** clicked on okay button to confirm ****************")

    def wait_to_complete_restart(self):
        self.logger.info("****************** waiting to complete restarting process ****************")


