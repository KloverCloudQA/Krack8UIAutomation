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


class Application:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    # logger object
    logger = cl.LogGen.customLogger(logging.DEBUG)

    textbox_username_id = Locator.textbox_Email_xpath
    textbox_password_id = Locator.textbox_Password_xpath
    button_login_xpath = Locator.button_SignI_xpath

    application_name = input("Enter the application name: ")

    def __init__(self, driver):
        self.driver = driver

    def go_to_login_page(self):
        self.logger.info("****************** go to login page ****************")
        self.driver.get(self.baseURL)
        self.logger.info("****************** maximize_window ****************")
        self.driver.maximize_window()
        time.sleep(5)

    def setUserName(self, username):
        self.logger.info("****************** input username ****************")
        self.driver.find_element(By.XPATH, self.textbox_username_id).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.logger.info("****************** input password ****************")
        self.driver.find_element(By.XPATH, self.textbox_password_id).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.logger.info("******************click on sign in button ****************")
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def logIn(self):
        self.go_to_login_page()
        self.setUserName(self.username)
        self.setPassword(self.password)
        time.sleep(2)
        self.clickLogin()
        time.sleep(10)
        self.logger.info("****************** start validation ****************")
        act_title = self.driver.title
        print(act_title)
        desired_title = "KloverCloud | Dashboard"
        if act_title == desired_title:
            assert True
            self.driver.close()
            self.logger.info(
                "*********************** Signed in successfully with valid credentials *******************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\Login\\" + "test_PageTitle.png")
            self.driver.close()
            self.logger.info("*********************** Sign In failed *******************")
            assert False

    # -----------------------------------------Delete Application---------------------------------------------------

    def go_applicationList_page(self):
        self.logger.info("****************** go to application list page ****************")
        self.driver.get(self.baseURL + "applications")
        time.sleep(5)

    def click_application_from_list(self):
        self.logger.info("****************** click on application ****************")
        self.driver.find_element(By.XPATH, "//span[normalize-space()='" + self.application_name + "']").click()
        time.sleep(5)

    def click_on_settings(self):
        self.logger.info("****************** click on settings ****************")
        self.driver.find_element(By.XPATH, Locator.application_Settings_xpath).click()
        time.sleep(5)

    def click_on_delete(self):
        self.logger.info("****************** click on delete ****************")
        self.driver.find_element(By.XPATH, Locator.application_Delete_button_xpath).click()
        time.sleep(5)

    def provide_application_name(self):
        self.logger.info("****************** input application name ****************")
        self.driver.find_element(By.XPATH, Locator.application_name_bar_xpath).send_keys(self.application_name)
        time.sleep(5)

    def click_on_Delete_permanently_button(self):
        self.logger.info("****************** click on submit button ****************")
        self.driver.find_element(By.XPATH, Locator.Delete_permanently_button).click()
        time.sleep(10)

    def validate_application_deletion(self):
        self.logger.info("****************** validate application deletion ****************")

        try:
            self.driver.refresh()
            WebDriverWait(self.driver, 15)
            application = self.driver.find_element(By.XPATH, "//span[normalize-space()='" + self.application_name + "']")

            if not application.is_displayed():
                print("Namespace '" + self.application_name + "' is not found")
                assert True
            else:
                print("Namespace '" + self.application_name + "' is found")
                assert False

        except NoSuchElementException:
            print("\n*******The" + self.application_name + " is not found in the list.***********")
