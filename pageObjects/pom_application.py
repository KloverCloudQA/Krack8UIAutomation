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

    web_framework_name = input("Enter the web framework name: ")
    application_name = input("Enter the application name: ")
    git_account = input("Enter git account name: ")
    container_registry = input("Enter container_registry name: ")
    namespace_name = input("Enter namespace name: ")

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

    # ------------------------------------------application from---------------------------------------------------
    # def go_to_new_application_creation_form(self):
    #     self.logger.info("****************** go to new application form ****************")
    #     self.driver.get("https://console.kc-cp.klovercloud.io/applications/new")
    #     self.logger.info("****************** maximize_window ****************")
    #     self.driver.maximize_window()
    #     time.sleep(5)

    def choose_framework(self):
        self.logger.info("****************** choose framework ****************")
        self.driver.find_element(By.XPATH, "//span[contains(text(),'" + self.web_framework_name + "')]").click()
        time.sleep(1)

    def input_application_name(self):
        self.logger.info("****************** input application name ****************")
        self.driver.find_element(By.XPATH, Locator.Application_Name_bar_xpath).send_keys(self.application_name)
        time.sleep(1)

    def choose_git_account(self):
        self.logger.info("****************** choose git account ****************")
        self.driver.find_element(By.XPATH, Locator.git_account_bar_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[contains(text(),'" + self.git_account + "')]").click()
        time.sleep(2)

    def choose_container_registry(self):
        self.logger.info("****************** choose container registry ****************")
        self.driver.find_element(By.XPATH, Locator.container_registry_bar_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[contains(text(),'" + self.container_registry + "')]").click()
        time.sleep(2)

    def click_next_button(self):
        self.logger.info("****************** go to next page ****************")
        self.driver.find_element(By.XPATH, Locator.next_button_xpath).click()
        time.sleep(2)

    def again_click_next_button(self):
        self.logger.info("****************** again go to next page ****************")
        self.driver.find_element(By.XPATH, Locator.next_button_xpath).click()
        time.sleep(2)

    def Choose_A_Namespace(self):
        self.logger.info("****************** Choose A Namespace for Prod Environment ****************")
        self.driver.find_element(By.XPATH, "//h3[normalize-space()='" + self.namespace_name + "']").click()
        time.sleep(2)

    def click_on_save_button(self):
        self.logger.info("****************** click on save button ****************")
        self.driver.find_element(By.XPATH, Locator.save_button_xpath).click()
        time.sleep(2)

    def click_on_create_application_button(self):
        self.logger.info("****************** click on create application button ****************")
        self.driver.find_element(By.XPATH, Locator.create_application_button_xpath).click()
        time.sleep(2)

    def wait_to_complete_app_creation(self):
        self.logger.info("****************** wait to complete creation ****************")

        try:
            wait_ToCreateApplication = WebDriverWait(self.driver, 800).until(
                EC.visibility_of_element_located((By.XPATH, Locator.wait_ToCreateApplication)))
            if wait_ToCreateApplication.is_displayed():
                time.sleep(4)
                pass
                self.logger.info("****************** The application creation process is complete ****************")
            else:
                pass
                self.logger.info("****************** cross button is not found ****************")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

    # -----------------------------------------Delete Application---------------------------------------------------

    def go_applicationList_page(self):
        self.logger.info("****************** go to application list page ****************")
        self.driver.get(self.baseURL + "applications")
        time.sleep(5)

    def click_application_from_list(self):
        self.logger.info("****************** click on application ****************")
        self.driver.find_element(By.XPATH, "//h3[normalize-space()='" + self.application_name + "']").click()
        time.sleep(5)

    def click_on_settings(self):
        self.logger.info("****************** click on settings ****************")
        self.driver.find_element(By.XPATH, Locator.Namespace_settings).click()
        time.sleep(5)

    def click_on_delete(self):
        self.logger.info("****************** click on delete ****************")
        self.driver.find_element(By.XPATH, Locator.deleteButton_namespace).click()
        time.sleep(5)

    def provide_application_name(self):
        self.logger.info("****************** input application name ****************")
        self.driver.find_element(By.XPATH, Locator.Application_namebox_D).send_keys(self.namespace_name)
        time.sleep(5)

    def click_on_Delete_permanently_button(self):
        self.logger.info("****************** click on submit button ****************")
        self.driver.find_element(By.XPATH, Locator.Delete_permanently_button).click()
        time.sleep(10)

    def validate_namespace_deletion(self):
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
            print("The" + self.application_name + "is not found in the list.")
