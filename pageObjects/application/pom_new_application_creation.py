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

    # web_framework_name = input("Enter the web framework name: ")
    application_name = input("Enter the application name: ")
    git_account = input("Enter git account name: ")
    container_registry = input("Enter container_registry name: ")
    namespace_name = input("Enter namespace name: ")

    def __init__(self, driver):
        self.driver = driver

    def logIn(self):
        self.lp = LoginPage(self.driver)
        self.lp.logIn()

    def go_to_create_new_application_page(self):
        self.driver.get(self.baseURL + "applications/new")
        self.logger.info("opened application creation page")
        time.sleep(5)

    def choose_webapp_framework(self):
        try:
            while True:
                user_input = input("Enter the webapp framework (java/javascript/python/c#/php/golang): ")

                if user_input.lower() == 'java':
                    self.driver.find_element(By.XPATH, self.button_webframework_springBoot).click()
                    self.logger.info(f"webapp framework chosen as: {user_input}")
                    time.sleep(1)
                    break
                elif user_input.lower() == 'javascript':
                    self.driver.find_element(By.XPATH, self.button_webframework_ExpressJS).click()
                    self.logger.info(f"webapp framework chosen as: {user_input}")
                    time.sleep(1)
                    break
                elif user_input.lower() == 'python':
                    self.driver.find_element(By.XPATH, self.button_webframework_Django).click()
                    self.logger.info(f"webapp framework chosen as: {user_input}")
                    time.sleep(1)
                    break
                elif user_input.lower() == 'c#':
                    self.driver.find_element(By.XPATH, self.button_webframework_DotNet).click()
                    self.logger.info(f"webapp framework chosen as: {user_input}")
                    time.sleep(1)
                    break
                elif user_input.lower() == 'php':
                    self.driver.find_element(By.XPATH, self.button_webframework_Laravel).click()
                    self.logger.info(f"webapp framework chosen as: {user_input}")
                    time.sleep(1)
                    break
                elif user_input.lower() == 'golang':
                    self.driver.find_element(By.XPATH, self.button_webframework_Golang).click()
                    self.logger.info(f"web app framework chosen as: {user_input}")
                    time.sleep(1)
                    break
                else:
                    print("Invalid web framework. Please type same as (java/javascript/python/c#/php/golang)")

        except NoSuchElementException as e:
            self.logger.info("NoSuchElementException error", e)
        except TimeoutException as e:
            self.logger.info("TimeoutException error", e)

    def input_application_name(self):
        try:
            self.driver.find_element(By.XPATH, Locator.Application_Name_bar_xpath).send_keys(self.application_name)
            time.sleep(1)
            self.logger.info(f"inputted application name as {self.application_name}")
        except NoSuchElementException as e:
            self.logger.info("NoSuchElementException error", e)

    def set_access_team(self):
        # Get user input
        user_input = input("Do you want to set a team access control? (y/n): ")
        if user_input.lower() == 'y':
            try:
                access_team_name = input("Choose the access team by typing actual team name default/team1/team2--- : ")

                # Wait for the team-box to be clickable
                element = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.dropdown_team_bar)))

                # Click the team box to show list
                element.click()
                time.sleep(2)
                self.logger.info("team list shown")
                self.driver.find_element(By.XPATH, "//span[normalize-space()='" + access_team_name + "']").click()
                self.logger.info(f"access team chosen as : {access_team_name}")
                time.sleep(1)

            except NoSuchElementException as e:
                self.logger.info("NoSuchElementException error", e)
            except TimeoutException as e:
                self.logger.info("TimeoutException error", e)
            except InvalidSessionIdException as e:
                self.logger.info("InvalidSessionIdException error", e)

    def choose_git_account(self):
        try:
            self.driver.find_element(By.XPATH, Locator.git_account_bar_xpath).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//span[contains(text(),'" + self.git_account + "')]").click()
            time.sleep(2)
            self.logger.info(f"git account chosen as : {self.git_account}")

        except NoSuchElementException as e:
            self.logger.info("NoSuchElementException error", e)
        except InvalidSessionIdException as e:
            self.logger.info("InvalidSessionIdException error", e)

    def choose_container_registry(self):
        try:
            self.driver.find_element(By.XPATH, Locator.container_registry_bar_xpath).click()
            time.sleep(2)

            # # Find all the registry names using XPath
            # registry_elements = self.driver.find_elements(By.XPATH, "//span[@class='ng-tns-c33-317 ng-star-inserted']")
            #
            # # Extract and print the registry names
            # registry_names = [element.text for element in registry_elements]
            # for name in registry_names:
            #     print(name)
            #     time.sleep(2)

            self.driver.find_element(By.XPATH, "//span[contains(text(),'" + self.container_registry + "')]").click()
            time.sleep(2)
            self.logger.info(f"container registry chosen as {self.container_registry}")

        except NoSuchElementException as e:
            self.logger.info("NoSuchElementException error", e)
        except InvalidSessionIdException as e:
            self.logger.info("InvalidSessionIdException error", e)

    def application_build_trigger_mode(self):
        self.logger.info("application_build_trigger_mode manual")
        user_input = input("Do you want change application trigger mode Manual (y/n): ")
        if user_input.lower() == 'y':
            try:
                # Wait for the team-box to be clickable
                element = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.checkbox_application_build_trigger_mode_manual)))

                # Click the team box to show list
                element.click()
                time.sleep(1)
            except NoSuchElementException as e:
                self.logger.info("NoSuchElementException error", e)
            except InvalidSessionIdException as e:
                self.logger.info("InvalidSessionIdException error", e)
            except TimeoutException as e:
                self.logger.info("TimeoutException error", e)

    def click_next_button(self):
        try:
            self.driver.find_element(By.XPATH, Locator.next_button_xpath).click()
            time.sleep(1)
            self.logger.info("clicked on next button")
        except NoSuchElementException as e:
            self.logger.info("NoSuchElementException error", e)
        except InvalidSessionIdException as e:
            self.logger.info("InvalidSessionIdException error", e)

    def again_click_next_button(self):
        try:
            self.driver.find_element(By.XPATH, Locator.next_button_xpath).click()
            time.sleep(1)
            self.logger.info("clicked on next button")
        except NoSuchElementException as e:
            self.logger.info("NoSuchElementException error", e)
        except InvalidSessionIdException as e:
            self.logger.info("InvalidSessionIdException error", e)

    def Choose_A_Namespace(self):
        try:
            self.driver.find_element(By.XPATH, "//h3[normalize-space()='" + self.namespace_name + "']").click()
            time.sleep(2)
            self.logger.info(f"Namespace chosen as {self.namespace_name}")
        except NoSuchElementException as e:
            self.logger.info("NoSuchElementException error", e)
        except InvalidSessionIdException as e:
            self.logger.info("InvalidSessionIdException error", e)

    def choose_enable_persistent_volume_checkbox(self):
        # Get user input
        user_input = input("Do you want to choose 'Enable Persistent Volume'? (y/n): ")
        # If the user choose to enable the snapshot service
        if user_input.lower() == 'y':
            try:
                self.driver.find_element(By.XPATH, self.checkbox_Enable_Persistent_Volume).click()
                self.logger.info("Enable Persistent Volume' chosen")
            except NoSuchElementException as e:
                self.logger.info("NoSuchElementException error", e)
            except InvalidSessionIdException as e:
                self.logger.info("InvalidSessionIdException error", e)

    def choose_enable_in_memory_volume_non_persistent_checkbox(self):
        # Get user input
        user_input = input("Do you want to choose 'Enable In-Memory Volume(Non-Persistent)'? (y/n): ")
        # If the user choose to enable the snapshot service
        if user_input.lower() == 'y':
            try:
                self.driver.find_element(By.XPATH, self.checkbox_Enable_In_Memory_Volume_Non_Persistent).click()
                self.logger.info("Enable In-Memory Volume(Non-Persistent)' chosen")
                mount_paths = input("Now Input your mount paths (/home/kc/cache) : ")
                self.driver.find_element(By.XPATH, self.textbox_In_Memory_Volume_Mount_Paths_Non_Persistent).send_keys(
                    mount_paths)
                time.sleep(1)
                self.logger.info(f"inputted mount path as : {mount_paths}")
            except NoSuchElementException as e:
                self.logger.info("NoSuchElementException error", e)
            except InvalidSessionIdException as e:
                self.logger.info("InvalidSessionIdException error", e)

    def choose_enable_auto_scaling_checkbox(self):
        # Get user input
        user_input = input("Do you want to choose 'Enable Auto Scaling'? (y/n): ")
        # If the user choose to enable the snapshot service
        if user_input.lower() == 'y':
            try:
                self.driver.find_element(By.XPATH, self.checkbox_Enable_Auto_Scaling).click()
                self.logger.info("Enable Auto Scaling' chosen")
                self.driver.find_element(By.XPATH, self.checkbox_CPU_Threshold).click()
                self.logger.info("CPU threshold chose by default")
                time.sleep(1)
            except NoSuchElementException as e:
                self.logger.info("NoSuchElementException error", e)
            except InvalidSessionIdException as e:
                self.logger.info("InvalidSessionIdException error", e)

    def choose_enable_basic_auth_for_external_access_url_checkbox(self):
        # Get user input
        user_input = input("Do you want to choose 'Enable Basic Auth for External Access Url'? (y/n): ")
        # If the user choose to enable the snapshot service
        if user_input.lower() == 'y':
            try:
                self.driver.find_element(By.XPATH, self.checkbox_Enable_Basic_Auth).click()
                self.logger.info("Enable Basic Auth for External Access Url' chosen")
                username = input("Input your basic auth username minimum 6 characters : ")
                password = input("Input your basic auth password : ")
                try:
                    self.driver.find_element(By.XPATH, self.textbox_basic_auth_username).send_keys(username)
                    time.sleep(1)
                    self.logger.info(f"inputted username : {username}")
                    self.driver.find_element(By.XPATH, self.textbox_basic_auth_password).send_keys(password)
                    time.sleep(1)
                    self.logger.info(f"inputted password : {password}")
                except Exception as e:
                    self.logger.info(f"Exception: {e}")
                    self.logger.info("Element not found within the timeout.")
                    # Add more debug information if needed
            except NoSuchElementException as e:
                self.logger.info("NoSuchElementException error", e)
            except InvalidSessionIdException as e:
                self.logger.info("InvalidSessionIdException error", e)

    def click_on_save_button(self):
        try:
            self.driver.find_element(By.XPATH, Locator.save_button_xpath).click()
            time.sleep(1)
            self.logger.info("clicked on save button")

        except NoSuchElementException as e:
            self.logger.info("NoSuchElementException error", e)
        except InvalidSessionIdException as e:
            self.logger.info("InvalidSessionIdException error", e)

    def click_on_create_application_button(self):
        try:
            self.driver.find_element(By.XPATH, Locator.create_application_button_xpath).click()
            time.sleep(2)
            self.logger.info("clicked on 'Create application button'")
        except NoSuchElementException as e:
            self.logger.info("NoSuchElementException error", e)
        except InvalidSessionIdException as e:
            self.logger.info("InvalidSessionIdException error", e)

    def wait_to_complete_app_creation(self):
        self.logger.info("wait to complete creation")

        try:
            wait_ToCreateApplication = WebDriverWait(self.driver, 800).until(
                EC.visibility_of_element_located((By.XPATH, Locator.icon_application_build_xpath)))
            if wait_ToCreateApplication.is_displayed():
                time.sleep(3)
                self.logger.info("The application creation process is complete")
                assert True
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

    def wait_to_complete_app_build(self):
        self.logger.info("wait to complete application build")

        try:
            wait_ToCreateApplication = WebDriverWait(self.driver, 800).until(
                EC.visibility_of_element_located((By.XPATH, Locator.wait_ToCreateApplication)))
            if wait_ToCreateApplication.is_displayed():
                time.sleep(4)
                pass
                self.logger.info("The application build process is complete")
            else:
                pass
                self.logger.info("cross button is not found")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

    def application_build_status_check(self):
        try:
            self.logger.info("application_build_trigger_mode")
            self.driver.find_element(By.XPATH, Locator.icon_application_build_xpath).click()
            self.logger.info("clicked on application build pipeline icon")
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
                    self.logger.info("Build Status is None")
                elif status_text == "Success":
                    self.logger.info("Build Status is None")
                elif status_text == "Timeout":
                    self.logger.info("Build Status is Timeout")
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

    def scrape_all_container_registry_name(self):
        try:
            # Find all the registry names using XPath
            registry_elements = self.driver.find_elements(By.XPATH, "//span[@class='ng-tns-c33-317 ng-star-inserted']")

            # Extract and print the registry names
            registry_names = [element.text for element in registry_elements]
            for name in registry_names:
                print(name)
        except NoSuchElementException as e:
            self.logger.info("NoSuchElementException error", e)
        except TimeoutException as e:
            self.logger.info("TimeoutException error", e)
        except InvalidSessionIdException as e:
            self.logger.info("InvalidSessionIdException error", e)

    def new_application_creation(self):
        self.go_to_create_new_application_page()
        self.choose_webapp_framework()
        self.input_application_name()
        self.choose_git_account()
        self.choose_container_registry()
        self.click_next_button()
        self.again_click_next_button()
        self.Choose_A_Namespace()
        self.click_on_save_button()
        self.click_on_create_application_button()
        self.wait_to_complete_app_creation()

    def application_build_trigger_test_by_create_new_app(self):
        self.go_to_create_new_application_page()
        self.choose_webapp_framework()
        self.input_application_name()
        self.choose_git_account()
        self.choose_container_registry()
        self.set_access_team()
        self.application_build_trigger_mode()
        self.click_next_button()
        self.again_click_next_button()
        self.Choose_A_Namespace()
        self.click_on_save_button()
        self.click_on_create_application_button()
        self.wait_to_complete_app_creation()
        self.application_build_status_check()

    def application_creation_with_advanced_feature(self):
        self.go_to_create_new_application_page()
        self.choose_webapp_framework()
        self.input_application_name()
        self.choose_git_account()
        self.choose_container_registry()
        self.set_access_team()
        self.application_build_trigger_mode()
        self.click_next_button()
        self.again_click_next_button()
        self.Choose_A_Namespace()
        self.choose_enable_persistent_volume_checkbox()
        self.choose_enable_in_memory_volume_non_persistent_checkbox()
        self.choose_enable_auto_scaling_checkbox()
        self.choose_enable_basic_auth_for_external_access_url_checkbox()
        self.click_on_save_button()
        self.click_on_create_application_button()
        self.wait_to_complete_app_creation()
        self.application_build_status_check()
