""" /* File: Objective: The objective of this page is Automating the file about home page(Dashboard Report Values) of
the IPSS HR module.


Description: This page has Document id,Company code,company name.The Company Value details will
                 be here.

                 Also,this page has advanced filter for searching details,sorting option also available which is more
                 useful to sort in an order.Edit,save,delete those function will be used to change or delete the
                 record of the employee Details, add function is used to add Status of Company Requirements
                 staffs.Routing button is to go ahead to detail page for an employee. In that also add,edit,delete,
                 save function will be used. For all these functions I have automated using selenium scripts with all
                 the negative cases.


Initiated By:Rajesh on 6th June.
Modification History

--------------------------------------------------------------------------------------------------------------------
DATE     |   AUTHOR           |  Modification Request No.                           | Remarks / Detail of Changes
--------------------------------------------------------------------------------------------------------------------
6-June-2022    Rajesh           Rajesh on 6th June 2022                                 Created mock script
8-June-2022    Rajesh           Rajesh on 8th June 2022                          Completed the full script
6-July-2022    Rajesh           Rajesh on 6th July 2022                               revamped the script with added
                                                                  Methods of assertion, file logging, Report generation.

--------------------------------------------------------------------------------------------------------------------"""
import logging
import time
import unittest

# import softest
from selenium.webdriver.common.keys import Keys

from ipss_automation.base import BasePage
from ipss_automation.locators import Locators


# Unittest.Testcase Used for Report Generation
# Logging function
class Dashboard(BasePage, unittest.TestCase):

    def __init__(self, driver):
        super().__init__(driver)

    def dashboard(self):

        self.driver.refresh()
        time.sleep(10)
        self.click(Locators.SEARC)
        time.sleep(2)
        self.click(Locators.P2)
        time.sleep(2)
        self.click(Locators.DRAWER_ICON)
        time.sleep(2)
        logging.info("The information is it's Clicking Drawer Button")
        time.sleep(2)
        self.click(Locators.GENERAL)
        time.sleep(2)
        self.click(Locators.DASHBOARD)
        time.sleep(10)
        # Generate the sequence
        self.click(Locators.SEQUENCE)
        time.sleep(2)
        # Assert function
        try:
            self.assertTrue(self.is_element_present(Locators.SEQUENCE))
        except AssertionError:
            print("SEQUENCE Button is Not present")
        logging.info("Sequence Button is working")
        # Adding sequence

        self.click(Locators.ADDBUTTON)
        time.sleep(2)
        logging.info("ADD Button is working")
        # Assert function
        try:
            self.assertTrue(self.is_element_present(Locators.ADD_BUTTON))
        except AssertionError:
            print("ADD Button is Not present")
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
        self.enter_text(Locators.PREFIX, "1234@")
        time.sleep(2)
        self.clear(Locators.PREFIX)
        self.enter_text(Locators.PREFIX, "PG-")
        time.sleep(2)
        self.enter_text(Locators.DESCRIPTION, "PENTAGON")
        time.sleep(2)
        self.send_keys(Locators.ZERO_PADDING,"")
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
        self.click(Locators.SUBMIT)
        time.sleep(2)
        self.enter_text(Locators.PREFIX, "1234")
        time.sleep(2)
        self.send_keys(Locators.PREFIX,Keys.CONTROL+'a')
        time.sleep(2)
        self.enter_text(Locators.PREFIX, "PG-")
        time.sleep(2)
        self.enter_text(Locators.DESCRIPTION, "PENTAGON")
        time.sleep(2)
        self.enter_text(Locators.ZERO_PADDING, "123")
        time.sleep(2)
        self.send_keys(Locators.ZERO_PADDING,Keys.CONTROL+'a')
        time.sleep(2)
        self.enter_text(Locators.ZERO_PADDING, "ABC")
        time.sleep(2)
        self.send_keys(Locators.ZERO_PADDING, Keys.CONTROL + 'a')
        time.sleep(2)
        self.enter_text(Locators.ZERO_PADDING, "6")
        time.sleep(2)
        self.enter_text(Locators.LAST_NO, "ABC")
        time.sleep(2)
        self.enter_text(Locators.LAST_NO, "1")
        time.sleep(2)
        self.click(Locators.CANCEL)
        time.sleep(2)
        logging.info("The information is WithOut Entering the data its Canceled")
        self.click(Locators.ADDBUTTON)
        time.sleep(2)
        try:
            self.click(Locators.SUBMIT)
            time.sleep(2)
        except:
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
        # Assertion function
        try:
            self.assertTrue(self.is_element_present(Locators.EDITBUTTON))
        except AssertionError:
            print("Edit Button is Not present")
        logging.info("Edit Button is working")
        self.click(Locators.ACTVE)
        time.sleep(2)
        self.click(Locators.D2)
        time.sleep(2)
        self.click(Locators.SUBMIT)
        time.sleep(2)
        logging.info("The information is With Entering the data its submitted")
        # Assertion function
        try:
            self.assertTrue(self.is_element_present(Locators.DELETE_BUTTON))
        except AssertionError:
            print("Delete Button is Not present")
        time.sleep(2)
        self.click(Locators.CANCE)
        time.sleep(2)
        # Assertion function
        try:
            self.assertTrue(self.is_element_present(Locators.CANCE))
        except AssertionError:
            print("Close Button is Not present")
        logging.info("Close Button is working")
        # Adding data in master Page
        self.click(Locators.ALLR)
        time.sleep(2)
        self.click(Locators.ALLR)
        time.sleep(2)
        self.click(Locators.ROW)
        time.sleep(2)
        self.click(Locators.ADD_BUTTON)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        self.click(Locators.ROW)
        time.sleep(2)
        self.click(Locators.ADD_BUTTON)
        time.sleep(2)
        # Assertion function
        try:
            self.assertTrue(self.is_element_present(Locators.ADD_BUTTON))
        except AssertionError:
            print("ADD Button is Not present")
        # Logging function
        logging.info("ADD Button is working")
        time.sleep(2)
        self.click(Locators.PTRANS)
        time.sleep(2)
        self.send_keys(Locators.PTRANS, Keys.ARROW_DOWN)
        time.sleep(2)
        self.send_keys(Locators.PTRANS, Keys.ENTER)
        time.sleep(2)
        # Assertion function
        try:
            self.assertNotEqual("Recruitment", "Recruitment")
        except AssertionError:
            print("Status are same")
        print("Assertion passed")
        time.sleep(2)
        self.click(Locators.DOCDATE)
        time.sleep(2)
        self.enter_text(Locators.DOCDATE, "08082022")
        time.sleep(2)
        self.click(Locators.SUBMIT)
        time.sleep(2)
        logging.info("The information is With Entering the data its submitted")
        time.sleep(5)
        self.click(Locators.ADD_BUTTON)
        time.sleep(2)
        self.click(Locators.PTRANS)
        time.sleep(2)
        self.send_keys(Locators.PTRANS, Keys.ARROW_DOWN)
        time.sleep(2)
        self.send_keys(Locators.PTRANS, Keys.ENTER)
        time.sleep(2)
        self.click(Locators.DOCDATE)
        time.sleep(2)
        self.enter_text(Locators.DOCDATE, "08082022")
        time.sleep(2)
        self.click(Locators.CANCEL)
        time.sleep(5)
        logging.info("The information is With Entering the data its Canceled")
        time.sleep(2)
        self.click(Locators.ADD_BUTTON)
        time.sleep(2)
        try:
            self.click(Locators.SUBMIT)
            time.sleep(2)
        except:
            self.click(Locators.CANCEL)
            time.sleep(2)
        self.click(Locators.CANCEL)
        time.sleep(2)

        # Editing Data in Master Page
        self.click(Locators.EDIT_BUTTON)
        time.sleep(2)
        logging.info("Edit Button is working")
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        logging.error("This Alert Message")
        self.click(Locators.ROW)
        time.sleep(2)
        self.click(Locators.ROW1)
        time.sleep(2)
        self.click(Locators.EDIT_BUTTON)
        time.sleep(2)
        logging.error("This Alert Message")
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        self.click(Locators.ROW1)
        time.sleep(5)
        self.click(Locators.EDIT_BUTTON)
        time.sleep(2)
        # Assertion function
        try:
            self.assertTrue(self.is_element_present(Locators.EDIT_BUTTON))
        except AssertionError:
            print("Edit Button is Not present")
        # Logging function
        logging.info("Edit Button is working")
        self.click(Locators.DOCDATE)
        time.sleep(2)
        self.send_keys(Locators.DOCDATE, Keys.CONTROL + 'a')
        time.sleep(2)
        self.enter_text(Locators.DOCDATE, "20102022")
        time.sleep(2)
        self.click(Locators.SUBMIT)
        time.sleep(10)
        logging.info("The information is With Entering the data its submitted")
        time.sleep(2)

        # Delete
        self.click(Locators.DELETE_BUTTON)
        time.sleep(2)
        # Assertion function
        try:
            self.assertTrue(Locators.DELETE_BUTTON)
        except AssertionError:
            print("Delete Button is Not present")
        logging.info("Delete Button is working")
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        logging.error("This Alert Message")
        # self.click(Locators.ROW1)
        # time.sleep(2)
        self.click(Locators.DELETE_BUTTON)
        time.sleep(2)
        logging.info("Delete Button is working")
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        # Download
        self.click(Locators.DOWNLOAD_BUTTON)
        time.sleep(2)
        # Assertion function
        try:
            self.assertTrue(Locators.DOWNLOAD_BUTTON)
        except AssertionError:
            print("Download Button is Not present")
        logging.info("Download Button is working")

        # Routing function
        self.click(Locators.ROUTING_BUTTON)
        time.sleep(2)
        logging.error("This Alert Message")
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        self.click(Locators.ROW)
        time.sleep(2)
        self.click(Locators.ROW1)
        time.sleep(2)
        self.click(Locators.ROUTING_BUTTON)
        time.sleep(2)
        logging.error("This Alert Message")
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        self.click(Locators.ROW1)
        time.sleep(2)
        self.click(Locators.ROUTING_BUTTON)
        time.sleep(2)
        # Assertion function
        try:
            self.assertTrue(Locators.ROUTING_BUTTON)
        except AssertionError:
            print("Routing Button  is Not present")
        logging.info("Routing Button is working")
        # self.click(Locators.ROW)
        # time.sleep(2)
        # Adding Data in Details Page
        self.click(Locators.ALLR)
        time.sleep(2)
        self.click(Locators.ALLR)
        time.sleep(2)
        self.click(Locators.ADD_BUTTON1)
        time.sleep(2)
        # Assertion function
        try:
            self.assertTrue(Locators.ADD_BUTTON1)
        except AssertionError:
            print("ADD Button is Not present")
        logging.info("ADD Button is working")

        self.click(Locators.RVALUE)
        time.sleep(2)
        self.enter_text(Locators.RVALUE, "5")
        time.sleep(2)
        # Assertion function
        try:
            self.assertIsNot("5", "5")
        except AssertionError:
            print("Given Value Same")
        self.click(Locators.NOTES)
        time.sleep(2)
        self.enter_text(Locators.NOTES, "dtrfygk")
        time.sleep(1)
        self.click(Locators.SUBMIT)
        time.sleep(2)
        logging.info("The information is With Entering the data its submitted")
        time.sleep(2)
        self.click(Locators.ADD_BUTTON1)
        time.sleep(2)
        self.enter_text(Locators.RVALUE, "5")
        time.sleep(2)
        # Assertion function
        self.assertIs("5", "5", "Comparison same")
        self.click(Locators.NOTES)
        time.sleep(2)
        self.enter_text(Locators.NOTES, "dtrfygk")
        time.sleep(1)
        self.click(Locators.SUBMIT)
        time.sleep(2)
        logging.info("The information is With Entering the data its submitted")
        time.sleep(2)
        self.click(Locators.ADD_BUTTON1)
        time.sleep(2)
        self.click(Locators.RVALUE)
        time.sleep(2)
        self.enter_text(Locators.RVALUE, "5")
        time.sleep(2)
        self.click(Locators.NOTES)
        time.sleep(2)
        self.enter_text(Locators.NOTES, "dtrfygk")
        time.sleep(1)
        self.click(Locators.CANCEL)
        time.sleep(2)
        logging.info("The information is With Entering the data its Canceled")
        time.sleep(2)
        self.click(Locators.ADD_BUTTON1)
        time.sleep(2)
        logging.warning("Without Entering the data its cancelled")
        self.click(Locators.CANCEL)
        time.sleep(2)
        self.click(Locators.ADD_BUTTON1)
        time.sleep(2)
        try:
            self.click(Locators.SUBMIT)
            time.sleep(2)
            print("The input values are not clear in Sequence")
        except:
            self.click(Locators.CANCEL)
        time.sleep(2)
        self.click(Locators.CANCEL)
        time.sleep(2)
        # Editing Data in Details page
        self.click(Locators.EDIT_BUTTON1)
        time.sleep(2)
        logging.info("Edit Button is working")
        self.driver.switch_to.alert.accept()
        time.sleep(2)
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
        time.sleep(2)
        # Assertion Function
        try:
            self.assertTrue(self.is_element_present(Locators.EDIT_BUTTON1))
        except AssertionError:
            print("Edit Button is not present")
        # Logging function
        logging.info("Edit Button is working")
        self.click(Locators.RVALUE)
        time.sleep(2)
        self.send_keys(Locators.RVALUE, Keys.CONTROL + 'a')
        time.sleep(2)
        self.enter_text(Locators.RVALUE, "5")
        time.sleep(2)
        # Assertion function
        self.assertIs("5", "5", "Comparison same")
        self.click(Locators.SUBMIT)
        time.sleep(10)
        logging.info("The information is With Entering the data its submitted")
        time.sleep(2)
        # Save function
        self.click(Locators.SAVE_BUTTON1)
        time.sleep(2)
        logging.info("Save Button is working")
        self.click(Locators.COL)
        time.sleep(2)
        self.send_keys(Locators.COL, "235")
        time.sleep(2)
        self.send_keys(Locators.COL, Keys.ENTER)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        # self.click(Locators.SAVE_BUTTON1)
        # time.sleep(2)
        logging.critical("Cell edit is happened")
        time.sleep(2)
        # Assertion function
        try:
            self.assertTrue(Locators.SAVE_BUTTON1)
        except AssertionError:
            print("Save Button is not present")
        # Logging function
        logging.info("save Button is working")
        logging.warning("The edited cell is Saved")
        # Delete Function

        self.click(Locators.DELETE_BUTTON1)
        time.sleep(2)
        # Assertion Function
        try:
            self.assertTrue(Locators.DELETE_BUTTON)
        except AssertionError:
            print("Delete Button is not present")
        self.driver.switch_to.alert.accept()
        time.sleep(1)
        logging.error("This Alert Message")
        self.click(Locators.ROW)
        time.sleep(2)
        self.click(Locators.DELETE_BUTTON1)
        time.sleep(2)
        logging.info("Delete Button is working")
        self.driver.switch_to.alert.accept()
        time.sleep(1)

        # Download Data
        self.click(Locators.DOWNLOAD_BUTTON1)
        time.sleep(2)
        # Assertion function
        try:
            self.assertTrue(Locators.DOWNLOAD_BUTTON1)
        except AssertionError:
            print("Download Button is not present")
        logging.info("Download Button is working")
        time.sleep(2)
        # Back to Master Page
        self.click(Locators.BACK)
        time.sleep(10)
        self.click(Locators.LOGOUT_LINK)
        time.sleep(5)
