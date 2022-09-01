""" /* File: Objective: The objective of this page is Automating the file about home page(Bank Master)
of the student module.

Description: This page has Document id,Company code,company name.The Employee Bank details will
                 be here.

                 Also,this page has advanced filter for searching details,sorting option also available which is more
                 useful to sort in an order.Edit,save,delete those function will be used to change or delete the
                 record of the employee, add function is used to add  Details of Employee Bank details.Routing
                 button is to go ahead to detail page for an employee. In that also add,edit,delete,save function
                 will be used. For all these functions I have automated using selenium scripts with all the negative
                 cases.


Initiated By:Bavatharani on 9th June.
Modification History

--------------------------------------------------------------------------------------------------------------------
DATE     |   AUTHOR           |  Modification Request No.                           | Remarks / Detail of Changes
--------------------------------------------------------------------------------------------------------------------
8-June-2022    Bavatharani           Bavatharani on 6th June 2022                                 Created mock script
9-June-2022   Bavatharani           Bavatharani on 8th June 2022                          Completed the full script
6-July-2022    Bavatharani           Thangaraj on 6th July 2022                        revamped the script with added
                                                                                      Methods of assertion, file logging,
                                                                                      Report generation.
2-August-2022   Rajesh         Rajesh on 1st August 2022                             Adding sequence and Modifying code
--------------------------------------------------------------------------------------------------------------------"""
import logging
# Unittest.Testcase Used for Report Generation
# Logging function
import time

import softest
from selenium.webdriver.common.keys import Keys

from ipss_automation.base import BasePage
from ipss_automation.locators import Locators


class Vec(BasePage, softest.TestCase):

    def __init__(self, driver):
        super().__init__(driver)

    def master(self):
        self.driver.refresh()
        time.sleep(2)
        self.click(Locators.SEARC)
        time.sleep(2)
        self.click(Locators.P10)
        time.sleep(2)

        # self.click(Locators.E_VECHILE_PAGE)
        # time.sleep(3)
        # Generate the sequence
        # self.click(Locators.SEQUENCE)
        # time.sleep(2)
        # # Assert function
        # try:
        #     self.assertTrue(Locators.SEQUENCE)
        # except AssertionError:
        #     print("SEQUENCE Button  is not present")
        # logging.info("Sequence Button is working")
        # Adding sequence
        # self.click(Locators.ALLR)
        # time.sleep(2)
        # self.click(Locators.ALLR)
        # time.sleep(2)
        #
        # self.click(Locators.ADD_BUTTON)
        # time.sleep(2)
        # logging.info("ADD Button is working")
        # # Assert function
        # try:
        #     self.assertTrue(Locators.ADD_BUTTON)
        # except AssertionError:
        #     print("ADD Button is present")
        # logging.info("ADD Button is working")
        # time.sleep(2)
        # self.click(Locators.TXT)
        # time.sleep(2)
        # self.click(Locators.D1)
        # time.sleep(2)
        # self.click(Locators.IDTY)
        # time.sleep(2)
        # self.click(Locators.D1)
        # time.sleep(2)
        # self.enter_text(Locators.PREFIX, "PG-")
        # time.sleep(2)
        # self.enter_text(Locators.DESCRIPTION, "PENTAGON")
        # time.sleep(2)
        # self.enter_text(Locators.ZERO_PADDING, "6")
        # time.sleep(2)
        # self.enter_text(Locators.LAST_NO, "0")
        # time.sleep(2)
        # self.click(Locators.ACTVE)
        # time.sleep(2)
        # self.click(Locators.D1)
        # time.sleep(2)
        # self.click(Locators.SUBMIT)
        # time.sleep(2)
        # logging.info("The information is With Entering the data its submitted")
        # self.click(Locators.ADDBUTTON)
        # time.sleep(2)
        # self.click(Locators.TXT)
        # time.sleep(2)
        # self.click(Locators.D1)
        # time.sleep(2)
        # self.click(Locators.IDTY)
        # time.sleep(2)
        # self.click(Locators.D1)
        # time.sleep(2)
        # self.enter_text(Locators.PREFIX, "PG-")
        # time.sleep(2)
        # self.enter_text(Locators.DESCRIPTION, "PENTAGON")
        # time.sleep(2)
        # self.enter_text(Locators.ZERO_PADDING, "6")
        # time.sleep(2)
        # self.enter_text(Locators.LAST_NO, "0")
        # time.sleep(2)
        # self.click(Locators.ACTVE)
        # time.sleep(2)
        # self.click(Locators.D1)
        # time.sleep(2)
        # self.click(Locators.CANCEL)
        # time.sleep(2)
        # self.click(Locators.ADDBUTTON)
        # time.sleep(2)
        # self.click(Locators.SUBMIT)
        # time.sleep(2)
        # self.click(Locators.CANCEL)
        # time.sleep(2)
        # logging.info("The information is WithOut Entering the data its Canceled")
        # # selecting row
        #
        # self.click(Locators.SROW)
        # time.sleep(2)
        # self.click(Locators.EDIT_BUTTON1)
        # time.sleep(2)
        # # Assertion Function
        # try:
        #     self.assertTrue(Locators.EDIT_BUTTON1)
        # except AssertionError:
        #     print("Edit Button is present")
        # logging.info("Edit Button is working")
        # self.click(Locators.ACTVE)
        # time.sleep(2)
        # self.click(Locators.D1)
        # time.sleep(2)
        # self.click(Locators.SUBMIT)
        # time.sleep(2)
        # logging.info("The information is With Entering the data its submitted")
        # self.click(Locators.CANCE)
        # time.sleep(2)
        # # Assertion function
        # try:
        #     self.assertTrue(Locators.CANCE)
        # except AssertionError:
        #     print("Close Button is present")
        # logging.info("Close Button is working")
        # time.sleep(2)
        # Add data in Vehicle page

        logging.info("Add button is clicked")
        self.click(Locators.T_ADD)
        time.sleep(2)
        self.enter_text(Locators.E_DOC_DATE, "08052001")
        time.sleep(2)
        self.click(Locators.E_VECHILE_NO)
        time.sleep(2)
        self.enter_text(Locators.E_VECHILE_NO, "6789")
        time.sleep(3)
        # Assertion Function
        try:
            self.assertFalse(Locators.E_VECHILE_NO)
        except AssertionError:
            print("vehicle no is Present")

        self.click(Locators.E_VECHILE_NAME)
        time.sleep(2)
        self.enter_text(Locators.E_VECHILE_NAME, "Honda")
        time.sleep(3)
        # Assertion Function
        try:
            self.assertFalse(Locators.E_VECHILE_NAME)
        except AssertionError:
            print("vehicle name is Present")

        self.click(Locators.E_VECHILE_TYPE)
        time.sleep(2)
        self.enter_text(Locators.E_VECHILE_TYPE, "Three Wheeler")
        time.sleep(3)
        self.send_keys(Locators.E_VECHILE_TYPE, Keys.ARROW_DOWN)
        time.sleep(2)
        self.send_keys(Locators.E_VECHILE_TYPE, Keys.ENTER)
        time.sleep(2)
        self.click(Locators.E_VECHILE_CATEGORY)
        time.sleep(2)
        self.enter_text(Locators.E_VECHILE_CATEGORY, "Personal")
        time.sleep(3)
        self.send_keys(Locators.E_VECHILE_CATEGORY, Keys.ARROW_DOWN)
        time.sleep(2)
        self.send_keys(Locators.E_VECHILE_CATEGORY, Keys.ENTER)
        time.sleep(2)
        self.click(Locators.E_TRAVEL_NAME)
        time.sleep(2)
        self.enter_text(Locators.E_TRAVEL_NAME, "car")
        time.sleep(1)
        self.click(Locators.E_OWNER_NAME)
        time.sleep(1)
        self.enter_text(Locators.E_OWNER_NAME, "bava")
        time.sleep(1)
        # Assertion Function
        try:
            self.assertIsNot("bava", "bava")
        except AssertionError:
            print("Given name Same")

        self.click(Locators.E_DRIVER_NAME)
        time.sleep(1)
        self.enter_text(Locators.E_DRIVER_NAME, "darani")
        time.sleep(1)
        self.click(Locators.E_VECHILE_ROOT)
        time.sleep(1)
        self.enter_text(Locators.E_VECHILE_ROOT, "kerala")
        time.sleep(1)
        self.click(Locators.E_ROUTE_NO)
        time.sleep(1)
        self.enter_text(Locators.E_ROUTE_NO, "55")
        time.sleep(1)
        self.click(Locators.E_TARGET)
        time.sleep(1)
        self.enter_text(Locators.E_TARGET, "66")
        time.sleep(1)
        self.assertIs("66", "66", "Comparison same")
        self.click(Locators.E_KM)
        time.sleep(1)
        self.enter_text(Locators.E_KM, "3")
        time.sleep(1)
        self.click(Locators.E_RENT)
        time.sleep(1)
        self.enter_text(Locators.E_RENT, "5000")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,50);")
        time.sleep(2)
        logging.info("Save button is clicked")
        self.click(Locators.E_SAVE)
        time.sleep(2)
        self.click(Locators.T_ADD)
        time.sleep(2)
        self.enter_text(Locators.E_DOC_DATE, "08052001")
        time.sleep(2)
        self.click(Locators.E_VECHILE_NO)
        time.sleep(2)
        self.enter_text(Locators.E_VECHILE_NO, "6789")
        time.sleep(3)
        # Assertion Function
        try:
            self.assertFalse(Locators.E_VECHILE_NO)
        except AssertionError:
            print("vehicle no is Present")

        self.click(Locators.E_VECHILE_NAME)
        time.sleep(2)
        self.enter_text(Locators.E_VECHILE_NAME, "Honda")
        time.sleep(3)
        # Assertion Function
        try:
            self.assertFalse(Locators.E_VECHILE_NAME)
        except AssertionError:
            print("vehicle name is Present")

        self.click(Locators.E_VECHILE_TYPE)
        time.sleep(2)
        self.enter_text(Locators.E_VECHILE_TYPE, "Three Wheeler")
        time.sleep(3)
        self.send_keys(Locators.E_VECHILE_TYPE, Keys.ARROW_DOWN)
        time.sleep(2)
        self.send_keys(Locators.E_VECHILE_TYPE, Keys.ENTER)
        time.sleep(2)
        self.click(Locators.E_VECHILE_CATEGORY)
        time.sleep(2)
        self.enter_text(Locators.E_VECHILE_CATEGORY, "Personal")
        time.sleep(3)
        self.send_keys(Locators.E_VECHILE_CATEGORY, Keys.ARROW_DOWN)
        time.sleep(2)
        self.send_keys(Locators.E_VECHILE_CATEGORY, Keys.ENTER)
        time.sleep(2)
        self.click(Locators.E_TRAVEL_NAME)
        time.sleep(2)
        self.enter_text(Locators.E_TRAVEL_NAME, "car")
        time.sleep(1)
        self.click(Locators.E_OWNER_NAME)
        time.sleep(1)
        self.enter_text(Locators.E_OWNER_NAME, "bava")
        time.sleep(1)
        # Assertion Function
        try:
            self.assertIsNot("bava", "bava")
        except AssertionError:
            print("Given name Same")

        self.click(Locators.E_DRIVER_NAME)
        time.sleep(1)
        self.enter_text(Locators.E_DRIVER_NAME, "darani")
        time.sleep(1)
        self.click(Locators.E_VECHILE_ROOT)
        time.sleep(1)
        self.enter_text(Locators.E_VECHILE_ROOT, "kerala")
        time.sleep(1)
        self.click(Locators.E_ROUTE_NO)
        time.sleep(1)
        self.enter_text(Locators.E_ROUTE_NO, "55")
        time.sleep(1)
        self.click(Locators.E_TARGET)
        time.sleep(1)
        self.enter_text(Locators.E_TARGET, "66")
        time.sleep(1)
        self.assertIs("66", "66", "Comparison same")
        self.click(Locators.E_KM)
        time.sleep(1)
        self.enter_text(Locators.E_KM, "3")
        time.sleep(1)
        self.click(Locators.E_RENT)
        time.sleep(1)
        self.enter_text(Locators.E_RENT, "5000")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,50);")
        time.sleep(2)
        self.click(Locators.CLSE)
        time.sleep(2)
        self.click(Locators.T_ADD)
        time.sleep(2)
        self.click(Locators.E_SAVE)
        time.sleep(2)
        self.click(Locators.CLSE)
        time.sleep(2)
        # Edit data in Vehicle page
        logging.info("Edit button is clicked")
        self.click(Locators.T_EDIT_BUTTON)
        time.sleep(3)
        self.driver.switch_to.alert.accept()
        time.sleep(1)
        logging.error("This Alert Message")
        self.click(Locators.T_SELECT_BOX1)
        time.sleep(2)
        logging.info("Edit button is clicked")
        self.click(Locators.T_EDIT_BUTTON)
        time.sleep(3)
        self.enter_text(Locators.E_KM, "3")
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0,50);")
        time.sleep(2)
        # Save function
        logging.info("Save button is clicked")
        self.click(Locators.E_SAVE)
        time.sleep(3)
        self.click(Locators.T_SELECT_BOX1)
        time.sleep(2)
        self.click(Locators.COL3)
        time.sleep(3)
        self.enter_text(Locators.COL3, "TN-95")
        time.sleep(3)
        self.send_keys(Locators.COL3, Keys.ENTER)
        time.sleep(3)
        self.driver.switch_to.alert.accept()
        time.sleep(1)
        # Delete function
        logging.warning("Delete button is clicked")
        self.click(Locators.E_DELETE_BUTTON)
        time.sleep(3)
        self.driver.switch_to.alert.accept()
        time.sleep(1)
        self.click(Locators.T_SELECT_BOX)
        time.sleep(2)
        logging.warning("Delete button is clicked")
        self.click(Locators.E_DELETE_BUTTON)
        time.sleep(3)
        self.driver.switch_to.alert.accept()
        time.sleep(1)
        # Download Function
        logging.info("Download button is clicked")
        self.click(Locators.E_DOWNLOAD)
        time.sleep(3)
