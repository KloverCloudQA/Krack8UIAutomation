from selenium.common import NoSuchElementException, TimeoutException, InvalidSessionIdException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import logging
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
import utilities.customLogger as cl
from src.Locators.Locators import Locator
from pageObjects.auth.pom_LoginPage import LoginPage


class Application:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    # logger object
    logger = cl.LogGen.customLogger(logging.DEBUG)

    checkbox_application_build_trigger_mode_manual = Locator.checkbox_application_build_trigger_mode_manual_xpath
    textbox_password_id = Locator.textbox_Password_xpath
    button_login_xpath = Locator.button_SignI_xpath

    button_webframework_springBoot = Locator.button_webframework_springBoot_xpath
    button_webframework_ExpressJS = Locator.button_webframework_ExpressJS_xpath
    button_webframework_Django = Locator.button_webframework_Django_xpath
    button_webframework_DotNet = Locator.button_webframework_Dot_Net_xpath
    button_webframework_Laravel = Locator.button_webframework_Laravel_xpath
    button_webframework_Golang = Locator.button_webframework_Golang_xpath
    dropdown_team_bar = Locator.dropdown_teamBar_application_creation_xpath
    checkbox_Enable_Persistent_Volume = Locator.checkbox_Enable_Persistent_Volume_xpath
    checkbox_Enable_In_Memory_Volume_Non_Persistent = Locator.checkbox_Enable_In_Memory_Volume_Non_Persistent_xpath
    checkbox_Enable_Auto_Scaling = Locator.checkbox_Enable_Auto_Scaling_xpath
    checkbox_Enable_Basic_Auth = Locator.checkbox_Enable_Basic_Auth_xpath
    textbox_In_Memory_Volume_Mount_Paths_Non_Persistent = Locator.textbox_In_Memory_Volume_Mount_Paths_Non_Persistent_xpath
    checkbox_CPU_Threshold = Locator.checkbox_CPU_Threshold_application_xpath
    textbox_basic_auth_username = Locator.textbox_basic_auth_username_application_xpath
    textbox_basic_auth_password = Locator.textbox_basic_auth_password_application_xpath


    def __init__(self, driver):
        self.driver = driver

    def logIn(self):
        self.lp = LoginPage(self.driver)
        self.lp.logIn()

    def go_to_create_new_application_page(self):
        application_Id = input("Enter your application ID: ")
        self.driver.get(self.baseURL + "applications/" + application_Id + "/settings")
        self.logger.info("opened settings page")
        time.sleep(5)

    def click_on_build_schedule_configuration(self):
        self.driver.find_element(By.XPATH, Locator.Application_Name_bar_xpath).click()
        time.sleep(1)

    def click_(self):
        self.driver.find_element(By.XPATH, Locator.Application_Name_bar_xpath).click()
        time.sleep(1)