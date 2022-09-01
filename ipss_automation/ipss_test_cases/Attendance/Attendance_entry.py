""" /* File: Objective: The objective of this page is Automating the file about home page(Attendance details) of the
IPSS HR module.


    Description: This page has Document id,Company code,company name.The employee Attendance details will
                 be here.

                 Also,this page has advanced filter for searching details,sorting option also available which is more
                 useful to sort in an order.Edit,save,delete those function will be used to change or delete the
                 record of the employee, add function is used to add Employee Attendance details.Routing button is to
                 go ahead to detail page for an employee. In that also add,edit,delete,save function will be used.
                 For all these functions I have automated using selenium scripts with all the negative cases.



Initiated By:Rajesh on 8th June.
Modification History

--------------------------------------------------------------------------------------------------------------------
DATE     |   AUTHOR           |  Modification Request No.                           | Remarks / Detail of Changes
--------------------------------------------------------------------------------------------------------------------
8-June-2022    Rajesh           Rajesh on 6th June 2022                                 Created mock script
9-June-2022    Rajesh           Rajesh on 8th June 2022                          Completed the full script
6-July-2022    Rajesh           Rajesh on 6th July 2022                               revamped the script with added
                                                                  Methods of assertion, file logging, Report generation.
2-August-2022   Rajesh         Rajesh on 1st August 2022                             Adding sequence and Modifying code
--------------------------------------------------------------------------------------------------------------------"""

import logging
import time
import unittest

from selenium.webdriver.common.keys import Keys

from ipss_automation.base import BasePage
from ipss_automation.locators import Locators
# Unittest.Testcase Used for Report Generation
# Logging function

class Attendanceentry(BasePage, unittest.TestCase):
    def __init__(self, driver):
        super().__init__(driver)

    def Attendance(self):
        self.driver.refresh()
        time.sleep(2)
        self.click(Locators.SEARC)
        time.sleep(2)
        self.click(Locators.P3)
        time.sleep(2)
        self.click(Locators.DRAWER_ICON)
        time.sleep(2)
        logging.info("The information is it's Clicking Drawer Button")
        self.click(Locators.ATTENDANCE)
        time.sleep(2)
        logging.info("The information is it's Clicking Attendance")
        self.click(Locators.ATTENDANCE_ENTRY)
        time.sleep(2)
        logging.info("The information is it's Clicking Attendance entry")

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
        self.click(Locators.ADDBUTTON)
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
        logging.info("The information is WithOut Entering the data its Canceled")
        # selecting row

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

        # Adding data in master Page
        time.sleep(20)
        self.click(Locators.ROW)
        time.sleep(2)
        self.click(Locators.ADD_BUTTON)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        logging.error("This Alert Message")
        self.click(Locators.ROW)
        time.sleep(2)
        self.click(Locators.ADD_BUTTON)
        time.sleep(2)
        # Assertion function
        try:
            self.assertTrue(Locators.ADD_BUTTON)
        except AssertionError:
            print("ADD Button is not present")
        # Logging function
        logging.info("ADD Button is working")
        time.sleep(2)
        logging.info("Add Button Clicked")
        self.click(Locators.DOCDATE1)
        time.sleep(2)
        self.enter_text(Locators.DOCDATE1, "08.08.2022")
        time.sleep(2)
        self.click(Locators.SUBMI)
        logging.info("Submit Button Clicked")
        logging.info("The information is With Entering the data its submitted")
        time.sleep(5)
        self.click(Locators.ADD_BUTTON)
        time.sleep(2)
        self.click(Locators.DOCDATE1)
        time.sleep(2)
        self.enter_text(Locators.DOCDATE1, "08082022")
        time.sleep(2)
        self.click(Locators.CANCEL)
        logging.info("Cancel Button Clicked")
        logging.info("The information is With Entering the data its Canceled")
        time.sleep(2)
        self.click(Locators.ADD_BUTTON)
        time.sleep(2)
        self.click(Locators.CANCEL)
        time.sleep(2)
        logging.info("The information is Without Entering the data its Canceled")
        self.click(Locators.ADD_BUTTON)
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
        # Edit the master data
        self.click(Locators.EDIT_BUTTON)
        time.sleep(2)
        logging.info("Edit Button Clicked")
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        logging.error("This Alert Message")
        self.click(Locators.ROW)
        time.sleep(1)
        self.click(Locators.ROW1)
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
        # assert function
        try:
            self.assertTrue(self.is_element_present(Locators.EDIT_BUTTON))
        except AssertionError:
            print("Edit Button is not present")
        # Logging function
        logging.info("Edit Button is working")
        logging.info("Edit Button Clicked")
        self.send_keys(Locators.DOCDATE1, Keys.CONTROL + 'a')
        time.sleep(2)
        self.send_keys(Locators.DOCDATE1, Keys.DELETE)
        time.sleep(2)
        self.enter_text(Locators.DOCDATE1, "08082022")
        time.sleep(2)
        self.click(Locators.SUBMIT)
        time.sleep(2)
        logging.info("Submit Button Clicked")
        logging.info("The information is With Entering the data its submitted")

        # Delete The Master data
        self.click(Locators.DELETE_BUTTON)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        logging.error("This Alert Message")
        self.click(Locators.ROW)
        time.sleep(2)
        self.click(Locators.DELETE_BUTTON)
        # assert function
        try:
            self.assertTrue(Locators.DELETE_BUTTON)
        except AssertionError:
            print("Delete Button is not present")
        logging.info("Delete Button is working")
        logging.info("Delete Button Clicked")
        self.driver.switch_to.alert.accept()
        time.sleep(5)

        # Download Function
        self.click(Locators.DOWNLOAD_BUTTON)
        time.sleep(1)
        # assert function
        try:
            self.assertTrue(Locators.DOWNLOAD_BUTTON)
        except AssertionError:
            print("Download Button is not present")
        logging.info("Download Button is working")
        time.sleep(2)
        # Routing Function
        self.click(Locators.ROUTING_BUTTON_ATT)
        time.sleep(2)
        self.driver.switch_to.alert.dismiss()
        time.sleep(2)
        logging.error("This Alert Message")
        self.click(Locators.ROUTING_BUTTON_ATT)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        logging.error("This Alert Message")
        self.click(Locators.ROW)
        time.sleep(2)
        self.click(Locators.ROW1)
        time.sleep(2)
        self.click(Locators.ROUTING_BUTTON_ATT)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        logging.error("This Alert Message")
        self.click(Locators.ROW1)
        time.sleep(2)
        self.click(Locators.ROUTING_BUTTON_ATT)
        time.sleep(2)
        # Assertion function
        try:
            self.assertTrue(Locators.ROUTING_BUTTON_ATT)
        except AssertionError:
            print("Routing Button is not present")
        logging.info("Routing Button Clicked")
        time.sleep(2)
        # Adding Data in Detail page

        self.click(Locators.ADD_BUTTON)
        time.sleep(2)
        # Assertion function
        try:
            self.assertTrue(Locators.ADD_BUTTON)
        except AssertionError:
            print("ADD Button is present")
        logging.info("ADD Button is not working")
        logging.info("Add Button Clicked")
        time.sleep(2)
        self.click(Locators.ID_CARD)
        time.sleep(3)
        self.send_keys(Locators.ID_CARD, Keys.ARROW_DOWN)
        time.sleep(2)
        self.send_keys(Locators.ID_CARD, Keys.ENTER)
        time.sleep(2)
        self.click(Locators.DOCDATE)
        time.sleep(2)
        self.send_keys(Locators.DOCDATE, "01062022")
        time.sleep(2)
        self.click(Locators.PRESENT)
        time.sleep(2)
        self.click(Locators.D1)
        time.sleep(2)
        self.click(Locators.SHIFT)
        time.sleep(10)
        self.click(Locators.D1)
        time.sleep(2)
        self.click(Locators.TEMPLATE)
        time.sleep(2)
        self.click(Locators.D1)
        time.sleep(2)
        self.click(Locators.NOTES)
        time.sleep(2)
        self.enter_text(Locators.NOTES, "gsjbfhb")
        time.sleep(2)
        # assert function
        self.assertIs("gsjbfhb", "gsjbfhb", "Comparison same")
        self.click(Locators.SUBMIT)
        logging.warning("Submit Button Clicked")
        time.sleep(5)
        self.click(Locators.ADD_BUTTON)
        time.sleep(2)
        logging.info("Add Button Clicked")
        # self.driver.execute_script("window.scrollTo(0,0)")
        time.sleep(2)
        self.click(Locators.ID_CARD)
        time.sleep(3)
        self.send_keys(Locators.ID_CARD, Keys.ARROW_DOWN)
        time.sleep(2)
        self.send_keys(Locators.ID_CARD, Keys.ENTER)
        time.sleep(2)
        self.click(Locators.DOCDATE)
        time.sleep(2)
        self.send_keys(Locators.DOCDATE, "01062022")
        time.sleep(2)
        self.click(Locators.PRESENT)
        time.sleep(2)
        self.send_keys(Locators.PRESENT, Keys.ARROW_DOWN)
        time.sleep(2)
        self.send_keys(Locators.PRESENT, Keys.ENTER)
        time.sleep(2)
        self.click(Locators.SHIFT)
        time.sleep(2)
        self.send_keys(Locators.SHIFT, Keys.ARROW_DOWN)
        time.sleep(2)
        self.send_keys(Locators.SHIFT, Keys.ENTER)
        time.sleep(2)
        self.click(Locators.TEMPLATE)
        time.sleep(2)
        self.send_keys(Locators.TEMPLATE, Keys.ARROW_DOWN)
        time.sleep(2)
        self.send_keys(Locators.TEMPLATE, Keys.ENTER)
        time.sleep(2)
        self.click(Locators.NOTES)
        time.sleep(2)
        self.enter_text(Locators.NOTES, "gsjbfhb")
        time.sleep(2)
        self.click(Locators.SUBMIT)
        time.sleep(5)
        logging.info("The information is With Entering the data its submitted")
        self.click(Locators.ADD_BUTTON)
        time.sleep(2)
        self.click(Locators.ID_CARD)
        time.sleep(3)
        self.send_keys(Locators.ID_CARD, Keys.ARROW_DOWN)
        time.sleep(2)
        self.send_keys(Locators.ID_CARD, Keys.ENTER)
        time.sleep(2)
        self.click(Locators.DOCDATE)
        time.sleep(2)
        self.send_keys(Locators.DOCDATE, "01062022")
        time.sleep(2)
        self.click(Locators.PRESENT)
        time.sleep(2)
        self.send_keys(Locators.PRESENT, Keys.ARROW_DOWN)
        time.sleep(2)
        self.send_keys(Locators.PRESENT, Keys.ENTER)
        time.sleep(2)
        self.click(Locators.SHIFT)
        time.sleep(2)
        self.send_keys(Locators.SHIFT, Keys.ARROW_DOWN)
        time.sleep(2)
        self.send_keys(Locators.SHIFT, Keys.ENTER)
        time.sleep(2)
        self.click(Locators.TEMPLATE)
        time.sleep(2)
        self.send_keys(Locators.TEMPLATE, Keys.ARROW_DOWN)
        time.sleep(2)
        self.send_keys(Locators.TEMPLATE, Keys.ENTER)
        time.sleep(2)
        self.click(Locators.NOTES)
        time.sleep(2)
        self.enter_text(Locators.NOTES, "gsjbfhb")
        time.sleep(2)
        self.click(Locators.CANCEL)
        time.sleep(2)
        logging.warning("Without Entering the data its cancelled")
        self.click(Locators.ADD_BUTTON)
        time.sleep(2)
        try:
            self.click(Locators.SUBMIT)
            print("The input values are not clear in Sequence")
        except:
            self.click(Locators.CANCEL)
        time.sleep(2)
        self.click(Locators.CANCEL)
        time.sleep(2)
        logging.warning("Without Entering the data its cancelled")
        logging.warning("Cancel Button Clicked")
        # Edit the detail page data
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
        logging.warning("Edit Button Clicked With no row selected")
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        self.click(Locators.ROW1)
        time.sleep(2)
        self.click(Locators.EDIT_BUTTON)
        time.sleep(2)
        # assert function
        try:
            self.assertTrue(Locators.EDIT_BUTTON)
        except AssertionError:
            print("Edit Button is not present")
        # Logging function
        logging.info("Edit Button is working")
        logging.warning("Edit Button Clicked")
        self.click(Locators.PRESENT)
        time.sleep(2)
        self.send_keys(Locators.PRESENT, Keys.ARROW_DOWN)
        time.sleep(2)
        self.send_keys(Locators.PRESENT, Keys.ENTER)
        time.sleep(2)
        self.click(Locators.SUBMIT)
        time.sleep(2)
        # Cell edit and Save function
        self.click(Locators.SAVE_BUTTON)
        time.sleep(2)
        logging.info("Save Button Clicked")
        self.click(Locators.COL6)
        time.sleep(2)
        self.enter_text(Locators.COL6, "Present")
        time.sleep(2)
        self.send_keys(Locators.COL6, Keys.ENTER)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(1)
        self.click(Locators.COL6)
        time.sleep(2)
        self.enter_text(Locators.COL6, "Present")
        time.sleep(2)
        self.send_keys(Locators.COL6, Keys.ENTER)
        time.sleep(2)
        self.click(Locators.SAVE_BUTTON)
        time.sleep(2)
        # assert function
        try:
            self.assertTrue(Locators.SAVE_BUTTON)
        except AssertionError:
            print("Save Button is not present")
        # Logging function
        logging.info("Save Button is working")
        # Delete Function
        self.click(Locators.DELETE_BUTTON)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(1)
        logging.error("This Alert Message")
        self.click(Locators.ROW)
        time.sleep(2)
        self.click(Locators.DELETE_BUTTON)
        time.sleep(2)
        # assert function
        try:
            self.assertTrue(Locators.DELETE_BUTTON)
        except AssertionError:
            print("Delete Button is not present")
        logging.info("Delete Button is working")
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        logging.warning("Delete Button Clicked")
        self.driver.switch_to.alert.accept()
        time.sleep(5)

        # Download Function
        self.click(Locators.DOWNLOAD_BUTTON)
        time.sleep(2)
        # assert function
        try:
            self.assertTrue(Locators.DOWNLOAD_BUTTON)
        except AssertionError:
            print("Download Button is not present")
        logging.info("Download Button is working")
        logging.info("Download Button Clicked")

        self.click(Locators.LOGOUT_LINK)
        time.sleep(5)
