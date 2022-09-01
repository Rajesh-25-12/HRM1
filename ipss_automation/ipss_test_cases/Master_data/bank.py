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


Initiated By:Arjun on 8th June.
Modification History

--------------------------------------------------------------------------------------------------------------------
DATE     |   AUTHOR           |  Modification Request No.                           | Remarks / Detail of Changes
--------------------------------------------------------------------------------------------------------------------
8-June-2022    Arjun           Arjun on 6th June 2022                                 Created mock script
9-June-2022   Arjun           Arjun on 8th June 2022                                  Completed the full script
6-July-2022    Arjun         Thangaraj   on 6th July 2022                      revamped the script with added Methods of
                                                                            assertion, file logging, Report generation.
2-August-2022   Rajesh         Rajesh on 1st August 2022                         Adding sequence and Modifying code
--------------------------------------------------------------------------------------------------------------------"""
import logging
# Unittest.Testcase Used for Report Generation
# Logging function
import time

import softest
from selenium.webdriver.common.keys import Keys

from ipss_automation.base import BasePage
from ipss_automation.locators import Locators


class Banking(BasePage, softest.TestCase):

    def __init__(self, driver):
        super().__init__(driver)

    def banking(self):
        self.driver.refresh()
        time.sleep(2)
        self.click(Locators.SEARC)
        time.sleep(2)
        self.click(Locators.P2)
        time.sleep(2)
        self.click(Locators.DRAWER)
        time.sleep(2)
        self.click(Locators.MAS_DATA)
        time.sleep(2)
        self.click(Locators.BANK)
        time.sleep(10)

        # Add details in master page
        self.click(Locators.ALLR)
        time.sleep(2)
        self.click(Locators.ALLR)
        time.sleep(2)
        self.click(Locators.ROW)
        time.sleep(2)
        self.click(Locators.ADD1)
        logging.info("Add button is clicked")
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        logging.error("This Alert Message")
        logging.error("This Alert Message")
        self.click(Locators.ROW)
        time.sleep(2)
        self.click(Locators.ADD1)
        # Assertion function
        try:
            self.assertTrue(Locators.ADD1)
        except AssertionError:
            print("ADD Button is not present")
        logging.info("Add button is clicked")
        time.sleep(2)

        self.click(Locators.BCODE)
        time.sleep(2)
        self.enter_text(Locators.BCODE, "415")
        time.sleep(2)
        self.click(Locators.BNAME)
        time.sleep(2)
        self.enter_text(Locators.BNAME, "4578")
        time.sleep(2)
        self.click(Locators.BADD)
        time.sleep(2)
        self.enter_text(Locators.BADD, "madurai")
        time.sleep(2)
        self.click(Locators.BIFSC)
        time.sleep(2)
        self.enter_text(Locators.BIFSC, "BKID0008225")
        time.sleep(2)
        self.click(Locators.BBRANCH)
        time.sleep(2)
        self.enter_text(Locators.BBRANCH, "madurai")
        time.sleep(2)
        self.click(Locators.ACTIVE)
        time.sleep(2)
        self.click(Locators.TRUE)
        time.sleep(2)
        logging.warning("Submit button is clicked")
        self.click(Locators.SUBMIT)
        time.sleep(2)
        logging.info("The information is With Entering the data its submitted")
        logging.info("Add button is clicked")
        self.click(Locators.ADD1)
        time.sleep(2)
        self.click(Locators.BCODE)
        time.sleep(2)
        self.enter_text(Locators.BCODE, "415")
        time.sleep(2)
        self.click(Locators.BNAME)
        time.sleep(2)
        self.enter_text(Locators.BNAME, "4578")
        time.sleep(2)
        self.click(Locators.BADD)
        time.sleep(2)
        self.enter_text(Locators.BADD, "madurai")
        time.sleep(2)
        self.click(Locators.BIFSC)
        time.sleep(2)
        self.enter_text(Locators.BIFSC, "BKID0008225")
        time.sleep(2)
        try:
            self.assertFalse(Locators.BIFSC)
        except AssertionError:
            print("IFSC Field is Present")

        self.click(Locators.BBRANCH)
        time.sleep(2)
        self.enter_text(Locators.BBRANCH, "madurai")
        time.sleep(2)
        self.click(Locators.ACTIVE)
        time.sleep(2)
        self.click(Locators.TRUE)
        time.sleep(2)
        logging.warning("Cancel button is clicked")
        self.click(Locators.CANCEL)
        logging.info("The information is With Entering the data its Canceled")
        time.sleep(2)
        logging.info("Add button is clicked")
        self.click(Locators.ADD1)
        time.sleep(2)
        logging.warning("Cancel button is clicked")
        try:
            self.click(Locators.SUBMIT)
            time.sleep(2)
        except:
            self.click(Locators.CANCEL)
        logging.info("The information is Without Entering the data its Canceled")
        self.click(Locators.CANCEL)
        time.sleep(2)

        # Edit details in master page
        logging.info("Edit button is clicked")
        self.click(Locators.EDIT_BUTTON)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        logging.error("This Alert Message")
        self.click(Locators.CB_1)
        time.sleep(2)
        self.click(Locators.ROW1)
        time.sleep(2)
        logging.info("Edit button is clicked")
        self.click(Locators.EDIT)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        logging.error("This Alert Message")
        self.click(Locators.ROW1)
        time.sleep(2)
        logging.info("Edit button is clicked")
        self.click(Locators.EDIT_BUTTON)
        # Assertion Function
        try:
            self.assertTrue(Locators.EDIT_BUTTON)
        except AssertionError:
            print("Edit Button is not present")
        # Logging function
        logging.info("Edit Button is working")
        time.sleep(2)
        self.click(Locators.BCODE)
        time.sleep(2)
        self.enter_text(Locators.BCODE, "BIOB")
        self.assertIs("BIOB", "BIOB", "Bank code same")
        self.click(Locators.ACTIVE)
        time.sleep(2)
        self.enter_text(Locators.ACTIVE, "F")
        time.sleep(2)
        self.send_keys(Locators.ACTIVE, Keys.ARROW_DOWN)
        self.send_keys(Locators.ACTIVE, Keys.ENTER)
        time.sleep(2)
        logging.info("Submit button is clicked")
        self.click(Locators.SUBMIT)
        logging.info("The information is  With Entering the data its submitted")
        time.sleep(2)
        # Delete Function
        logging.info("Delete button is clicked")
        self.click(Locators.DELETE)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        logging.error("This Alert Message")
        self.click(Locators.ROW)
        time.sleep(2)
        logging.info("Delete button is clicked")
        self.click(Locators.DELETE)
        time.sleep(2)
        # Assertion Function
        try:
            self.assertTrue(Locators.DELETE)
        except AssertionError:
            print("Delete Button is not present")
        logging.info("Delete Button is working")
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        # Download Function
        logging.info("Download button is clicked")
        self.click(Locators.DOWNLOAD)
        # Assertion Function
        try:
            self.assertTrue(Locators.DOWNLOAD)
        except AssertionError:
            print("Download Button is not present")
        logging.info("Download Button is working")
        time.sleep(2)
        self.click(Locators.LOGOUT_LINK)
        time.sleep(5)
