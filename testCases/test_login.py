import time

import pytest
from selenium import webdriver
# from pageObjects.LoginPage import Login


class Test_001_Login:
    baseURL = "https://console.kc-cp.klovercloud.io/auth/login"
    username = "admin@yourstore.com"
    password = "admin"

    def test_homePageTitle(self, setup):
        self.driver = setup

        # try:
        self.driver.get(self.baseURL)
        time.sleep(5)
        act_title = self.driver.title
        desired_title = "KloverCloud | Sign In"
        assert act_title == desired_title
