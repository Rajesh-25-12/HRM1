import time
from unittest import TestCase
import unittest

from ipss_automation.base import BasePage
from selenium.webdriver.common.keys import Keys
from ipss_automation.locators import Locators


class Village(BasePage,unittest.TestCase):

    def _init_(self, driver):
        super().__init__(driver)

    def masterdata(self):
     self.click(Locators.V_DRAWER)
     time.sleep(3)
     self.click(Locators.V_MASTER_DATA)
     time.sleep(3)
     self.click(Locators.V_VILLAGE)
     time.sleep(3)
     self.click(Locators.V_SELECT_BOX)
     time.sleep(3)
     self.click(Locators.V_ADD)
     time.sleep(3)
     self.enter_text(Locators.V_VILLAGE_NAME,"theni")
     time.sleep(3)
     self.click(Locators.V_DROP_DOWN)
     time.sleep(3)
     self.click(Locators.V_CHOOSE_DROP)
     time.sleep(3)
     self.click(Locators.V_SUBMIT_BUTTON)
     time.sleep(3)
     self.click(Locators.V_SELECT_BOX)
     time.sleep(3)
     self.click(Locators.V_EDIT_BUTTON)
     time.sleep(3)
     self.enter_text(Locators.V_VILLAGE_NAME, "vellore")
     time.sleep(3)
     self.click(Locators.V_SUBMIT_BUTTON)
     time.sleep(3)
     self.click(Locators.V_SELECT_BOX)
     time.sleep(3)
     self.click(Locators.V_ADD)
     time.sleep(3)
     self.enter_text(Locators.V_VILLAGE_NAME,"kovai")
     time.sleep(3)
     self.click(Locators.V_DROP_DOWN)
     time.sleep(3)
     self.click(Locators.V_CHOOSE_DROP)
     time.sleep(3)
     self.click(Locators.V_CANCEL_BUTTON)
     time.sleep(3)
     self.click(Locators.V_SELECT_BOX)
     time.sleep(3)
     self.click(Locators.V_ADD)
     time.sleep(3)
     self.click(Locators.V_CANCEL_BUTTON)
     time.sleep(3)
     self.click(Locators.V_SELECT_BOX)
     time.sleep(3)
     self.click(Locators.V_DELETE_BUTTON)
     time.sleep(3)
     self.driver.switch_to.alert.accept()
     time.sleep(3)
     self.click(Locators.V_SELECT_BOX)
     time.sleep(3)
     self.click(Locators.V_UPLOAD_BUTTON)
     time.sleep(3)
     self.click(Locators.V_SELECT_BOX)
     time.sleep(3)
     self.click(Locators.V_EXPORT_BUTTON)
     time.sleep(3)
     self.click(Locators.V_SELECT_BOX)
     time.sleep(3)
     self.click(Locators.V_SELECT_BOX1)
     time.sleep(3)
     self.click(Locators.V_EDIT_BUTTON)
     time.sleep(3)
     self.driver.switch_to.alert.accept()
     time.sleep(3)
     self.click(Locators.V_SELECT_BOX)
     time.sleep(3)
     self.enter_text(Locators.V_BOX_BUTTON,"karur")
     time.sleep(3)
     self.send_keys(Locators.V_BOX_BUTTON,Keys.ENTER)
     time.sleep(3)
     self.click(Locators.V_SAVE_BUTTON)
     time.sleep(3)

















