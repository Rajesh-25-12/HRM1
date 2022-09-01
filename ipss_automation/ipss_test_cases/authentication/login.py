import time
import unittest
import logging
from selenium.webdriver import Keys

from ipss_automation.base import BasePage
from selenium.webdriver.common.by import By
from ipss_automation.locators import Locators
from ipss_automation.utils import get_otp_value


class Login(BasePage,unittest.TestCase):
    """
    Login common module for all user roles.
    """
    def __init__(self, driver):
        super().__init__(driver)

    def do_login(self):
        """
        Click the sign in navigation menu and fill the sign in credentials
        To-Do: Detect if 2FA enabled then fill the 2FA form and submit.
        :return:
        """
        self.driver.maximize_window()
        logging.warning("This is Warning message")
        logging.info("This is info")
        # self.click(Locators.LOGIN_LINK)
        # otp_code = get_otp_value("7373323508")
        # time.sleep(20)
        # self.click(Locators.SUBMI)
        # time.sleep(10)
        # self.send_keys(Locators.CSV, "C:/Users/rajes/Downloads/export (11).csv")
        # time.sleep(10)

        self.enter_text(Locators.USERNAME_INPUT, "ithod@pgc.com")
        time.sleep(2)

        self.enter_text(Locators.PASSWORD_INPUT, "edp123")
        time.sleep(2)
        self.click(Locators.KEEP_BUTTON)
        time.sleep(2)
        self.click(Locators.LOGIN_SUBMIT_BUTTON)
        time.sleep(10)
