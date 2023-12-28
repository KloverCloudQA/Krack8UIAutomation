from selenium.common import NoSuchElementException, TimeoutException, WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import logging
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
import utilities.customLogger as cl
from src.Locators.Locators import Locator
from pageObjects.auth.pom_LoginPage import LoginPage


class DeleteApplication:
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
        try:
            self.driver.get(self.baseURL + "applications")
            newApp_button = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='New App']")))
            if newApp_button.is_displayed():
                self.logger.info("opened applications list page")
                time.sleep(2)
        except (TimeoutException, WebDriverException) as e:
            self.logger.error("Timeout or WebDriver exception occurred: {}".format(e))
        # Handle timeout or WebDriver-specific actions
        except Exception as e:
            self.logger.error("An unexpected exception occurred: {}".format(e))
            # Handle other exception

    def click_application_from_list(self):
        try:
            self.logger.info("click on application")
            self.driver.find_element(By.XPATH, "//span[normalize-space()='" + self.application_name + "']").click()
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='CI/CD Pipeline']")))
            time.sleep(2)
        except NoSuchElementException as e:
            self.logger.info("NoSuchElementException error: {}".format(e))
        except Exception as e:
            self.logger.error("An unexpected exception occurred: {}".format(e))
            # Handle other exceptions

    def click_on_settings(self):
        try:
            self.logger.info("click on settings")
            self.driver.find_element(By.XPATH, Locator.application_Settings_xpath).click()
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//h3[normalize-space()='Delete this Application']")))
            time.sleep(1)
        except NoSuchElementException as e:
            self.logger.info("NoSuchElementException error: {}".format(e))
        except Exception as e:
            self.logger.error("An unexpected exception occurred: {}".format(e))
            # Handle other exceptions

    def click_on_delete(self):
        try:
            self.logger.info("click on delete")
            self.driver.find_element(By.XPATH, Locator.application_Delete_button_xpath).click()
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, Locator.application_name_bar_xpath)))
        except NoSuchElementException as e:
            self.logger.info("NoSuchElementException error: {}".format(e))
        except Exception as e:
            self.logger.error("An unexpected exception occurred: {}".format(e))
            # Handle other exceptions

    def provide_application_name(self):
        try:
            self.logger.info("input application name")
            self.driver.find_element(By.XPATH, Locator.application_name_bar_xpath).send_keys(self.application_name)
            time.sleep(1)
        except NoSuchElementException as e:
            self.logger.info("NoSuchElementException error: {}".format(e))
        except Exception as e:
            self.logger.error("An unexpected exception occurred: {}".format(e))
            # Handle other exceptions

    def click_on_Delete_permanently_button(self):
        try:
            self.logger.info("click on submit button")
            self.driver.find_element(By.XPATH, Locator.Delete_permanently_button).click()
            time.sleep(10)
        except NoSuchElementException as e:
            self.logger.info("NoSuchElementException error: {}".format(e))
        except Exception as e:
            self.logger.error("An unexpected exception occurred: {}".format(e))
            # Handle other exceptions

    def validate_application_deletion(self):
        self.logger.info("validate application deletion")

        try:
            self.driver.refresh()
            WebDriverWait(self.driver, 20)
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
        except Exception as e:
            self.logger.error("An unexpected exception occurred: {}".format(e))
            # Handle other exceptions

    def delete_application_from_list(self):
        self.go_applicationList_page()
        self.click_application_from_list()
        self.click_on_settings()
        self.click_on_delete()
        self.provide_application_name()
        self.click_on_Delete_permanently_button()
        self.validate_application_deletion()
