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


class LoginPage:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    # logger object
    logger = cl.LogGen.customLogger(logging.DEBUG)

    textbox_username_id = Locator.textbox_Email_xpath
    textbox_password_id = Locator.textbox_Password_xpath
    button_login_xpath = Locator.button_SignI_xpath
    button_dashboard_sidebar = Locator.button_dashboard_sidebar_xpath

    def __init__(self, driver):
        self.driver = driver

    def go_to_login_page(self):
        self.logger.info("opened login page")
        self.driver.get(self.baseURL)
        self.logger.info("maximized_window")
        self.driver.maximize_window()
        time.sleep(1)
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.button_login_xpath)))
        time.sleep(2)

    def setUserName(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_id).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_id).send_keys(username)
        self.logger.info("username inputted")

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_id).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_id).send_keys(password)
        self.logger.info("password inputted")

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()
        time.sleep(1)
        self.logger.info("clicked on sign in button")
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.button_dashboard_sidebar)))
        time.sleep(2)

    def login_validation(self):
        self.logger.info("Starting login validation by matching dashboard page title")
        act_title = self.driver.title
        desired_title = "KloverCloud | Dashboard"
        if act_title == desired_title:
            assert True
            self.logger.info(
                "Signed in successfully")
        else:
            self.driver.save_screenshot(".\\Screenshots\\Login\\" + "test_PageTitle.png")
            self.driver.close()
            self.logger.info("Sign In failed")
            assert False

    def logIn(self):
        self.go_to_login_page()
        act_title = self.driver.title
        print(act_title)
        desired_title = "KloverCloud | Sign In"
        if act_title == desired_title:
            self.setUserName(self.username)
            self.setPassword(self.password)
            self.clickLogin()
            self.login_validation()
        else:
            self.logger.info("opened login page")
            print("already signed")
            pass
