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
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import utilities.customLogger as cl
from src.Locators.Locators import Locator
from pageObjects.pom_LoginPage import LoginPage


class Database:
    baseURL = ReadConfig.getApplicationURL()

    # logger object
    logger = cl.LogGen.customLogger(logging.DEBUG)
    # ---------------------------------------locators--------------------------------------------------------
    button_create_new = Locator.button_create_new_database_xpath
    box_team_list = Locator.team_list_dropdown_xpath
    button_login_xpath = Locator.button_SignI_xpath
    textbox_database_server_name = Locator.textbox_database_server_name_xpath
    textbox_initial_admin_password = Locator.textbox_initial_admin_password_database_xpath
    textbox_confirm_password = Locator.textbox_confirm_password_xpath
    button_next = Locator.button_next_database_xpath
    button_confirm = Locator.button_confirm_database_xpath
    button_database_status = Locator.button_database_status_xpath

    database_framework = input("Choose the database by typing MySQL/PostgresSQL/MongoDB : ")
    database_name = input("Input your database name : ")

    def __init__(self, driver):
        self.driver = driver

    def logIn(self):
        self.lp = LoginPage(self.driver)
        self.lp.logIn()

    # -----------------------------------------database creation---------------------------------------------------

    def go_to_create_database_page(self):
        self.logger.info("****************** go to database creation page ****************")
        self.driver.get(self.baseURL + "database/create")
        time.sleep(5)

    def click_on_create_new_button(self):
        self.driver.find_element(By.XPATH, self.button_create_new).click()
        self.logger.info("****************** clicked on Create New button ****************")
        time.sleep(3)

    def choose_database_framework(self):
        self.driver.find_element(By.XPATH, "//h3[contains(text(), '" + self.database_framework + "')]").click()
        self.logger.info(f"**************** database framework chosen as : {self.database_framework} **************")
        time.sleep(3)

    def set_access_team(self):
        access_team_name = input("Choose the access team by typing actual team name None/default/team1--- : ")
        self.driver.find_element(By.XPATH, self.box_team_list).click()
        time.sleep(2)
        self.logger.info("****************** clicked team list box ****************")
        self.driver.find_element(By.XPATH, "//span[normalize-space()='" + access_team_name + "']").click()
        self.logger.info(f"**************** access team chosen as : {access_team_name} **************")
        time.sleep(1)

    def set_namespace(self):
        namespace_name = input("Choose the namespace by typing actual namespace name : ")
        self.driver.find_element(By.XPATH, "//h3[@class='vpc__name' and text()='" + namespace_name + "']").click()
        self.logger.info(f"**************** namespace chosen as : {namespace_name} **************")
        time.sleep(2)

    def set_database_server_name(self):
        self.driver.find_element(By.XPATH, self.textbox_database_server_name).send_keys(self.database_name)
        self.logger.info(f"**************** namespace chosen as : {self.database_name} **************")
        time.sleep(1)

    def set_initial_admin_password(self):
        self.driver.find_element(By.XPATH, self.textbox_database_server_name).send_keys(self.database_name)
        self.logger.info(f"*********** database initial admin password inputted as: {self.database_name} *********")
        time.sleep(1)

    def set_confirm_password(self):
        self.driver.find_element(By.XPATH, self.textbox_confirm_password).send_keys(self.database_name)
        self.logger.info(f"*********** confirm password inputted as: {self.database_name} *********")
        time.sleep(1)

    def click_on_next_button(self):
        self.driver.find_element(By.XPATH, self.button_next).click()
        self.logger.info(f"*********** went to the next page *********")
        time.sleep(1)

    def click_on_button_confirm(self):
        self.driver.find_element(By.XPATH, self.button_confirm).click()
        self.logger.info("*********** clicked on confirm button *********")
        time.sleep(1)

    def wait_to_complete_creation(self):
        element = WebDriverWait(self.driver, 120).until(
            EC.presence_of_element_located(self.button_database_status)
        )
        # Check if the element is displayed
        if element.is_displayed():
            self.logger.info(f"****{self.database_name} database cluster creation process is complete ****")
        else:
            self.logger.info(f"****{self.database_name} database status is not found ****")
