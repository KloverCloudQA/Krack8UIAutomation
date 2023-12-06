import time
import logging

from selenium.common import NoSuchElementException, TimeoutException, InvalidSessionIdException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    button_database_status = Locator.button_database_status_xpath
    button_database_settings = Locator.button_database_settings_xpath
    button_relational = Locator.button_relational_xpath

    def __init__(self, driver):
        self.driver = driver

    def logIn(self):
        self.lp = LoginPage(self.driver)
        self.lp.logIn()

    # -----------------------------------------Restart Application---------------------------------------------------

    def go_database_settings_page(self):
        database_Id = input("Enter the database Id that you want to restart: ")
        self.driver.get(self.baseURL + "database/" + database_Id + "/settings")
        time.sleep(1)
        self.logger.info("****************** opened database's settings page ****************")
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.button_database_settings)))
        time.sleep(2)

    def go_database_list_page(self):
        self.driver.get(self.baseURL + "database")
        time.sleep(8)
        self.logger.info("****************** opened database list page ****************")
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.button_relational)))
        time.sleep(2)

    def click_on_database_by_name_from_list(self):
        database_name = input("Enter the database name that you want to restart: ")
        self.driver.find_element(By.XPATH, "//span[normalize-space()='" + database_name + "']").click()
        time.sleep(1)
        self.logger.info(f"****************** clicked on {database_name} database ****************")
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.button_database_settings)))
        time.sleep(2)

    def click_on_settings(self):
        self.driver.find_element(By.XPATH, self.button_database_settings).click()
        time.sleep(3)
        self.logger.info("****************** clicked on database's settings ****************")
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.button_restart_xpath)))
        time.sleep(2)

    def click_on_restart_button(self):
        self.driver.find_element(By.XPATH, self.button_restart_xpath).click()
        time.sleep(1)
        self.logger.info("****************** clicked on restart button ****************")
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.button_okay_xpath)))
        time.sleep(1)

    def click_on_okay_button(self):
        self.driver.find_element(By.XPATH, self.button_okay_xpath).click()
        time.sleep(3)
        self.logger.info("****************** clicked on okay button to confirm ****************")

    def wait_to_complete_database_restarting(self):
        self.logger.info("wait for a while complete creation")
        try:
            wait_ToCreateApplication = WebDriverWait(self.driver, 180).until(
                EC.presence_of_element_located((By.XPATH, self.button_database_status)))
            if wait_ToCreateApplication.is_displayed():
                time.sleep(4)
                pass
                self.logger.info("database creation process is completed")
            else:
                pass
                self.logger.info("status button is not found")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

    def database_restarting_by_id(self):
        self.logger.info("Database is restarting")
        self.go_database_settings_page()
        self.click_on_restart_button()
        self.click_on_okay_button()
        self.wait_to_complete_database_restarting()

    def database_restarting_by_name(self):
        self.logger.info("Database is restarting")
        self.go_database_list_page()
        self.click_on_database_by_name_from_list()
        self.click_on_settings()
        self.click_on_restart_button()
        self.click_on_okay_button()
        self.wait_to_complete_database_restarting()
