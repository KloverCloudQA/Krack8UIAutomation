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


class Application:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    # logger object
    logger = cl.LogGen.customLogger(logging.DEBUG)

    textbox_username_id = Locator.textbox_Email_xpath
    textbox_password_id = Locator.textbox_Password_xpath
    button_login_xpath = Locator.button_SignI_xpath

    application_Id = input("Enter the application Id: ")

    def __init__(self, driver):
        self.driver = driver

    def logIn(self):
        self.lp = LoginPage(self.driver)
        self.lp.logIn()
    # -----------------------------------------Deploy Application---------------------------------------------------

    def go_application_pipeline_page(self):
        self.logger.info("****************** go to application's pipeline page ****************")
        self.driver.get(self.baseURL + "applications/" + self.application_Id + "/pipeline")
        time.sleep(8)

    # def click_application_from_list(self):
    #     self.logger.info("****************** click on application ****************")
    #     self.driver.find_element(By.XPATH, "//span[normalize-space()='" + self.application_name + "']").click()
    #     time.sleep(5)

    def click_on_pipeline_icon(self):
        self.driver.find_element(By.XPATH, Locator.deploy_icon_xpath).click()
        time.sleep(2)
        self.logger.info("****************** clicked on svg icon ****************")

    def click_on_deploy_button(self):
        self.driver.find_element(By.XPATH, Locator.deploy_button_xpath).click()
        time.sleep(2)
        self.logger.info("****************** clicked on svg icon ****************")

    def click_on_okay_button(self):
        self.driver.find_element(By.XPATH, Locator.okay_button_xpath).click()
        time.sleep(3)
        self.logger.info("****************** clicked on okay button to confirm ****************")

    def wait_to_complete_app_creation(self):
        self.logger.info("****************** waiting to complete deployment ****************")

        try:
            wait_to_complete_deploy_xpath = WebDriverWait(self.driver, 800).until(
                EC.visibility_of_element_located((By.XPATH, Locator.wait_to_complete_deploy_xpath)))
            if wait_to_complete_deploy_xpath.is_displayed():
                time.sleep(4)
                pass
                self.logger.info("****************** The application deployment process is complete ****************")
            else:
                pass
                self.logger.info("****************** cross button is not found ****************")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        self.driver.find_element(By.XPATH, Locator.wait_to_complete_deploy_xpath)
        self.logger.info("****************** complete the deployment process ****************")

    def test_application_deployment(self):
        self.go_application_pipeline_page()
        self.click_on_pipeline_icon()
        self.click_on_deploy_button()
        self.click_on_okay_button()
        self.wait_to_complete_app_creation()
