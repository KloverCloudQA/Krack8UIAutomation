from selenium.common import NoSuchElementException
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

    textbox_username_id = Locator.textbox_Email_xpath
    textbox_password_id = Locator.textbox_Password_xpath
    button_login_xpath = Locator.button_SignI_xpath

    application_name = input("Enter the application name: ")

    def __init__(self, driver):
        self.driver = driver

    def logIn(self):
        self.lp = LoginPage(self.driver)
        self.lp.logIn()

    # -----------------------------------------Delete Application---------------------------------------------------

    def go_applicationList_page(self):
        self.logger.info("go to application list page")
        self.driver.get(self.baseURL + "applications")
        time.sleep(5)

    def click_application_from_list(self):
        self.logger.info("click on application")
        self.driver.find_element(By.XPATH, "//span[normalize-space()='" + self.application_name + "']").click()
        time.sleep(5)

    def click_on_settings(self):
        self.logger.info("click on settings")
        self.driver.find_element(By.XPATH, Locator.application_Settings_xpath).click()
        time.sleep(5)

    def click_on_delete(self):
        self.logger.info("click on delete")
        self.driver.find_element(By.XPATH, Locator.application_Delete_button_xpath).click()
        time.sleep(5)

    def provide_application_name(self):
        self.logger.info("input application name")
        self.driver.find_element(By.XPATH, Locator.application_name_bar_xpath).send_keys(self.application_name)
        time.sleep(5)

    def click_on_Delete_permanently_button(self):
        self.logger.info("click on submit button")
        self.driver.find_element(By.XPATH, Locator.Delete_permanently_button).click()
        time.sleep(10)

    def validate_application_deletion(self):
        self.logger.info("validate application deletion")

        try:
            self.driver.refresh()
            WebDriverWait(self.driver, 15)
            application = self.driver.find_element(By.XPATH,
                                                   "//span[normalize-space()='" + self.application_name + "']")

            if not application.is_displayed():
                print("Namespace '" + self.application_name + "' is not found")
                assert True
            else:
                print("Namespace '" + self.application_name + "' is found")
                assert False

        except NoSuchElementException:
            print("\nThe " + self.application_name + "application is not found in the list.")
