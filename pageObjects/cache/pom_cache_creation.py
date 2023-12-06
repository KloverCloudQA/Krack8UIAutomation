from selenium.common import NoSuchElementException, TimeoutException, InvalidSessionIdException
from selenium.webdriver.support.ui import WebDriverWait
import time
import logging
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
import utilities.customLogger as cl
from src.Locators.Locators import Locator
from pageObjects.auth.pom_LoginPage import LoginPage
from selenium.webdriver.support import expected_conditions as EC


class CacheCreation:
    baseURL = ReadConfig.getApplicationURL()

    # logger object
    logger = cl.LogGen.customLogger(logging.DEBUG)
    # ---------------------------------------locators--------------------------------------------------------
    cache_framework_radis = Locator.cache_framework_redis_xpath
    dropdown_team_list = Locator.dropdown_team_list_xpath
    textbox_cache_server_name = Locator.textbox_cache_server_name_xpath
    textbox_initial_admin_password_cache = Locator.textbox_initial_admin_password_cache_xpath
    textbox_confirm_password_cache = Locator.textbox_confirm_password_cache_xpath
    dropdown_version_list_cache = Locator.dropdown_version_list_cache_xpath
    checkbox_add_storage_cache = Locator.checkbox_add_storage_cache_xpath
    checkbox_enable_web_client_cache = Locator.checkbox_enable_web_client_cache_xpath
    textbox_web_client_username_cache = Locator.textbox_web_client_username_cache_xpath
    textbox_web_client_password_cache = Locator.textbox_web_client_password_cache_xpath
    checkbox_enable_snapshot_service_cache = Locator.checkbox_enable_snapshot_service_cache_xpath
    button_next = Locator.button_next_cache_xpath
    button_confirm = Locator.button_confirm_cache_xpath
    button_cache_status = Locator.button_cache_status_xpath

    # database_framework = input("Choose the database framework by typing Mysql/Postgresql/Mongodb : ")
    cache_name = input("Input your cache name : ")
    namespace_name = input("Choose the namespace by typing actual namespace name : ")
    initial_admin_password = input("Input your initial_admin_password : ")

    def __init__(self, driver):
        self.driver = driver

    def logIn(self):
        self.lp = LoginPage(self.driver)
        self.lp.logIn()

    # -----------------------------------------cache creation---------------------------------------------------

    def go_to_create_cache_page(self):
        self.driver.get(self.baseURL + "cache/create")
        time.sleep(5)
        self.logger.info("opened cache creation page")

    def cache_framework(self):
        self.driver.find_element(By.XPATH, self.cache_framework_radis).click()
        self.logger.info(f"cache framework chosen as Redis")
        time.sleep(4)

    def set_access_team(self):
        # Get user input
        user_input = input("Do you want to set a team? (y/n): ")
        if user_input.lower() == 'y':
            access_team_name = input("Choose the access team by typing actual team name default/team1/team2--- : ")
            # Wait for the team-box to be clickable
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.dropdown_team_list)))

            # Click the team box to show list
            element.click()
            time.sleep(2)
            self.logger.info("team list shown")
            self.driver.find_element(By.XPATH, "//span[normalize-space()='" + access_team_name + "']").click()
            self.logger.info(f"access team chosen as : {access_team_name}")
            time.sleep(1)
            try:
                namespace = WebDriverWait(self.driver, 30).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, "//h3[@class='vpc__name' and text()='" + self.namespace_name + "']")))
                if namespace.is_displayed():
                    time.sleep(2)
                    pass
                else:
                    self.logger.info("Namespace not found")
                    self.driver.close()
            except NoSuchElementException as e:
                print("NoSuchElementException error", e)
            except TimeoutException as e:
                print("TimeoutException error", e)
            except InvalidSessionIdException as e:
                print("InvalidSessionIdException error", e)

    def set_namespace(self):
        self.driver.find_element(By.XPATH, "//h3[@class='vpc__name' and text()='" + self.namespace_name + "']").click()
        self.logger.info(f"namespace chosen as : {self.namespace_name}")
        time.sleep(2)

    def set_cache_server_name(self):
        self.driver.find_element(By.XPATH, self.textbox_cache_server_name).send_keys(self.cache_name)
        self.logger.info(f"cache server name inputted as : {self.cache_name}")
        time.sleep(1)

    def set_initial_admin_password(self):
        self.driver.find_element(By.XPATH, self.textbox_initial_admin_password_cache).send_keys(
            self.initial_admin_password)
        self.logger.info(f"cache initial admin password inputted as: {self.initial_admin_password}")
        time.sleep(1)

    def set_confirm_password(self):
        self.driver.find_element(By.XPATH, self.textbox_confirm_password_cache).send_keys(self.initial_admin_password)
        self.logger.info(f"confirm password inputted as: {self.initial_admin_password}")
        time.sleep(1)

    def click_on_next_button(self):
        next_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.button_next)))
        next_button.click()
        self.logger.info(f"went to the next page")
        time.sleep(3)

    def click_on_button_confirm(self):
        self.driver.find_element(By.XPATH, self.button_confirm).click()
        self.logger.info("clicked on confirm button")
        time.sleep(3)

    def choose_add_storage_checkbox(self):
        # Get user input
        user_input = input("Do you want to choose 'Add Storage'? (y/n): ")
        # If the user chooses to add storage
        if user_input.lower() == 'y':
            self.driver.find_element(By.XPATH, self.checkbox_add_storage_cache).click()
            time.sleep(2)
            self.logger.info("'Add Storage' chosen")

    def choose_Enable_Web_Client_checkbox(self):
        # Get user input
        user_input = input("Do you want to enable the web client feature? (y/n): ")
        if user_input.lower() == 'y':
            self.driver.find_element(By.XPATH, self.checkbox_enable_web_client_cache).click()
            time.sleep(2)
            self.logger.info("'Enable Web Client' chosen")
            web_client_username = input("Input your web_client_username : ")
            web_client_password = input("Input your web_client_password : ")

            try:
                self.driver.find_element(By.XPATH, self.textbox_web_client_username_cache).send_keys(
                    web_client_username)
                time.sleep(1)
                self.logger.info(f"inputted webclient user name : {web_client_username}")
                self.driver.find_element(By.XPATH, self.textbox_web_client_password_cache).send_keys(web_client_password)
                time.sleep(1)
                self.logger.info(f"inputted webclient password : {web_client_password}")
            except Exception as e:
                self.logger.info(f"Exception: {e}")
                self.logger.info("Element not found within the timeout.")
                # Add more debug information if needed

    def choose_enable_snapshot_service_checkbox(self):
        # Get user input
        user_input = input("Do you want to enable the snapshot service? (y/n): ")
        # If the user choose to enable the snapshot service
        if user_input.lower() == 'y':
            self.driver.find_element(By.XPATH, self.checkbox_enable_snapshot_service_cache).click()
            time.sleep(2)
            self.logger.info("'enabled snapshot service' chosen")

    def wait_to_complete_cache_creation(self):
        self.logger.info("wait for a while complete creation")

        try:
            wait_ToCreateApplication = WebDriverWait(self.driver, 180).until(
                EC.visibility_of_element_located((By.XPATH, self.button_cache_status)))
            if wait_ToCreateApplication.is_displayed():
                time.sleep(4)
                pass
                self.logger.info("cache creation process is completed")
            else:
                pass
                self.logger.info("status button is not found")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

    def simple_cache_creation(self):
        self.logger.info("Starting a simple cache creation")
        self.go_to_create_cache_page()
        self.cache_framework()
        self.set_namespace()
        self.set_cache_server_name()
        self.set_initial_admin_password()
        self.set_confirm_password()
        self.click_on_next_button()
        self.click_on_next_button()
        self.click_on_button_confirm()
        self.wait_to_complete_cache_creation()

    def advanced_database_cluster_creation(self):
        self.logger.info("Starting a simple database creation")
        self.go_to_create_cache_page()
        self.cache_framework()
        self.set_access_team()
        self.set_namespace()
        self.set_cache_server_name()
        self.set_initial_admin_password()
        self.set_confirm_password()
        self.choose_add_storage_checkbox()
        self.choose_Enable_Web_Client_checkbox()
        self.choose_enable_snapshot_service_checkbox()
        self.click_on_next_button()
        self.click_on_next_button()
        self.click_on_button_confirm()
        self.wait_to_complete_cache_creation()
