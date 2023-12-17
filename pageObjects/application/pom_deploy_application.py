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


class DeployApplication:
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

    # -----------------------------------------Deploy Application---------------------------------------------------

    def go_application_pipeline_page(self):
        application_Id = input("Enter the application Id: ")
        self.driver.get(self.baseURL + "applications/" + application_Id + "/pipeline")
        self.logger.info("opened application's pipeline page")
        time.sleep(8)

    def click_on_pipeline_icon(self):
        self.driver.find_element(By.XPATH, Locator.deploy_icon_xpath).click()
        time.sleep(2)
        self.logger.info("clicked on svg icon")

    def click_on_deploy_button(self):
        self.driver.find_element(By.XPATH, Locator.deploy_button_xpath).click()
        time.sleep(2)
        self.logger.info("clicked on svg icon")

    def click_on_okay_button(self):
        self.driver.find_element(By.XPATH, Locator.okay_button_xpath).click()
        time.sleep(3)
        self.logger.info("clicked on okay button to confirm")

    def wait_to_complete_deployment(self):
        self.logger.info("waiting to complete deployment")

        try:
            wait_to_complete_deploy_xpath = WebDriverWait(self.driver, 800).until(
                EC.visibility_of_element_located((By.XPATH, Locator.wait_to_complete_deploy_xpath)))
            if wait_to_complete_deploy_xpath.is_displayed():
                time.sleep(4)
                pass
                self.logger.info("The application deployment process is complete")
            else:
                pass
                self.logger.info("cross button is not found")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        self.driver.find_element(By.XPATH, Locator.wait_to_complete_deploy_xpath)
        self.logger.info("complete the deployment process")

    def application_deploy_status_check(self):
        try:
            self.driver.find_element(By.XPATH, Locator.deploy_icon_xpath).click()
            self.logger.info("clicked on application deploy icon")
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
                    self.logger.info("deployment Status is None")
                elif status_text == "Success":
                    self.logger.info("deployment Status is None")
                elif status_text == "Timeout":
                    self.logger.info("deployment Status is Timeout")
                else:
                    print(f"Unknown status: {status_text}")
                    self.logger.info(f"Build Status is : {status_text}")

            except Exception as e:
                print(f"Error: {e}")

        except NoSuchElementException as e:
            self.logger.info("NoSuchElementException error", e)
        except TimeoutException as e:
            self.logger.info("TimeoutException error", e)
        except InvalidSessionIdException as e:
            self.logger.info("InvalidSessionIdException error", e)

    def test_application_deployment_by_id(self):
        self.go_application_pipeline_page()
        self.click_on_pipeline_icon()
        self.click_on_deploy_button()
        self.click_on_okay_button()
        self.wait_to_complete_deployment()
        self.application_deploy_status_check()
