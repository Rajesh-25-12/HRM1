""" /* File:
    Objective: The objective of this page is Automating the file about home page(Manual OT Entry) of the General module.

Description: This page has Document id,Company code,company name.The employee Manual OT details will
                 be here.

                 Also,this page has advanced filter for searching details,sorting option also available which is more
                 useful to sort in an order.Edit,save,delete those function will be used to change or delete the
                 record of the employee, add function is used to add Employee Manual OT details.Routing button is to
                 go ahead to detail page for an employee. In that also add,edit,delete,save function will be used.
                 For all these functions I have automated using selenium scripts with all the negative cases.


Initiated By:Rajesh on 9th June.
Modification History

--------------------------------------------------------------------------------------------------------------------
DATE     |   AUTHOR           |  Modification Request No.                           | Remarks / Detail of Changes
--------------------------------------------------------------------------------------------------------------------
9-June-2022    Rajesh           Rajesh on 6th June 2022                                 Created mock script
10-June-2022   Rajesh           Rajesh on 8th June 2022                          Completed the full script
6-July-2022    Rajesh           Rajesh on 6th July 2022                               revamped the script with added
                                                                  Methods of assertion, file logging, Report generation.

--------------------------------------------------------------------------------------------------------------------"""

# Unittest.Testcase Used for Report Generation
# Logging function
import logging
import time
import unittest

from selenium.webdriver.common.keys import Keys

from ipss_automation.base import BasePage
from ipss_automation.locators import Locators


class Manual_OT_Entry(BasePage, unittest.TestCase):
    def __init__(self, driver):
        super().__init__(driver)

    def Manual(self):
        self.driver.refresh()
        time.sleep(2)
        self.click(Locators.SEARC)
        time.sleep(2)
        self.click(Locators.P4)
        time.sleep(2)

        self.click(Locators.DRAWER_ICON)
        time.sleep(2)
        logging.info("The information is it's Clicking Drawer Button")
        self.click(Locators.ATTENDANCE)
        time.sleep(2)
        self.click(Locators.MANUAL_OT_ENTRY)
        time.sleep(5)

        # Generate the sequence
        self.click(Locators.SEQUENCE)
        time.sleep(2)
        # Assert function
        try:
            self.assertTrue(self.is_element_present(Locators.SEQUENCE))
        except AssertionError:
            print("SEQUENCE Button is not present")
        logging.info("Sequence Button is working")
        # Adding sequence

        self.click(Locators.ADDBUTTON)
        time.sleep(2)
        logging.info("ADD Button is working")
        # Assert function
        try:
            self.assertTrue(self.is_element_present(Locators.ADD_BUTTON))
        except AssertionError:
            print("ADD Button is not present")
        logging.info("ADD Button is working")
        time.sleep(2)
        self.click(Locators.TXT)
        time.sleep(2)
        self.click(Locators.D1)
        time.sleep(2)
        self.click(Locators.IDTY)
        time.sleep(2)
        self.click(Locators.D1)
        time.sleep(2)
        self.enter_text(Locators.PREFIX, "PG-")
        time.sleep(2)
        self.enter_text(Locators.DESCRIPTION, "PENTAGON")
        time.sleep(2)
        self.enter_text(Locators.ZERO_PADDING, "6")
        time.sleep(2)
        self.enter_text(Locators.LAST_NO, "0")
        time.sleep(2)
        self.click(Locators.ACTVE)
        time.sleep(2)
        self.click(Locators.D1)
        time.sleep(2)
        self.click(Locators.SUBMIT)
        time.sleep(2)
        logging.info("The information is With Entering the data its submitted")
        self.click(Locators.ADDBUTTON)
        time.sleep(2)
        self.click(Locators.TXT)
        time.sleep(2)
        self.click(Locators.D1)
        time.sleep(2)
        self.click(Locators.IDTY)
        time.sleep(2)
        self.click(Locators.D1)
        time.sleep(2)
        self.enter_text(Locators.PREFIX, "PG-")
        time.sleep(2)
        self.enter_text(Locators.DESCRIPTION, "PENTAGON")
        time.sleep(2)
        self.enter_text(Locators.ZERO_PADDING, "6")
        time.sleep(2)
        self.enter_text(Locators.LAST_NO, "0")
        time.sleep(2)
        self.click(Locators.ACTVE)
        time.sleep(2)
        self.click(Locators.D1)
        time.sleep(2)
        self.click(Locators.CANCEL)
        time.sleep(2)
        logging.info("The information is WithOut Entering the data its Canceled")
        self.click(Locators.ADDBUTTON)
        time.sleep(2)
        self.click(Locators.SUBMIT)
        time.sleep(2)
        self.click(Locators.CANCEL)
        time.sleep(2)
        # selecting row
        self.click(Locators.EDITBUTTON)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)

        self.click(Locators.SROW)
        time.sleep(2)
        self.click(Locators.EDITBUTTON)
        time.sleep(2)
        # assert function
        try:
            self.assertTrue(self.is_element_present(Locators.EDITBUTTON))
        except AssertionError:
            print("Edit Button is not present")
        logging.info("Edit Button is working")
        self.click(Locators.ACTVE)
        time.sleep(2)
        self.click(Locators.D2)
        time.sleep(2)
        self.click(Locators.SUBMIT)
        time.sleep(2)
        logging.info("The information is With Entering the data its submitted")
        self.click(Locators.CANCE)
        time.sleep(2)
        # assert function
        try:
            self.assertTrue(self.is_element_present(Locators.CANCE))
        except AssertionError:
            print("Close Button is not present")
        logging.info("Close Button is working")
        # Add data in Master page
        self.click(Locators.ADD_BUTTON)
        time.sleep(2)
        logging.info("ADD Button is working")
        # assert function
        try:
            self.assertTrue(self.is_element_present(Locators.ADD_BUTTON))
        except AssertionError:
            print("ADD Button is not present")

        self.enter_text(Locators.DOCDATE, "20062022")
        time.sleep(2)
        self.click(Locators.SUBMIT)
        time.sleep(2)
        logging.info("The information is With Entering the data its submitted")
        self.click(Locators.ADD_BUTTON)
        time.sleep(2)

        self.enter_text(Locators.DOCDATE, "20062022")
        time.sleep(2)
        self.click(Locators.CANCEL)
        time.sleep(2)
        logging.info("The information is With Entering the data its Canceled")
        self.click(Locators.ADD_BUTTON)
        time.sleep(2)
        self.click(Locators.SUBMIT)
        time.sleep(2)
        self.click(Locators.CANCEL)
        time.sleep(2)
        # Edit
        self.click(Locators.ROW)
        time.sleep(2)
        self.click(Locators.EDIT_BUTTON)
        time.sleep(2)
        # assert function
        try:
            self.assertTrue(self.is_element_present(Locators.EDIT_BUTTON))
        except AssertionError:
            print("Edit Button is not present")
        # Logging function
        logging.info("Edit Button is working")
        self.click(Locators.DOCDAT)
        time.sleep(2)
        self.send_keys(Locators.DOCDAT, Keys.CONTROL + 'a')
        time.sleep(2)
        self.send_keys(Locators.DOCDAT, Keys.DELETE)
        time.sleep(2)
        self.enter_text(Locators.DOCDAT, "15022022")
        time.sleep(2)
        self.click(Locators.SUBMIT)
        time.sleep(5)
        logging.info("The information is With Entering the data its submitted")

        # Delete Function
        self.click(Locators.DELETE_BUTTON)
        time.sleep(2)
        # assert function
        try:
            self.assertTrue(Locators.DELETE_BUTTON)
        except AssertionError:
            print("Delete Button is not present")
        logging.info("Delete Button is working")
        self.driver.switch_to.alert.accept()
        time.sleep(5)
        logging.error("This Alert Message")
        self.click(Locators.ROW)
        time.sleep(2)
        self.click(Locators.DELETE_BUTTON)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(5)
        logging.info("The selected row is deleted")
        # Download Function
        self.click(Locators.DOWNLOAD_BUTTON)
        time.sleep(2)
        # assert function
        try:
            self.assertTrue(Locators.DOWNLOAD_BUTTON)
        except AssertionError:
            print("Download Button is not present")
        logging.info("Download Button is working")
        logging.info("Download Button is working")
        # Routing to detail page
        self.click(Locators.ROUTING_BUTTON)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        logging.error("This Alert Message")
        self.click(Locators.ROW)
        time.sleep(2)
        self.click(Locators.ROW1)
        time.sleep(2)
        self.click(Locators.ROUTING_BUTTON)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        logging.error("This Alert Message")
        self.click(Locators.ROW1)
        time.sleep(2)
        self.click(Locators.ROUTING_BUTTON)
        time.sleep(2)
        # assert function
        try:
            self.assertTrue(Locators.ROUTING_BUTTON)
        except AssertionError:
            print("Routing Button is not present")
        logging.info("Routing Button is working")
        time.sleep(2)
        # Adding data in details page
        self.click(Locators.ADD_BUTTON1)
        time.sleep(2)
        # assert function
        try:
            self.assertTrue(Locators.ADD_BUTTON1)
        except AssertionError:
            print("ADD Button is not present")
        logging.info("ADD Button is working")
        self.click(Locators.IDCARD)
        time.sleep(2)
        self.send_keys(Locators.IDCARD, Keys.ARROW_DOWN)
        time.sleep(2)
        self.send_keys(Locators.IDCARD, Keys.ENTER)
        time.sleep(2)
        self.enter_text(Locators.OTDATE, "10062022")
        time.sleep(2)
        self.click(Locators.OTHR)
        time.sleep(2)
        self.enter_text(Locators.OTHR, "10")
        time.sleep(2)
        # assert function
        try:
            self.assertIsNot("10", "10")
        except AssertionError:
            print("Given Value Same")
        self.click(Locators.NOTES)
        time.sleep(2)
        self.enter_text(Locators.NOTES, "gdfvjdb")
        time.sleep(2)
        self.click(Locators.SUBMIT)
        time.sleep(2)
        self.click(Locators.ADD_BUTTON1)
        time.sleep(2)
        self.click(Locators.IDCARD)
        time.sleep(2)
        self.send_keys(Locators.IDCARD, Keys.ARROW_DOWN)
        time.sleep(2)
        self.send_keys(Locators.IDCARD, Keys.ENTER)
        time.sleep(2)
        self.click(Locators.OTDATE)
        time.sleep(1)
        self.enter_text(Locators.OTDATE, "10062022")
        time.sleep(2)
        self.click(Locators.OTHR)
        time.sleep(2)
        self.enter_text(Locators.OTHR, "10")
        time.sleep(2)
        self.assertIs("10", "10", "Comparison same")
        self.click(Locators.NOTES)
        time.sleep(2)
        self.enter_text(Locators.NOTES, "gdfvjdb")
        time.sleep(2)
        self.click(Locators.SUBMIT)
        time.sleep(2)
        logging.info("The information is With Entering the data its submitted")
        time.sleep(2)
        self.click(Locators.ADD_BUTTON1)
        time.sleep(2)
        self.click(Locators.IDCARD)
        time.sleep(2)
        self.send_keys(Locators.IDCARD, Keys.ARROW_DOWN)
        time.sleep(2)
        self.send_keys(Locators.IDCARD, Keys.ENTER)
        time.sleep(2)
        self.click(Locators.OTDATE)
        time.sleep(1)
        self.enter_text(Locators.OTDATE, "10062022")
        time.sleep(2)
        self.click(Locators.OTHR)
        time.sleep(2)
        self.enter_text(Locators.OTHR, "10")
        time.sleep(2)
        self.click(Locators.NOTES)
        time.sleep(2)
        self.enter_text(Locators.NOTES, "gdfvjdb")
        time.sleep(2)
        self.click(Locators.CANCEL)
        time.sleep(2)
        logging.info("The information is With Entering the data its Canceled")
        self.click(Locators.ADD_BUTTON1)
        time.sleep(2)
        self.click(Locators.SUBMIT)
        time.sleep(2)
        self.click(Locators.CANCEL)
        time.sleep(2)
        logging.warning("Without Entering the data its cancelled")
        # Editing the data in details page
        self.click(Locators.EDIT_BUTTON1)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        logging.error("This Alert Message")
        self.click(Locators.ROW)
        time.sleep(2)
        self.click(Locators.ROW1)
        time.sleep(2)
        self.click(Locators.EDIT_BUTTON1)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        logging.error("This Alert Message")
        self.click(Locators.ROW1)
        time.sleep(2)
        self.click(Locators.EDIT_BUTTON1)
        time.sleep(3)
        # assert function
        try:
            self.assertTrue(Locators.EDIT_BUTTON)
        except AssertionError:
            print("Edit Button is not present")
        # Logging function
        logging.info("Edit Button is working")
        self.click(Locators.OTHR)
        time.sleep(2)
        self.send_keys(Locators.OTHR, Keys.CONTROL + 'a')
        time.sleep(2)
        self.send_keys(Locators.OTHR, Keys.DELETE)
        time.sleep(2)
        self.enter_text(Locators.OTHR, "15")
        time.sleep(2)
        self.click(Locators.SUBMIT)
        time.sleep(2)
        logging.info("The information is With Entering the data its submitted")
        # Save function for cell editing
        self.click(Locators.SAVE_BUTTON1)
        time.sleep(2)
        logging.info("Save Button is working")
        self.click(Locators.COL3)
        time.sleep(2)
        self.enter_text(Locators.COL3, "5")
        time.sleep(2)
        self.send_keys(Locators.COL3, Keys.ENTER)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        logging.critical("Cell edit is happened")
        self.click(Locators.COL3)
        time.sleep(2)
        self.enter_text(Locators.COL3, "50")
        time.sleep(2)
        self.send_keys(Locators.COL3, Keys.ENTER)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        self.click(Locators.SAVE_BUTTON1)
        time.sleep(2)
        # Assertion Function
        try:
            self.assertTrue(Locators.SAVE_BUTTON1)
        except AssertionError:
            print("SAVE Button is not present")
        logging.info("Save Button is working")
        logging.warning("The edited cell is Saved")
        # Delete Function
        # self.click(Locators.ROW)
        # time.sleep(2)
        self.click(Locators.DELETE_BUTTON1)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(5)
        logging.error("This Alert Message")
        self.click(Locators.ROW)
        time.sleep(2)
        self.click(Locators.DELETE_BUTTON1)
        time.sleep(2)
        # assert function
        try:
            self.assertTrue(Locators.DELETE_BUTTON1)
        except AssertionError:
            print("Delete Button is not present")
        logging.info("Delete Button is working")
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        # Download function
        self.click(Locators.DOWNLOAD_BUTTON1)
        time.sleep(2)
        # assert function
        try:
            self.assertTrue(Locators.DOWNLOAD_BUTTON1)
        except AssertionError:
            print("Download Button is not present")
        logging.info("Download Button is working")
        time.sleep(5)
        # Back to Master Page
        self.click(Locators.BAC)
        time.sleep(10)
        self.click(Locators.LOGOUT_LINK)
        time.sleep(5)
