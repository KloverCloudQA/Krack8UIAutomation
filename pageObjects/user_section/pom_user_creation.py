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


class UserCreation:
    baseURL = ReadConfig.getApplicationURL()

    # logger object
    logger = cl.LogGen.customLogger(logging.DEBUG)
    firstname = input("Enter the Firstname: ")
    lastname = input("Enter the Lastname: ")
    auth_type = input("Choose auth type(Password or SSO): ")
    email = input("Enter the email: ")
    password = input("Enter the password: ")

    def __init__(self, driver):
        self.driver = driver

    def logIn(self):
        self.lp = LoginPage(self.driver)
        self.lp.logIn()

    # -----------------------------------------user section---------------------------------------------------

    def go_users_list_page(self):
        self.logger.info("****************** go to users list page ****************")
        self.driver.get(self.baseURL + "manage/users")
        time.sleep(5)

    def click_on_create_user_icon(self):
        self.driver.find_element(By.XPATH, Locator.create_user_icon_xpath).click()
        self.logger.info("****************** clicked on create user icon ****************")
        time.sleep(3)

    def input_firstname(self):
        self.driver.find_element(By.XPATH, Locator.first_name_bar_xpath).send_keys(self.firstname)
        self.logger.info("****************** firstname inputted ****************")
        time.sleep(3)

    def input_lastname(self):
        self.driver.find_element(By.XPATH, Locator.last_name_bar_xpath).send_keys(self.lastname)
        self.logger.info("****************** lastname inputted ****************")
        time.sleep(3)

    def choose_auth_type(self):
        self.driver.find_element(By.XPATH, Locator.auth_type_listbox_xpath).click()
        time.sleep(2)
        self.logger.info("****************** clicked on auth type dropdown button ****************")
        self.driver.find_element(By.XPATH, "//span[normalize-space()='" + self.auth_type + "']").click()
        time.sleep(1)
        self.logger.info(f"****************** auth_type is chosen as : {self.auth_type} ****************")

    def input_email(self):
        self.driver.find_element(By.XPATH, Locator.email_input_bar_xpath).send_keys(self.email)
        time.sleep(1)
        self.logger.info(f"****************** inputted email is : {self.email} ****************")

    def choose_provide_password_checkbox(self):
        self.driver.find_element(By.XPATH, Locator.provide_password_checkbox_xpath).click()
        time.sleep(1)
        self.logger.info(f"****************** chosen provide password check box  ****************")

    def choose_want_to_create_admin_user_checkbox(self):
        self.driver.find_element(By.XPATH, Locator.create_admin_checkbox_xpath).click()
        time.sleep(1)
        self.logger.info(f"****************** chosen want to create admin user check box  ****************")

    def input_password(self):
        self.driver.find_element(By.XPATH, Locator.password_input_bar_xpath).send_keys(self.password)
        time.sleep(1)
        self.logger.info(f"****************** password is inputted as : {self.password}   ****************")

    def input_confirm_password(self):
        self.driver.find_element(By.XPATH, Locator.password_confirmation_input_bar_xpath).send_keys(self.password)
        time.sleep(1)
        self.logger.info(f"****************** password is inputted as : {self.password}   ****************")

    def choose_team(self):
        team_name = input("Enter the team name : ")
        self.driver.find_element(By.XPATH, Locator.team_dropdown_button_xpath).click()
        time.sleep(2)
        self.logger.info("****************** clicked on team dropdown ****************")
        self.driver.find_element(By.XPATH, "//span[normalize-space()='" + team_name + "']").click()
        time.sleep(1)
        # Create an ActionChains instance
        actions = ActionChains(self.driver)

        # Simulate pressing the 'Tab' key
        actions.send_keys(Keys.TAB)

        # Perform the action
        actions.perform()

        # Optional: You may want to wait for some time to see the effect (e.g., for demonstration purposes)
        time.sleep(2)
        self.logger.info(f"****************** chosen team as: {team_name} ****************")

    def choose_role(self):
        role_name = input("Enter the role name : ")
        self.driver.find_element(By.XPATH, Locator.roles_dropdown_button_xpath).click()
        time.sleep(2)
        self.logger.info("****************** clicked on create button ****************")
        self.driver.find_element(By.XPATH, "//span[normalize-space()='" + role_name + "']").click()
        time.sleep(1)
        # Create an ActionChains instance
        actions = ActionChains(self.driver)

        # Simulate pressing the 'Tab' key
        actions.send_keys(Keys.TAB)

        # Perform the action
        actions.perform()

        # Optional: You may want to wait for some time to see the effect (e.g., for demonstration purposes)
        time.sleep(2)
        self.logger.info(f"****************** chosen role as: {role_name} ****************")

    def click_on_create_button(self):
        self.driver.find_element(By.XPATH, Locator.create_button_user_xpath).click()
        time.sleep(5)
        self.logger.info("****************** clicked on create button ****************")

    def validate_user_creation(self):
        self.logger.info("****************** validate new user creation ****************")

        try:
            self.driver.refresh()
            WebDriverWait(self.driver, 15)
            new_users = self.driver.find_element(By.XPATH,
                                                 "//span[normalize-space()='" + self.email + "']")

            if new_users.is_displayed():
                self.logger.info("The new user '" + self.email + "' available in the list")
                assert True
            else:
                self.logger.info("new user '" + self.email + "' is not found the list")
                assert False

        except NoSuchElementException:
            self.logger.info("The new user " + self.email + "is found in the list.")

    def simple_nonAdmin_user_creation(self):
        self.go_users_list_page()
        self.click_on_create_user_icon()
        self.input_firstname()
        self.input_lastname()
        self.choose_auth_type()
        self.input_email()
        self.choose_provide_password_checkbox()
        self.input_password()
        self.input_confirm_password()
        self.click_on_create_button()
        self.validate_user_creation()

    def nonAdmin_user_creation_with_team(self):
        self.go_users_list_page()
        self.click_on_create_user_icon()
        self.input_firstname()
        self.input_lastname()
        self.choose_auth_type()
        self.input_email()
        self.choose_provide_password_checkbox()
        self.input_password()
        self.input_confirm_password()
        self.choose_team()
        self.click_on_create_button()
        self.validate_user_creation()

    def nonAdmin_user_creation_with_role(self):
        self.go_users_list_page()
        self.click_on_create_user_icon()
        self.input_firstname()
        self.input_lastname()
        self.choose_auth_type()
        self.input_email()
        self.choose_provide_password_checkbox()
        self.input_password()
        self.input_confirm_password()
        self.choose_role()
        self.click_on_create_button()
        self.validate_user_creation()

    def nonAdmin_user_creation_with_team_and_role(self):
        self.go_users_list_page()
        self.click_on_create_user_icon()
        self.input_firstname()
        self.input_lastname()
        self.choose_auth_type()
        self.input_email()
        self.choose_provide_password_checkbox()
        self.input_password()
        self.input_confirm_password()
        self.choose_team()
        self.choose_role()
        self.click_on_create_button()
        self.validate_user_creation()

    def secondaryAdmin_user_creation(self):
        self.go_users_list_page()
        self.click_on_create_user_icon()
        self.input_firstname()
        self.input_lastname()
        self.choose_auth_type()
        self.input_email()
        self.choose_want_to_create_admin_user_checkbox()
        self.choose_provide_password_checkbox()
        self.input_password()
        self.input_confirm_password()
        self.click_on_create_button()
        self.validate_user_creation()
