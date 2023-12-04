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
from selenium.webdriver.support import expected_conditions as EC


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
    checkbox_Enable_Web_Client = Locator.checkbox_Enable_Web_Client_xpath
    web_client_username = Locator.textbox_web_client_username_xpath
    web_client_password = Locator.textbox_web_client_password_xpath
    mysql_framework = Locator.button_mysql_xpath
    mongodb_framework = Locator.button_mongodb_xpath
    postgresql_framework = Locator.button_postgresql_xpath
    checkbox_enable_snapshot_service = Locator.checkbox_enable_snapshot_service_xpath

    # database_framework = input("Choose the database framework by typing Mysql/Postgresql/Mongodb : ")
    database_name = input("Input your database name : ")
    namespace_name = input("Choose the namespace by typing actual namespace name : ")
    initial_admin_password = input("Input your initial_admin_password : ")

    def __init__(self, driver):
        self.driver = driver

    def logIn(self):
        self.lp = LoginPage(self.driver)
        self.lp.logIn()

    # -----------------------------------------database creation---------------------------------------------------

    def go_to_create_database_page(self):
        self.driver.get(self.baseURL + "database/create")
        time.sleep(5)
        self.logger.info("opened database creation page")

    def click_on_create_new_button(self):
        self.driver.find_element(By.XPATH, self.button_create_new).click()
        self.logger.info("clicked on Create New button")
        time.sleep(5)

    def choose_database_framework(self):
        while True:
            user_input = input("Enter the database framework (Mongodb/Postgresql/Mysql): ").capitalize()

            if user_input == 'Mongodb':
                self.driver.find_element(By.XPATH, self.mongodb_framework).click()
                self.logger.info(f"Database framework chosen as: {user_input}")
                time.sleep(3)
                break
            elif user_input == 'Postgresql':
                self.driver.find_element(By.XPATH, self.postgresql_framework).click()
                self.logger.info(f"Database framework chosen as: {user_input}")
                time.sleep(3)
                break
            elif user_input == 'Mysql':
                self.driver.find_element(By.XPATH, self.mysql_framework).click()
                self.logger.info(f"Database framework chosen as: {user_input}")
                time.sleep(3)
                break
            else:
                print("Invalid database framework. Please type Mysql/Postgresql/Mongodb.")

    def set_access_team(self):
        # Get user input
        user_input = input("Do you want to set a team? (y/n): ")
        if user_input.lower() == 'y':
            access_team_name = input("Choose the access team by typing actual team name default/team1/team2--- : ")
            # Wait for the team-box to be clickable
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.box_team_list)))

            # Click the team box to show list
            element.click()
            time.sleep(2)
            self.logger.info("team list shown")
            self.driver.find_element(By.XPATH, "//span[normalize-space()='" + access_team_name + "']").click()
            self.logger.info(f"access team chosen as : {access_team_name}")
            time.sleep(1)
            try:
                namespace = WebDriverWait(self.driver, 30).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, "//h3[@class='vpc__name' and text()='" + self.namespace_name + "']")))
                if namespace.is_displayed():
                    time.sleep(2)
                    pass
                else:
                    self.logger.info("Namespace not found")
                    self.driver.close()
            except NoSuchElementException as e:
                print("NoSuchElementException error", e)
            except TimeoutException as e:
                print("TimeoutException error", e)
            except InvalidSessionIdException as e:
                print("InvalidSessionIdException error", e)

    def set_namespace(self):
        self.driver.find_element(By.XPATH, "//h3[@class='vpc__name' and text()='" + self.namespace_name + "']").click()
        self.logger.info(f"namespace chosen as : {self.namespace_name}")
        time.sleep(2)

    def set_database_server_name(self):
        self.driver.find_element(By.XPATH, self.textbox_database_server_name).send_keys(self.database_name)
        self.logger.info(f"namespace chosen as : {self.database_name}")
        time.sleep(1)

    def set_initial_admin_password(self):
        self.driver.find_element(By.XPATH, self.textbox_initial_admin_password).send_keys(self.initial_admin_password)
        self.logger.info(f"database initial admin password inputted as: {self.initial_admin_password}")
        time.sleep(1)

    def set_confirm_password(self):
        self.driver.find_element(By.XPATH, self.textbox_confirm_password).send_keys(self.initial_admin_password)
        self.logger.info(f"confirm password inputted as: {self.initial_admin_password}")
        time.sleep(1)

    def click_on_next_button(self):
        next_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.button_next)))
        next_button.click()
        self.logger.info(f"went to the next page")
        time.sleep(3)

    def click_on_button_confirm(self):
        self.driver.find_element(By.XPATH, self.button_confirm).click()
        self.logger.info("clicked on confirm button")
        time.sleep(3)

    def choose_Enable_Web_Client_checkbox(self):
        # Get user input
        user_input = input("Do you want to enable the web client feature? (y/n): ")
        # If the user chooses to enable the web client feature
        if user_input.lower() == 'y':
            self.driver.find_element(By.XPATH, self.checkbox_Enable_Web_Client).click()
            time.sleep(2)
            self.logger.info("'Enable Web Client' chosen")
            web_client_username = input("Input your web_client_username : ")
            web_client_password = input("Input your web_client_password : ")

            try:
                self.driver.find_element(By.XPATH, self.web_client_username).send_keys(web_client_username)
                time.sleep(1)
                self.logger.info(f"inputted webclient user name : {web_client_username}")
                self.driver.find_element(By.XPATH, self.web_client_password).send_keys(web_client_password)
                time.sleep(1)
                self.logger.info(f"inputted webclient password : {web_client_password}")
            except Exception as e:
                self.logger.info(f"Exception: {e}")
                self.logger.info("Element not found within the timeout.")
                # Add more debug information if needed

    def choose_enable_snapshot_service_checkbox(self):
        # Get user input
        user_input = input("Do you want to enable the snapshot service? (y/n): ")
        # If the user choose to enable the snapshot service
        if user_input.lower() == 'y':
            self.driver.find_element(By.XPATH, self.checkbox_enable_snapshot_service).click()
            time.sleep(2)
            self.logger.info("'enabled snapshot service' chosen")

    def wait_to_complete_database_creation(self):
        self.logger.info("wait for a while complete creation")

        try:
            wait_ToCreateApplication = WebDriverWait(self.driver, 180).until(
                EC.visibility_of_element_located((By.XPATH, self.button_database_status)))
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

    def simple_database_creation(self):
        self.logger.info("Starting a simple database creation")
        self.go_to_create_database_page()
        self.choose_database_framework()
        self.set_namespace()
        self.set_database_server_name()
        self.set_initial_admin_password()
        self.set_confirm_password()
        self.click_on_next_button()
        self.click_on_next_button()
        self.click_on_button_confirm()
        self.wait_to_complete_database_creation()

    def advanced_database_cluster_creation(self):
        self.logger.info("Starting a simple database creation")
        self.go_to_create_database_page()
        self.choose_database_framework()
        self.set_access_team()
        self.set_namespace()
        self.set_database_server_name()
        self.set_initial_admin_password()
        self.set_confirm_password()
        self.choose_Enable_Web_Client_checkbox()
        self.choose_enable_snapshot_service_checkbox()
        self.click_on_next_button()
        self.click_on_next_button()
        self.click_on_button_confirm()
        self.wait_to_complete_database_creation()

