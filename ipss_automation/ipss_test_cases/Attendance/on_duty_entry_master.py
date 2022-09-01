""" /* File: Objective: The objective of this page is Automating the file about home page(On_Duty_entry)
of the student module.

Description: This page has Document id,Company code,company name.On Duty Details of Employee Attendance details will
                 be here.

                 Also,this page has advanced filter for searching details,sorting option also available which is more
                 useful to sort in an order.Edit,save,delete those function will be used to change or delete the
                 record of the employee, add function is used to add On Duty Details of Employee Attendance
                 details.Routing button is to go ahead to detail page for an employee. In that also add,edit,delete,
                 save function will be used. For all these functions I have automated using selenium scripts with all
                 the negative cases.


Initiated By:Bavatharani on 6th June.
Modification History

--------------------------------------------------------------------------------------------------------------------
DATE     |   AUTHOR           |  Modification Request No.                           | Remarks / Detail of Changes
--------------------------------------------------------------------------------------------------------------------
9-June-2022    Bavatharani           Bavatharani on 6th June 2022                                 Created mock script
10-June-2022   Bavatharani           Bavatharani on 8th June 2022                          Completed the full script
6-July-2022    Bavatharani           Thangaraj on 6th July 2022                        revamped the script with added
                                                                 Methods of assertion, file logging, Report generation.
2-August-2022   Rajesh         Rajesh on 1st August 2022                         Adding sequence and Modifying code
--------------------------------------------------------------------------------------------------------------------"""
import logging
# Unittest.Testcase Used for Report Generation
# Logging function
import time
import unittest
from re import A

from selenium.webdriver.common.keys import Keys

# import softest
from ipss_automation.base import BasePage
from ipss_automation.locators import Locators


class Duty(BasePage, unittest.TestCase):

    def __init__(self, driver):
        super().__init__(driver)

    def dutymaster(self):
        self.driver.refresh()
        time.sleep(2)
        self.click(Locators.SEARC)
        time.sleep(2)
        self.click(Locators.P6)
        time.sleep(2)
        self.click(Locators.T_DRAWER)
        time.sleep(3)
        self.click(Locators.ATTENDANCE_T)
        time.sleep(3)
        self.click(Locators.ON_DUTY)
        time.sleep(3)
        # Generate the sequence
        self.click(Locators.SEQUENCE)
        time.sleep(2)
        # Assert function
        try:
            self.assertTrue(Locators.SEQUENCE)
        except AssertionError:
            print("SEQUENCE Button  is present")
        logging.info("Sequence Button is working")
        # Adding sequence

        self.click(Locators.ADDBUTTON)
        time.sleep(2)
        logging.info("ADD Button is working")
        # Assert function
        try:
            self.assertTrue(Locators.ADDBUTTON)
        except AssertionError:
            print("ADD Button is present")
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
        self.click(Locators.ADDBUTTON)
        time.sleep(2)
        self.click(Locators.SUBMIT)
        time.sleep(2)
        # self.click(Locators.CANCEL)
        time.sleep(2)
        logging.info("The information is WithOut Entering the data its Canceled")
        # selecting row
        # self.click(Locators.SROW)
        # time.sleep(2)
        # editing the sequence for generate another sequence

        self.click(Locators.SROW)
        time.sleep(2)
        self.click(Locators.EDITBUTTON)
        time.sleep(2)
        # Assertion function
        try:
            self.assertTrue(Locators.EDITBUTTON)
        except AssertionError:
            print("Edit Button is present")
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
        # Assertion function
        try:
            self.assertTrue(Locators.CANCE)
        except AssertionError:
            print("Close Button is present")
        logging.info("Close Button is working")
        time.sleep(10)
        # Adding data in master page
        self.click(Locators.ROW)
        time.sleep(2)
        self.click(Locators.T_ADD)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        logging.error("This Alert Message")
        self.click(Locators.ROW)
        time.sleep(2)
        logging.info("Add Button Clicked")
        self.click(Locators.T_ADD)
        time.sleep(2)
        # Assertion function
        try:
            self.assertTrue(Locators.T_ADD)
        except AssertionError:
            print("ADD Button is present")

        # Logging function
        logging.info("ADD Button is working")
        time.sleep(2)
        self.click(Locators.E_DOC_DATE)
        time.sleep(2)
        self.enter_text(Locators.E_DOC_DATE, "08-05-2001")
        time.sleep(2)
        logging.info("Submit Button Clicked")
        self.click(Locators.T_SUBMIT)
        time.sleep(2)
        logging.info("The information is With Entering the data its submitted")
        logging.info("Add Button Clicked")
        self.click(Locators.T_ADD)
        time.sleep(2)
        self.click(Locators.E_DOC_DATE)
        time.sleep(2)
        self.enter_text(Locators.E_DOC_DATE, "08-05-2001")
        time.sleep(2)
        logging.warning("Cancel Button Clicked")
        self.click(Locators.T_CANCEL)
        logging.info("The information is With Entering the data its Canceled")
        time.sleep(2)
        self.click(Locators.T_ADD)
        time.sleep(2)
        self.click(Locators.T_SUBMIT)
        time.sleep(2)
        self.click(Locators.T_CANCEL)
        logging.info("The information is Without Entering the data its Canceled")
        time.sleep(2)
        # Edit Data in master page
        logging.info("Edit Button Clicked")
        self.click(Locators.T_EDIT_BUTTON)
        time.sleep(3)
        self.driver.switch_to.alert.accept()
        time.sleep(1)
        self.click(Locators.ROW)
        time.sleep(2)
        self.click(Locators.ROW1)
        time.sleep(2)
        self.click(Locators.T_EDIT_BUTTON)
        time.sleep(2)
        logging.info("Edit Button Clicked")
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        logging.error("This Alert Message")
        self.click(Locators.ROW1)
        time.sleep(2)
        self.click(Locators.T_EDIT_BUTTON)
        time.sleep(3)
        # Assertion function
        try:
            self.assertTrue(Locators.T_EDIT_BUTTON)
        except AssertionError:
            print("Edit Button is present")
        # Logging function
        logging.info("Edit Button is working")
        self.click(Locators.E_DOC_DATE)
        time.sleep(2)
        self.send_keys(Locators.E_DOC_DATE, Keys.CONTROL + 'a')
        time.sleep(2)
        self.send_keys(Locators.E_DOC_DATE, Keys.DELETE)
        time.sleep(2)
        self.enter_text(Locators.E_DOC_DATE, "08-05-2001")
        time.sleep(2)
        logging.info("Submit Button Clicked")
        self.click(Locators.T_SUBMIT)
        logging.info("The information is With Entering the data its submitted")
        time.sleep(2)

        # Delete Function
        logging.info("Delete Button Clicked")
        self.click(Locators.T_DELETE_BUTTON)
        time.sleep(3)
        self.driver.switch_to.alert.accept()
        time.sleep(1)
        logging.error("This Alert Message")
        self.click(Locators.T_SELECT_BOX)
        time.sleep(2)
        logging.info("Delete Button Clicked")
        self.click(Locators.T_DELETE_BUTTON)
        time.sleep(3)
        # Assertion function
        try:
            self.assertTrue(Locators.T_DELETE_BUTTON)
        except AssertionError:
            print("Delete Button is present")
        logging.info("Delete Button is working")
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        # Download function
        logging.info("Download Button Clicked")
        self.click(Locators.T_DOWNLOAD)
        try:
            self.assertTrue(Locators.DOWNLOAD_BUTTON)
        except AssertionError:
            print("Download Button is present")
        logging.info("Download Button is working")
        time.sleep(3)
        # Routing Function
        logging.warning("Routing Button is clicked")
        self.click(Locators.DETAIL)
        time.sleep(3)
        self.driver.switch_to.alert.accept()
        time.sleep(1)
        logging.error("This Alert Message")
        self.click(Locators.T_SELECT_BOX3)
        time.sleep(3)
        self.click(Locators.T_SELECT_BOX1)
        time.sleep(2)
        self.click(Locators.DETAIL)
        time.sleep(3)
        self.driver.switch_to.alert.accept()
        time.sleep(1)
        logging.error("This Alert Message")
        self.click(Locators.T_SELECT_BOX3)
        time.sleep(3)
        self.click(Locators.DETAIL)
        time.sleep(3)
        # Assertion function
        try:
            self.assertTrue(Locators.DETAIL)
        except AssertionError:
            print("Routing Button  is not present")
        logging.info("Routing Button is work")
        # self.driver.switch_to.alert.accept()
        time.sleep(1)
        # Adding Data in Detail page
        logging.info("Add Button Clicked")
        self.click(Locators.T_ADD)
        time.sleep(2)
        # self.click(Locators.ID)
        # time.sleep(3)
        # self.click(Locators.ID)
        # time.sleep(3)
        self.enter_text(Locators.ID, "3101197")
        time.sleep(3)
        self.send_keys(Locators.ID, Keys.ARROW_DOWN)
        time.sleep(3)
        self.send_keys(Locators.ID, Keys.ENTER)
        time.sleep(3)
        self.click(Locators.EMPN)
        time.sleep(2)
        # self.enter_text(Locators.EMPN, "Bava")
        time.sleep(3)
        self.click(Locators.P_CAT)
        time.sleep(4)
        self.enter_text(Locators.P_CAT, "MSTAFF")
        time.sleep(3)
        self.send_keys(Locators.P_CAT, Keys.ARROW_DOWN)
        time.sleep(3)
        self.send_keys(Locators.P_CAT, Keys.ENTER)
        time.sleep(3)
        self.click(Locators.E_DO_DATE)
        time.sleep(2)
        self.enter_text(Locators.E_DO_DATE, "08-05-2001")
        time.sleep(2)
        # self.click(Locators.OD)
        # time.sleep(2)
        # self.enter_text(Locators.OD, "wednesday")
        # time.sleep(2)
        self.click(Locators.OHD)
        time.sleep(2)
        self.enter_text(Locators.OHD, "No")
        time.sleep(2)
        self.click(Locators.HRS)
        time.sleep(2)
        self.enter_text(Locators.HRS, "4")
        time.sleep(2)
        logging.info("Submit Button Clicked")
        self.click(Locators.T_SUBMIT)
        time.sleep(2)
        logging.info("Add Button Clicked")
        self.click(Locators.T_ADD)
        time.sleep(2)
        self.click(Locators.ID)
        time.sleep(2)
        # self.enter_text(Locators.ID, "3101197")
        time.sleep(3)
        self.send_keys(Locators.ID, Keys.ARROW_DOWN)
        time.sleep(3)
        self.send_keys(Locators.ID, Keys.ENTER)
        time.sleep(3)
        # self.click(Locators.EMPN)
        # time.sleep(2)
        # self.enter_text(Locators.EMPN, "Bava")
        # time.sleep(3)
        # Assertion function
        try:
            self.assertFalse(Locators.EMPN)
        except AssertionError:
            print("Employee name is Present")

        self.click(Locators.P_CAT)
        time.sleep(4)
        self.enter_text(Locators.P_CAT, "MSTAFF")
        time.sleep(3)
        self.send_keys(Locators.P_CAT, Keys.ARROW_DOWN)
        time.sleep(3)
        self.send_keys(Locators.P_CAT, Keys.ENTER)
        time.sleep(3)
        self.click(Locators.E_DO_DATE)
        time.sleep(2)
        self.enter_text(Locators.E_DO_DATE, "08-05-2001")
        time.sleep(2)
        # self.click(Locators.OD)
        # time.sleep(2)
        # self.enter_text(Locators.OD, "wednesday")
        # time.sleep(2)
        # Assertion function

        self.click(Locators.OHD)
        time.sleep(2)
        self.enter_text(Locators.OHD, "No")
        time.sleep(2)
        self.assertIs("No", "No", "Comparison same")
        self.click(Locators.HRS)
        time.sleep(2)
        self.enter_text(Locators.HRS, "4")
        time.sleep(2)
        logging.info("Cancel Button Clicked")
        self.click(Locators.T_CANCEL)
        time.sleep(2)
        self.click(Locators.T_ADD)
        time.sleep(2)
        self.click(Locators.T_SUBMIT)
        time.sleep(2)
        self.click(Locators.T_CANCEL)
        time.sleep(2)

        # Edit the data in detail page
        logging.info("Edit Button Clicked")
        self.click(Locators.T_EDIT_BUTTON)
        time.sleep(3)
        self.driver.switch_to.alert.accept()
        time.sleep(1)
        logging.error("This Alert Message")
        self.click(Locators.ROW)
        time.sleep(2)
        logging.info("Edit Button Clicked")
        self.click(Locators.T_EDIT_BUTTON)
        time.sleep(3)
        # self.driver.switch_to.alert.accept()
        # time.sleep(2)
        # self.click(Locators.ROW1)
        # time.sleep(2)
        # logging.info("Edit Button Clicked")
        # self.click(Locators.T_EDIT_BUTTON)
        # time.sleep(3)
        self.click(Locators.HRS)
        time.sleep(2)
        self.send_keys(Locators.HRS, Keys.CONTROL+"a")
        time.sleep(2)
        self.send_keys(Locators.HRS, Keys.DELETE)
        time.sleep(2)
        self.enter_text(Locators.HRS, "4")
        time.sleep(2)
        self.send_keys(Locators.HRS, Keys.ENTER)
        time.sleep(3)
        logging.info("Submit Button Clicked")
        self.click(Locators.SUBMI)
        time.sleep(3)
        # Save function
        self.click(Locators.T_SELECT_BOX1)
        time.sleep(3)
        self.click(Locators.OD)
        time.sleep(3)
        self.send_keys(Locators.OD, Keys.CONTROL + "a")
        time.sleep(2)
        self.send_keys(Locators.OD, Keys.DELETE)
        time.sleep(2)
        self.enter_text(Locators.OD, "Tuesday")
        time.sleep(3)
        self.send_keys(Locators.OD, Keys.ENTER)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(1)
        self.click(Locators.SAVE_BUTTON1)
        time.sleep(2)
        # Delete function
        self.click(Locators.T_SELECT_BOX)
        time.sleep(2)
        self.click(Locators.T_SELECT_BOX1)
        time.sleep(2)
        logging.info("Delete Button Clicked")
        self.click(Locators.T_DELETE_BUTTON)
        time.sleep(3)
        self.driver.switch_to.alert.accept()
        time.sleep(1)
        logging.error("This Alert Message")
        self.click(Locators.T_SELECT_BOX)
        time.sleep(2)
        self.click(Locators.T_DELETE_BUTTON)
        time.sleep(3)
        # Assertion Function
        try:
            self.assertTrue(Locators.T_DELETE_BUTTON)
        except AssertionError:
            print("Delete Button is not present")
        logging.info("Delete Button is working")
        self.driver.switch_to.alert.accept()
        time.sleep(1)
        # Download Function
        logging.info("Download Button Clicked")
        self.click(Locators.T_DOWNLOAD)
        # Assertion function
        try:
            self.assertTrue(Locators.T_DOWNLOAD)
        except AssertionError:
            print("Download Button is not present")
        logging.info("Download Button is working")
        time.sleep(3)

        self.click(Locators.LOGOUT_LINK)
        time.sleep(5)
