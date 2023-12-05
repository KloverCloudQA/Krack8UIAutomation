from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import logging
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
import utilities.customLogger as cl
from src.Locators.Locators import Locator
from selenium.common.exceptions import NoSuchElementException
from pageObjects.auth.pom_LoginPage import LoginPage


class Namespace:
    # lo = Locator()
    textbox_username_id = Locator.textbox_Email_xpath
    textbox_password_id = Locator.textbox_Password_xpath
    button_login_xpath = Locator.button_SignI_xpath
    Namespace_sidebar = Locator.NamespaceButton_sidebar
    createNew_button = Locator.Create_button_N
    namespace_name_bar = Locator.input_namespaceName
    create_button = Locator.namespace_create_button
    wait_to_show_create_new_button = Locator.Create_button_N
    wait_to_show_namespace_bar = Locator.NamespaceName_bar

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = cl.LogGen.customLogger(logging.DEBUG)

    namespace_name = input("Enter the namespace name: ")

    def __init__(self, driver):
        self.driver = driver

    def logIn(self):
        self.lp = LoginPage(self.driver)
        self.lp.logIn()

    # Click on the "Namespace" link in the sidebar
    def clickNamespace_from_side_bar(self):
        self.driver.find_element(By.XPATH, Locator.NamespaceButton_sidebar).click()

    # Click on the "Create New" button
    def click_createNew_button(self):
        self.driver.find_element(By.XPATH, self.createNew_button).click()

    def wait_to_show_createNew_button(self):
        WebDriverWait(self.driver, 180).until(
            EC.visibility_of_element_located(self.createNew_button))

    def wait_to_show_namespaceBar(self):
        WebDriverWait(self.driver, 180).until(
            EC.visibility_of_element_located(self.wait_to_show_create_new_button))

    # Provide a name for the Namespace
    def setNamespace_name(self, namespace_name):
        self.driver.find_element(By.XPATH, self.namespace_name_bar).clear()
        self.driver.find_element(By.XPATH, self.namespace_name_bar).send_keys(namespace_name)

    # Click on the "Create" button
    def click_create_button(self):
        self.driver.find_element(By.XPATH, self.create_button).click()

    # ---------------------------------------- delete namespace---------------------------------
    def click_namespace(self):
        self.driver.find_element(By.XPATH, "//h3[normalize-space()='hello']").click()

    def go_namespaceList_page(self):
        self.logger.info("****************** go to namespace list page ****************")
        self.driver.get(self.baseURL + "namespace")
        time.sleep(5)

    def click_namespace_from_list(self):
        self.logger.info("****************** click on namespace ****************")
        self.driver.find_element(By.XPATH, "//h3[normalize-space()='" + self.namespace_name + "']").click()
        time.sleep(5)

    def click_on_settings(self):
        self.logger.info("****************** click on settings ****************")
        self.driver.find_element(By.XPATH, Locator.Namespace_settings).click()
        time.sleep(5)

    def click_on_delete(self):
        self.logger.info("****************** click on delete ****************")
        self.driver.find_element(By.XPATH, Locator.deleteButton_namespace).click()
        time.sleep(5)

    def input_namespace_name(self):
        self.logger.info("****************** input namespace name ****************")
        self.driver.find_element(By.XPATH, Locator.Application_namebox_D).send_keys(self.namespace_name)
        time.sleep(5)

    def click_on_Delete_permanently_button(self):
        self.logger.info("****************** click on submit button ****************")
        self.driver.find_element(By.XPATH, Locator.Delete_permanently_button).click()
        time.sleep(10)

    def validate_namespace_deletion(self):
        self.logger.info("****************** validate namespace deletion ****************")

        try:
            self.driver.refresh()
            WebDriverWait(self.driver, 15)
            Namespace = self.driver.find_element(By.XPATH, "//h3[normalize-space()='" + self.namespace_name + "']")

            if not Namespace.is_displayed():
                print("Namespace '" + self.namespace_name + "' is not found")
                assert True
            else:
                print("Namespace '" + self.namespace_name + "' is found")
                assert False

        except NoSuchElementException:
            print("The" + self.namespace_name + "is not found in the list.")
