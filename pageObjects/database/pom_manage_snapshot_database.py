from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
import time
import logging
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
import utilities.customLogger as cl
from src.Locators.Locators import Locator
from pageObjects.auth.pom_LoginPage import LoginPage
from selenium.webdriver.support import expected_conditions as EC


class DatabaseSnapshot:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    # logger object
    logger = cl.LogGen.customLogger(logging.DEBUG)
    database_Settings_xpath = Locator.database_Settings_xpath
    textbox_database_name = Locator.textbox_database_name_xpath
    button_relational = Locator.button_relational_xpath
    button_manage_snapshot_database = Locator.text_manage_snapshot_database_xpath
    button_edit_to_manage_snapshot = Locator.button_edit_to_manage_snapshot_xpath
    checkbox_to_manage_snapshot = Locator.checkbox_to_enable_manage_snapshot_xpath
    button_snapshot_from_header = Locator.button_snapshot_from_header_xpath
    button_close_to_manage_snapshot = Locator.button_close_to_manage_snapshot_xpath
    button_take_snapshot = Locator.button_take_snapshot_xpath
    checkbox_default_automated_scheduler_config = Locator.checkbox_default_automated_scheduler_config_xpath
    button_save_to_manage_snapshot = Locator.button_save_to_manage_snapshot_xpath

    database_id = input("Enter the database's id : ")

    def __init__(self, driver):
        self.driver = driver

    def logIn(self):
        self.lp = LoginPage(self.driver)
        self.lp.logIn()

    # -----------------------------------------delete database---------------------------------------------------

    def go_database_settings_page(self):
        self.driver.get(self.baseURL + "database/" + self.database_id + "/settings")
        time.sleep(1)
        self.logger.info("opened database list page")
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.button_manage_snapshot_database)))
        time.sleep(1)

    def click_on_edit_button_to_enable_manage_snapshot(self):
        self.driver.find_element(By.XPATH, self.button_edit_to_manage_snapshot).click()
        time.sleep(1)
        self.logger.info("clicked on edit button to manage snapshot")

    def enable_manage_snapshot(self):
        try:
            # Assuming self.checkbox_default_automated_scheduler_config is a valid XPath
            checkbox = self.driver.find_element(By.XPATH, self.checkbox_default_automated_scheduler_config)

            # Check if the checkbox is selected
            if checkbox.is_displayed():
                print("Checkbox is selected.")
                self.logger.info("Snapshot is enabled.")
                self.driver.find_element(By.XPATH, self.button_close_to_manage_snapshot).click()
                time.sleep(1)
            elif checkbox.is_not_displayed():
                print("Snapshot is not enabled")
                self.logger.info("Snapshot is not enabled.")
                self.driver.find_element(By.XPATH, self.checkbox_to_manage_snapshot).click()
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.button_save_to_manage_snapshot).click()
                time.sleep(1)
                print("now snapshot is enabled.")
                self.logger.info("now snapshot is enabled.")
        except NoSuchElementException:
            print("Snapshot is not enabled.")
            self.logger.error("Snapshot is not enabled.")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
            self.logger.error(f"An unexpected error occurred: {str(e)}")

    def click_on_snapshot_from_header(self):
        self.driver.find_element(By.XPATH, self.button_snapshot_from_header).click()
        self.logger.info("clicked on snapshot form header")
        time.sleep(1)
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.button_take_snapshot)))
        time.sleep(1)

    def click_take_snapshot_button(self):
        take_snapshot = self.driver.find_element(By.XPATH, self.textbox_database_name).send_keys(self.button_take_snapshot).click()
        self.logger.info("clicked on take snapshot button")

    def database_snapshot_check_enable_or_disable(self):
        self.logger.info("starting database snapshot checking enable or disable")
        self.go_database_settings_page()
        self.enable_manage_snapshot()
        self.click_on_snapshot_from_header()
        self.click_take_snapshot_button()

        print("checking done")
