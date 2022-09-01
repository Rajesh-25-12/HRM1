import time
from unittest import TestCase
import unittest

from ipss_automation.base import BasePage
from selenium.webdriver.common.keys import Keys
from ipss_automation.locators import Locators


class Payroll (BasePage,TestCase):

    def _init_(self, driver):
        super().__init__(driver)

    def Payrollp (self):
            self.click(Locators.P_DRAWER)
            time.sleep(3)
            self.click(Locators.P_PAYROLL_MASTER)
            time.sleep(3)
            self.click(Locators.P_PAY_STRUCTURE)
            time.sleep(3)
            self.click(Locators.P_ADD)
            time.sleep(3)
            self.enter_text(Locators.P_COMPANY_CODE,"12345")
            time.sleep(3)
            self.enter_text(Locators.P_DOCUMENT_DATE,"20.6.2000")
            time.sleep(3)
            self.enter_text(Locators.P_FINANCIAL_YEAR, "2000")
            time.sleep(3)
            self.enter_text(Locators.P_PAYMENT_CATEGORY, "34")
            time.sleep(3)
            self.enter_text(Locators.P_TYPE_BUTTON, "45")
            time.sleep(3)
            self.click(Locators.P_SUBMIT_BUTTON)
            time.sleep(3)
            self.click(Locators.P_ADD)
            time.sleep(3)
            self.enter_text(Locators.P_COMPANY_CODE, "12345")
            time.sleep(3)
            self.enter_text(Locators.P_DOCUMENT_DATE, "20.6.2000")
            time.sleep(3)
            self.enter_text(Locators.P_FINANCIAL_YEAR, "2000")
            time.sleep(3)
            self.enter_text(Locators.P_PAYMENT_CATEGORY, "34")
            time.sleep(3)
            self.enter_text(Locators.P_TYPE_BUTTON, "45")
            time.sleep(3)
            self.click(Locators.P_CANCEL_BUTTON)
            time.sleep(3)
            self.click(Locators.P_ADD)
            time.sleep(3)
            self.click(Locators.P_CANCEL_BUTTON)
            time.sleep(3)
            self.click(Locators.P_SELECT_BOX)
            time.sleep(3)
            self.click(Locators.P_EDIT_BUTTON)
            time.sleep(3)
            self.enter_text(Locators.P_FINANCIAL_YEAR, "2000")
            time.sleep(3)
            self.click(Locators.P_SUBMIT_BUTTON)
            time.sleep(3)
            self.click(Locators.P_SELECT_BOX)
            time.sleep(3)
            self.enter_text(Locators.P_BOX_BUTTON,"78")
            time.sleep(3)
            self.click(Locators.P_SAVE_BUTTON)
            time.sleep(3)
            self.click(Locators.P_SELECT_BOX)
            time.sleep(3)
            self.click(Locators.P_DELETE_BUTTON)
            time.sleep(3)
            self.driver.switch_to.alert.accept()
            time.sleep(3)
            self.click(Locators.P_SELECT_BOX)
            time.sleep(3)
            self.click(Locators.P_DOWNLOAD_BUTTON)
            time.sleep(3)
            self.click(Locators.P_SELECT_BOX)
            self.click((Locators.P_SELECT_BOX1))
            time.sleep(3)
            self.click(Locators.P_ROUTE)
            time.sleep(3)
            self.click(Locators.P_ADD_BUTTON)
            time.sleep(3)
            self.enter_text(Locators.P_PAY_CODE,"78")
            time.sleep(3)
            self.enter_text(Locators.P_EARNED_CODE,"123")
            time.sleep(3)
            self.enter_text(Locators.P_PAY_DESCRIPTION,"123")
            time.sleep(3)
            self .enter_text(Locators.P_PICK_FORM,"hi")
            time.sleep(3)
            self.enter_text(Locators.P_FORMULA,"+%*")
            time.sleep(3)
            self.enter_text(Locators.P_NOTES,"jjj")
            time.sleep(3)
            self.click(Locators.P_SUBMIT_BUTTON)
            time.sleep(3)
            self.click(Locators.P_BOX_BUTTON)
            time.sleep(2)
            self.enter_text(Locators.P_BOX_BUTTON, "8552")
            time.sleep(2)
            self.send_keys(Locators.P_BOX_BUTTON,Keys.ENTER)
            time.sleep(2)
            self.click(Locators.P_SAVE_BUTTON)
            time.sleep(3)
            self.click(Locators.P_SELECT_BOX)
            time.sleep(3)
            self.click(Locators.P_DELETE_BUTTON)
            time.sleep(3)
            self.driver.switch_to.alert.accept()
            time.sleep(3)
            self.click(Locators.P_SELECT_BOX)
            time.sleep(3)
            self.click(Locators.P_DOWNLOAD_BUTTON1)
            time.sleep(3)



























