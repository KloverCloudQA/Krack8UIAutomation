from selenium import webdriver
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


class LoginPage:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    # logger object
    logger = cl.LogGen.customLogger(logging.DEBUG)

    textbox_username_id = Locator.textbox_Email_xpath
    textbox_password_id = Locator.textbox_Password_xpath
    button_login_xpath = Locator.button_SignI_xpath

    def __init__(self, driver):
        self.driver = driver

    def go_to_login_page(self):
        self.logger.info("****************** go to login page ****************")
        self.driver.get(self.baseURL)
        self.logger.info("****************** maximize_window ****************")
        self.driver.maximize_window()
        time.sleep(5)

    def setUsername(self):
        self.logger.info("****************** input password ****************")
        password = input("Enter your username: ")
        self.driver.find_element(By.XPATH, self.textbox_username_id).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_id).send_keys(password)

    def setPassword(self):
        self.logger.info("****************** input password ****************")
        password = input("Enter your password: ")
        self.driver.find_element(By.XPATH, self.textbox_password_id).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_id).send_keys(password)

    def logIn(self):
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(5)
        self.logger.info("****************** set username ****************")
        self.setUsername()
        time.sleep(2)
        self.logger.info("****************** set password ****************")
        self.setPassword()
        time.sleep(2)

