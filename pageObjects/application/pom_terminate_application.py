from selenium.common import NoSuchElementException, TimeoutException, InvalidSessionIdException, WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import logging
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
import utilities.customLogger as cl
from src.Locators.Locators import Locator
from pageObjects.auth.pom_LoginPage import LoginPage


class TerminateApplication:
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

    def logIn(self):
        self.lp = LoginPage(self.driver)
        self.lp.logIn()

    # -----------------------------------------Restart Application---------------------------------------------------

    def go_application_pipeline_page(self):
        try:
            application_Id = input("Enter the application Id: ")
            self.driver.get(self.baseURL + "applications/" + application_Id + "/pipeline")
            ci_cd_pipeline = WebDriverWait(self.driver, 800).until(
                EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='CI/CD Pipeline']")))
            if ci_cd_pipeline.is_displayed():
                self.logger.info("opened application's CI/CD pipeline page")
                time.sleep(2)
        except (TimeoutException, WebDriverException) as e:
            self.logger.error("Timeout or WebDriver exception occurred: {}".format(e))
        # Handle timeout or WebDriver-specific actions
        except Exception as e:
            self.logger.error("An unexpected exception occurred: {}".format(e))
            # Handle other exceptions

    def click_on_pipeline_icon(self):
        try:
            self.driver.find_element(By.XPATH, Locator.deploy_icon_xpath).click()
            time.sleep(2)
            self.logger.info("clicked on svg icon")
        except NoSuchElementException as e:
            self.logger.info("NoSuchElementException error", e)
        except Exception as e:
            self.logger.error("An unexpected exception occurred: {}".format(e))
            # Handle other exceptions

    def click_on_terminate_button(self):
        try:
            self.driver.find_element(By.XPATH, Locator.button_terminate_application_xpath).click()
            time.sleep(2)
            self.logger.info("clicked on terminate")
        except NoSuchElementException as e:
            self.logger.info("NoSuchElementException error", e)
        except Exception as e:
            self.logger.error("An unexpected exception occurred: {}".format(e))
            # Handle other exceptions

    def click_on_terminate_button_to_confirm(self):
        try:
            self.driver.find_element(By.XPATH, "//span[@class='ng-star-inserted']").click()
            time.sleep(2)
            self.logger.info("clicked on terminate button to confirm")
        except NoSuchElementException as e:
            self.logger.info("NoSuchElementException error", e)
        except Exception as e:
            self.logger.error("An unexpected exception occurred: {}".format(e))
            # Handle other exceptions

    def wait_to_complete_terminate(self):
        self.logger.info("start waiting to complete terminate")
        try:
            wait_to_complete_deploy_xpath = WebDriverWait(self.driver, 800).until(
                EC.visibility_of_element_located((By.XPATH, Locator.wait_to_complete_deploy_xpath)))
            if wait_to_complete_deploy_xpath.is_displayed():
                time.sleep(4)
                pass
                self.logger.info("The application terminate process is complete")
            else:
                pass
                self.logger.info("cross button is not found")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)
        self.logger.info("complete the restarting process")

    def application_terminate_status_check(self):
        try:
            self.driver.find_element(By.XPATH, Locator.deploy_icon_xpath).click()
            self.logger.info("clicked on application terminate icon")
            time.sleep(1)
            self.driver.find_element(By.XPATH, Locator.button_application_build_info_xpath).click()
            self.logger.info("clicked info button")
            time.sleep(1)
            try:
                status_element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//p[@class='m-0 body-1']"))
                )
                status_text = status_element.text.strip()

                if status_text == "None":
                    print("Status is None.")
                    self.logger.info("terminate Status is None")
                elif status_text == "Success":
                    self.logger.info("terminate Status is None")
                elif status_text == "Timeout":
                    self.logger.info("terminate Status is Timeout")
                else:
                    print(f"Unknown status: {status_text}")
                    self.logger.info(f"terminate Status is : {status_text}")

            except Exception as e:
                self.logger.error(f"Error: {e}")
                print(f"Error: {e}")

        except NoSuchElementException as e:
            self.logger.error("NoSuchElementException error: {}".format(e))
        except TimeoutException as e:
            self.logger.error("TimeoutException error: {}".format(e))
        except InvalidSessionIdException as e:
            self.logger.error("InvalidSessionIdException error: {}".format(e))
        except Exception as e:
            self.logger.error("An unexpected exception occurred: {}".format(e))
            # Handle other exceptions

    def test_terminate_application(self):
        self.go_application_pipeline_page()
        self.click_on_pipeline_icon()
        self.click_on_terminate_button()
        self.click_on_terminate_button_to_confirm()
        self.wait_to_complete_terminate()
        self.application_terminate_status_check()

