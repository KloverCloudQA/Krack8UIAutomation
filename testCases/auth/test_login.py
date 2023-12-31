import time
import logging
from pageObjects.auth.pom_LoginPage import LoginPage
from utilities.readProperties import ReadConfig
import utilities.customLogger as cl


class TestLogin:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    # logger object
    logger = cl.LogGen.customLogger(logging.DEBUG)

    def test_PageTitle(self, setup):
        self.logger.info("*********************** Verifying Homepage Title *******************")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(5)
        act_title = self.driver.title
        desired_title = "KloverCloud | Sign In"
        if act_title == desired_title:
            assert True
            self.driver.close()
            self.logger.info("*********************** homepage title test is passed *******************")

        else:
            self.driver.save_screenshot(".\\Screenshots\\Login\\" + "test_PageTitle.png")
            self.driver.close()
            self.logger.info("*********************** homepage title test is failed *******************")
            assert False

    def test_successful_login(self, setup):
        self.logger.info("****************** Verifying successfully sign in  with valid credentials ****************")
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(5)
        self.lp.setUserName(self.username)
        time.sleep(2)
        self.lp.setPassword(self.password)
        time.sleep(2)
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

    def test_fun_login(self, setup):
        self.logger.info("****************** Verifying successfully sign in  with valid credentials ****************")
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(5)
        self.lp.logIn()

    def test_easy_fun_login(self, setup):
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.lp.logIn()
