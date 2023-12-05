from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException, InvalidSessionIdException
from selenium.webdriver.common.by import By
from src.Locators.Locators import Locator
from selenium import webdriver
from selenium.webdriver.common.by import By
from src.Locators.Locators import Locator
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import logging
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import utilities.customLogger as cl
from src.Locators.Locators import Locator
from pageObjects.pom_LoginPage import LoginPage


class DatabaseDeletion:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    # logger object
    logger = cl.LogGen.customLogger(logging.DEBUG)
    database_Settings_xpath = Locator.database_Settings_xpath
    database_Delete_xpath = Locator.button_database_Delete_xpath
    textbox_database_name = Locator.textbox_database_name_xpath
    button_delete_permanently_database = Locator.button_delete_permanently_database_xpath

    database_name = input("Enter the database name that you want to delete : ")

    def __init__(self, driver):
        self.driver = driver

    def logIn(self):
        self.lp = LoginPage(self.driver)
        self.lp.logIn()

    # -----------------------------------------delete database---------------------------------------------------

    def go_database_list_page(self):
        self.driver.get(self.baseURL + "database")
        time.sleep(5)
        self.logger.info("opened database list page")

    def click_on_database_from_list(self):
        self.driver.find_element(By.XPATH, "//span[normalize-space()='" + self.database_name + "']").click()
        self.logger.info(f"clicked on {self.database_name} database")
        time.sleep(5)

    def click_on_settings(self):
        self.driver.find_element(By.XPATH, self.database_Settings_xpath).click()
        time.sleep(5)
        self.logger.info("clicked on settings")

    def click_on_delete(self):
        self.driver.find_element(By.XPATH, self.database_Delete_xpath).click()
        self.logger.info("clicked on delete button")
        time.sleep(5)

    def input_database_name(self):
        self.driver.find_element(By.XPATH, self.textbox_database_name).send_keys(self.database_name)
        time.sleep(5)
        self.logger.info("****************** inputted database name ****************")

    def click_on_delete_permanently_button(self):
        self.driver.find_element(By.XPATH, self.button_delete_permanently_database).click()
        time.sleep(10)
        self.logger.info("****************** clicked on submit button ****************")

    def validate_database_deletion(self):
        self.logger.info("****************** starting validation ****************")

        try:
            self.driver.refresh()
            WebDriverWait(self.driver, 40)
            database = self.driver.find_element(By.XPATH,
                                                "//span[normalize-space()='" + self.database_name + "']")

            if not database.is_displayed():
                print("Namespace '" + self.database_name + "' is not found")
                assert True
            else:
                print("Namespace '" + self.database_name + "' is found")
                assert False

        except NoSuchElementException:
            print("\n*******The " + self.database_name + "database is not found in the list.***********")

    def database_deletion(self):
        self.logger.info("****************** starting database deletion ****************")
        self.go_database_list_page()
        self.click_on_database_from_list()
        self.click_on_settings()
        self.click_on_delete()
        self.input_database_name()
        self.click_on_delete_permanently_button()
        self.validate_database_deletion()
