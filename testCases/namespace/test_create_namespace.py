import time
import logging
from pageObjects.namespace.pom_Namespace import Namespace
from utilities.readProperties import ReadConfig
import utilities.customLogger as cl


class Test_Create_Namespace:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    # logger object
    logger = cl.LogGen.customLogger(logging.DEBUG)

    namespace_name = input("Enter the namespace name: ")

    def test_fixed_namespace_creation(self, setup):
        self.logger.info("****************** Verifying successfully sign in  with valid credentials ****************")
        self.driver = setup
        self.lp = Namespace(self.driver)
        self.logger.info("****************** go to login page ****************")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(5)
        self.logger.info("****************** set username ****************")
        self.lp.setUserName(self.username)
        time.sleep(2)
        self.logger.info("****************** set password ****************")
        self.lp.setPassword(self.password)
        time.sleep(2)
        self.logger.info("****************** click on signin button ****************")
        self.lp.clickLogin()
        time.sleep(10)
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
        self.logger.info("****************** go to namespace creation form ****************")
        self.driver.get(self.baseURL + "namespace/create")
        time.sleep(5)
        self.logger.info("****************** input namespace name ****************")
        self.lp.setUserName(self.namespace_name)
        time.sleep(2)
        self.logger.info("****************** click on create button ****************")
        self.lp.click_create_button()
        time.sleep(10)

        self.driver.refresh()
        time.sleep(2)
