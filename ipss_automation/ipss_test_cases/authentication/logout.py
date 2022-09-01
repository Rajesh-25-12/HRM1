import time
import unittest

from ipss_automation.base import BasePage
from selenium.webdriver.common.by import By

from ipss_automation.locators import Locators


class Logout(BasePage,unittest.TestCase):
    """
    Logout common module for all user roles.
    """
    def __init__(self, driver):
        super().__init__(driver)

    def do_logout(self):
        """
        Click the account icon and then click logout link
        :return:
        """
        self.click(Locators.LOGOUT_LINK)
