import logging

from pageObjects.user_section.pom_user_creation import UserCreation
from utilities.readProperties import ReadConfig
import utilities.customLogger as cl


class Test_New_User_Creation:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    # logger object
    logger = cl.LogGen.customLogger(logging.DEBUG)

    def test_simple_nonAdmin_user_creation(self, setup):
        self.logger.info("****************** start user creation ****************")
        self.driver = setup
        self.ob = UserCreation(self.driver)
        self.ob.logIn()  # login
        self.ob.simple_nonAdmin_user_creation()  # simple non admin user creation without team and role

    def test_nonAdmin_user_creation_with_team(self, setup):
        self.logger.info("****************** start nonAdmin user creation with team ****************")
        self.driver = setup
        self.ob = UserCreation(self.driver)
        self.ob.logIn()  # login
        self.ob.nonAdmin_user_creation_with_team()

    def test_nonAdmin_user_creation_with_role(self, setup):
        self.logger.info("****************** start Non Admin user creation with role ****************")
        self.driver = setup
        self.ob = UserCreation(self.driver)
        self.ob.logIn()  # login
        self.ob.nonAdmin_user_creation_with_role()

    def test_nonAdmin_user_creation_with_team_and_role(self, setup):
        self.logger.info("****************** start Non Admin user creation with team and role ****************")
        self.driver = setup
        self.ob = UserCreation(self.driver)
        self.ob.logIn()  # login
        self.ob.nonAdmin_user_creation_with_team_and_role()

    def test_secondaryAdmin_user_creation(self, setup):
        self.logger.info("****************** Start Secondary Admin user creation ****************")
        self.driver = setup
        self.ob = UserCreation(self.driver)
        self.ob.logIn()  # login
        self.ob.secondaryAdmin_user_creation()  # admin user creation
