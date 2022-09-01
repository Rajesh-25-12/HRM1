""" /* File: Objective: The objective of this page is Automating the file about home page(Security Buyer Attendance)
of the student module.

Description: This page has Document id,Company code,company name.The security Employee Attendance details will
                 be here.

                 Also,this page has advanced filter for searching details,sorting option also available which is more
                 useful to sort in an order.Edit,save,delete those function will be used to change or delete the
                 record of the employee, add function is used to add security Employee Attendance details.Routing
                 button is to go ahead to detail page for an employee. In that also add,edit,delete,save function
                 will be used. For all these functions I have automated using selenium scripts with all the negative
                 cases.


Initiated By:Arjun on 6th June.
Modification History

--------------------------------------------------------------------------------------------------------------------
DATE     |   AUTHOR           |  Modification Request No.                           | Remarks / Detail of Changes
--------------------------------------------------------------------------------------------------------------------
9-June-2022    Arjun           Arjun on 6th June 2022                                 Created mock script
10-June-2022   Arjun           Arjun on 8th June 2022                          Completed the full script
6-July-2022    Arjun           Thangaraj on 6th July 2022                               revamped the script with added
                                                                  Methods of assertion, file logging, Report generation.
2-August-2022   Rajesh         Rajesh on 1st August 2022                             Adding sequence and Modifying code
--------------------------------------------------------------------------------------------------------------------"""
import logging
# Unittest.Testcase Used for Report Generation
# Logging function
import time
# import softest
import unittest

from selenium.webdriver.common.keys import Keys

from ipss_automation.base import BasePage

from ipss_automation.locators import Locators


class Security_buyer(BasePage, unittest.TestCase):

    def __init__(self, driver):
        super().__init__(driver)

    def security(self):

        self.click(Locators.SEARC)
        time.sleep(2)
        self.click(Locators.P4)
        time.sleep(2)
        self.click(Locators.DRAWER)
        time.sleep(2)
        self.click(Locators.ATTENDANECE)
        time.sleep(2)
        self.click(Locators.SECURITY_BUYER)
        time.sleep(10)
        # Add details in master page
        self.click(Locators.ALLR)
        time.sleep(2)
        self.click(Locators.ALLR)
        time.sleep(2)
        self.click(Locators.ROW)
        time.sleep(2)
        self.click(Locators.ADD)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        logging.error("This Alert Message")
        self.click(Locators.ROW)
        time.sleep(2)
        self.click(Locators.ADD)
        time.sleep(2)
        # Assertion function
        try:
            self.assertTrue(Locators.ADD)
        except AssertionError:
            print("ADD Button is not present")
        # Logging function
        logging.info("ADD Button is working")
        time.sleep(2)
        self.click(Locators.DATE)
        time.sleep(2)
        self.enter_text(Locators.DATE, "10-12-2020")
        time.sleep(2)
        self.click(Locators.SHIFT1)
        time.sleep(2)
        self.click(Locators.D1)
        time.sleep(2)
        self.click(Locators.SUBMIT)
        time.sleep(2)
        logging.info("The information is With Entering the data its submitted")
        self.click(Locators.ADD)
        time.sleep(2)
        self.click(Locators.DATE)
        time.sleep(2)
        self.enter_text(Locators.DATE, "10122000")
        time.sleep(2)
        self.click(Locators.SHIFT1)
        time.sleep(2)
        self.click(Locators.D1)
        time.sleep(2)
        self.click(Locators.CANCEL)
        logging.info("The information is With Entering the data its Canceled")
        time.sleep(2)
        self.click(Locators.ADD)
        time.sleep(2)
        try:
            self.click(Locators.SUBMIT)
            time.sleep(2)
        except:
            self.click(Locators.CANCEL)
            time.sleep(2)
        self.click(Locators.CANCEL)
        time.sleep(2)
        logging.info("The information is Without Entering the data its Canceled")
        # Edit some details in master page
        self.click(Locators.EDIT_BUTTON)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        logging.error("This Alert Message")
        self.click(Locators.ROW1)
        self.click(Locators.CELL1)
        time.sleep(2)
        self.click(Locators.EDIT_BUTTON)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        logging.error("This Alert Message")
        self.click(Locators.ROW1)
        time.sleep(2)
        self.click(Locators.EDIT_BUTTON)
        time.sleep(2)
        # Assertion function
        try:
            self.assertTrue(Locators.EDIT_BUTTON)
        except AssertionError:
            print("Edit Button is not present")
        # Logging function
        logging.info("Edit Button is working")
        self.click(Locators.DATE)
        time.sleep(2)
        self.enter_text(Locators.DATE, "14052022")
        time.sleep(2)
        self.click(Locators.SUBMIT)
        time.sleep(2)
        logging.info("The information is With Entering the data its submitted")
        self.click(Locators.EDIT)
        time.sleep(2)
        self.click(Locators.CANCEL)
        time.sleep(2)
        logging.info("The information is With Entering the data its Canceled")
        # Delete function
        self.click(Locators.DELETE)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        logging.error("This Alert Message")
        self.click(Locators.ROW1)
        time.sleep(2)
        self.click(Locators.DELETE)
        time.sleep(2)
        # Assertion function
        try:
            self.assertTrue(Locators.DELETE)
        except AssertionError:
            print("Delete Button is not present")
        logging.info("Delete Button is working")
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        # Download function
        self.click(Locators.DOWNLOAD)
        time.sleep(2)
        # Assertion function
        try:
            self.assertTrue(Locators.DOWNLOAD)
        except AssertionError:
            print("Download Button is not present")
        logging.info("Download Button is working")
        # Routing function
        self.click(Locators.ARROW)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        self.click(Locators.CELL1)
        time.sleep(2)
        self.click(Locators.ROW1)
        time.sleep(2)
        logging.warning("Routing Button is clicked")
        self.click(Locators.ARROW)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        self.click(Locators.ROW1)
        time.sleep(2)
        logging.warning("Routing Button is clicked")
        self.click(Locators.ARROW)
        time.sleep(2)
        # Assertion function
        try:
            self.assertTrue(Locators.ARROW)
        except AssertionError:
            print("Routing Button  is not present")
        logging.info("Routing Button is working")

        # Add details in detail page
        self.click(Locators.ALLR)
        time.sleep(2)
        self.click(Locators.ALLR)
        time.sleep(2)
        logging.info("Add Button is clicked")
        self.click(Locators.ADD)
        time.sleep(2)
        self.click(Locators.ID_CARD_NO)
        time.sleep(2)
        self.send_keys(Locators.ID_CARD_NO, Keys.ARROW_DOWN)
        time.sleep(2)
        self.send_keys(Locators.ID_CARD_NO, Keys.ARROW_DOWN)
        time.sleep(2)
        self.send_keys(Locators.ID_CARD_NO, Keys.ENTER)
        time.sleep(2)
        # Assert function
        try:
            self.assertNotEqual("13456", "13456")
        except AssertionError:
            print("ID are same")

        print("Assertion passed")
        self.click(Locators.DATE_1)
        time.sleep(2)
        self.enter_text(Locators.DATE_1, "01122001")
        time.sleep(2)
        # Assertion function
        try:
            self.assertNotEqual("01122001", "01122001")
        except AssertionError:
            print("Attendance time is same")
        self.click(Locators.ATTENDANCE_TIME)
        time.sleep(2)

        # Assertion function
        try:
            self.assertTrue(Locators.ATTENDANCE_TIME)
        except AssertionError:
            print("TIME IS not  PRESENT")
        self.enter_text(Locators.ATTENDANCE_TIME, "10")
        time.sleep(2)
        self.click(Locators.ATTENDANCE_OUTDATE)
        time.sleep(2)
        self.enter_text(Locators.ATTENDANCE_OUTDATE, "01122001")
        time.sleep(2)
        self.click(Locators.ATTENDANCE_OUTTIME)
        time.sleep(2)

        self.enter_text(Locators.ATTENDANCE_OUTTIME, "6")
        time.sleep(2)
        self.assertIs("6", "6", "comparison same")
        self.click(Locators.TOTAL_HOURS)
        time.sleep(2)
        self.enter_text(Locators.TOTAL_HOURS, "16")
        time.sleep(2)
        # Assertion function
        try:
            self.assertIsNot("16", "16")
        except AssertionError:
            print("same")
        self.click(Locators.NOTE)
        time.sleep(2)
        self.enter_text(Locators.NOTE, "jgvj")
        time.sleep(2)
        # self.assertIsNotNone(driver)
        logging.info("Submit Button is clicked")
        self.click(Locators.SUBMIT)
        time.sleep(2)
        logging.info("The information is With Entering the data its submitted")
        # Adding data in detail page
        logging.info("Add Button is clicked")
        self.click(Locators.ADD)
        time.sleep(2)
        self.click(Locators.ID_CARD_NO)
        time.sleep(2)
        self.send_keys(Locators.ID_CARD_NO, Keys.ARROW_DOWN)
        time.sleep(2)
        self.send_keys(Locators.ID_CARD_NO, Keys.ENTER)
        time.sleep(2)
        self.click(Locators.DATE_1)
        time.sleep(2)
        self.enter_text(Locators.DATE_1, "01122001")
        time.sleep(2)
        self.click(Locators.ATTENDANCE_TIME)
        time.sleep(2)
        self.enter_text(Locators.ATTENDANCE_TIME, "10")
        time.sleep(2)
        self.click(Locators.ATTENDANCE_OUTDATE)
        time.sleep(2)
        self.enter_text(Locators.ATTENDANCE_OUTDATE, "01122001")
        time.sleep(2)
        self.click(Locators.ATTENDANCE_OUTTIME)
        time.sleep(2)
        self.enter_text(Locators.ATTENDANCE_OUTTIME, "6")
        time.sleep(2)
        self.click(Locators.TOTAL_HOURS)
        time.sleep(2)
        self.enter_text(Locators.TOTAL_HOURS, "16")
        time.sleep(2)
        self.click(Locators.NOTE)
        time.sleep(2)
        self.enter_text(Locators.NOTE, "EMPLOYEE DETAIL")
        time.sleep(2)
        logging.info("Cancel Button is clicked")
        self.click(Locators.CANCEL)
        logging.info("The information is With Entering the data its Canceled")
        time.sleep(2)
        logging.info("Add Button is clicked")
        self.click(Locators.ADD)
        time.sleep(2)
        logging.info("Cancel Button is clicked")
        self.click(Locators.SUBMIT)
        time.sleep(2)
        self.click(Locators.CANCEL)
        logging.info("The information is Without Entering the data its Canceled")
        time.sleep(2)
        # Edit details in detail page
        logging.info("Edit Button is clicked")
        self.click(Locators.EDIT)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        logging.error("This Alert Message")
        self.click(Locators.CELL1)
        time.sleep(2)
        self.click(Locators.ROW1)
        time.sleep(2)
        logging.info("Edit Button is clicked")
        self.click(Locators.EDIT)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        logging.error("This Alert Message")
        self.click(Locators.ROW1)
        time.sleep(2)
        logging.info("Edit Button is clicked")
        self.click(Locators.EDIT)
        time.sleep(2)
        # Assertion function
        try:
            self.assertTrue(Locators.EDIT)
        except AssertionError:
            print("Edit Button is present")
        # Logging function
        logging.info("Edit Button is working")
        self.click(Locators.ATTENDANCE_TIME)
        time.sleep(2)
        self.send_keys(Locators.ATTENDANCE_TIME, Keys.CONTROL + "a")
        time.sleep(2)
        self.send_keys(Locators.ATTENDANCE_TIME, Keys.DELETE)

        self.enter_text(Locators.ATTENDANCE_TIME, "7")
        time.sleep(2)
        logging.info("Submit Button is clicked")
        self.click(Locators.SUBMIT)
        logging.info("The information is With Entering the data its submitted")
        time.sleep(2)

        # Cell edit in row

        self.click(Locators.ROW)
        time.sleep(2)
        self.click(Locators.CELL2)
        time.sleep(2)
        self.enter_text(Locators.CELL2, "15")
        time.sleep(2)
        self.send_keys(Locators.CELL2, Keys.ENTER)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        self.click(Locators.SAVE_BUTTON1)
        time.sleep(2)
        # Delete function
        logging.warning("Delete Button is clicked")
        self.click(Locators.DELETE)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        logging.error("This Alert Message")
        time.sleep(2)
        self.click(Locators.CELL2)
        time.sleep(2)
        logging.warning("Delete Button is clicked")
        self.click(Locators.DELETE)
        time.sleep(2)
        # Assertion function
        try:
            self.assertTrue(Locators.DELETE_BUTTON)
        except AssertionError:
            print("Delete Button is present")
        logging.info("Delete Button is working")
        self.driver.switch_to.alert.dismiss()
        time.sleep(2)
        # Download Function
        logging.info("Download Button is clicked")
        self.click(Locators.DOWNLOAD)
        time.sleep(2)
        # Assertion function
        try:
            self.assertTrue(Locators.DOWNLOAD)
        except AssertionError:
            print("Download Button is present")
        logging.info("Download Button is working")
        # Back to Master Page
        self.click(Locators.BACK)
        time.sleep(5)
        self.click(Locators.LOGOUT_LINK)
        time.sleep(5)
