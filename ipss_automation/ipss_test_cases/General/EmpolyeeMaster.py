""" /* File:
    Objective: The objective of this page is Automating the file about home page(EMployee Master) of the General Module.

Description: This page has Add, Read, Edit, Delete and Download the employee information
Information Captured - Personal details, Employment, Contact info, Identity, ESI/PF, Bank details,
Education Details, Family details, Previous employment details, Training details, Leave Policy

                 Also,this page has advanced filter for searching details,sorting option also available which is more
                 useful to sort in an order.Edit,save,delete those function will be used to change or delete the
                 record of the employee, add function is used to add Employee Manual OT details.Routing button is to
                 go ahead to detail page for an employee. In that also add,edit,delete,save function will be used.
                 For all these functions I have automated using selenium scripts with all the negative cases.


Initiated By:Rajesh on July 26.
Modification History

--------------------------------------------------------------------------------------------------------------------
DATE     |   AUTHOR           |  Modification Request No.                           | Remarks / Detail of Changes
--------------------------------------------------------------------------------------------------------------------
26-July-2022    Rajesh           Rajesh on 26th July 2022                                 Created mock script
30-July-2022   Rajesh           Rajesh on 30th July 2022                          Completed the full script
30-July-2022    Rajesh           Rajesh on 30th July 2022                               revamped the script with added
                                                                  Methods of assertion, file logging, Report generation.

--------------------------------------------------------------------------------------------------------------------"""
import time
from unittest import TestCase
from selenium.webdriver.common.keys import Keys
import unittest
import HtmlTestRunner
from selenium import webdriver

from ipss_automation.base import BasePage
import selenium.webdriver.common.keys
from ipss_automation.locators import Locators


class Empolyee(BasePage, unittest.TestCase):
    def __init__(self, driver):
        super().__init__(driver)

    def empolyee(self):
        self.click(Locators.SEARC)
        time.sleep(2)
        self.click(Locators.P1)
        time.sleep(2)
        self.click(Locators.DRAWER_ICON)
        time.sleep(2)
        self.click(Locators.GENERAL)
        time.sleep(2)
        self.click(Locators.EMPOLYE)
        time.sleep(2)
        self.click(Locators.ROW)
        time.sleep(2)
        self.click(Locators.ADD_BUTTON)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        self.click(Locators.ROW)
        time.sleep(2)
        # command
        self.click(Locators.ADD_BUTTON)
        time.sleep(2)
        self.click(Locators.SUBMI)
        # personal details
        self.click(Locators.R_TYPE)
        time.sleep(2)
        self.click(Locators.D1)
        time.sleep(2)
        self.click(Locators.R_FIRST)
        time.sleep(2)
        self.enter_text(Locators.R_FIRST, "123*4")
        time.sleep(2)
        self.send_keys(Locators.R_FIRST,Keys.CONTROL+'a')
        time.sleep(2)
        self.enter_text(Locators.R_FIRST, "Rajesh")
        time.sleep(2)
        self.enter_text(Locators.R_MID, "1234#")
        time.sleep(2)
        self.send_keys(Locators.R_MID, Keys.CONTROL + 'a')
        time.sleep(2)
        self.enter_text(Locators.R_MID, "Kannan")
        time.sleep(2)
        self.enter_text(Locators.R_LAST, "1234#")
        time.sleep(2)
        self.send_keys(Locators.R_LAST, Keys.CONTROL + 'a')
        time.sleep(2)
        self.enter_text(Locators.R_LAST, "A")
        time.sleep(2)
        self.enter_text(Locators.R_AADHAR, "1234@")
        time.sleep(2)
        self.send_keys(Locators.R_AADHAR, Keys.CONTROL + 'a')
        time.sleep(2)
        self.enter_text(Locators.R_AADHAR, "Rajesh Kannan A")
        time.sleep(2)
        self.enter_text(Locators.R_DOB, "25122001")
        time.sleep(2)
        self.click(Locators.R_GEN)
        time.sleep(2)
        self.click(Locators.D1)
        time.sleep(2)
        self.click(Locators.R_BLOOD)
        time.sleep(2)
        self.click(Locators.D4)
        time.sleep(2)
        self.click(Locators.R_NATION)
        time.sleep(2)
        self.click(Locators.D1)
        time.sleep(2)
        self.click(Locators.R_RELI)
        time.sleep(2)
        self.click(Locators.D1)
        time.sleep(2)
        self.enter_text(Locators.R_FATH, "123&")
        time.sleep(2)
        self.send_keys(Locators.R_FATH, Keys.CONTROL + 'a')
        time.sleep(2)
        self.enter_text(Locators.R_FATH, "APPA")
        time.sleep(2)
        self.enter_text(Locators.R_MOM, "1234#")
        time.sleep(2)
        self.send_keys(Locators.R_MOM, Keys.CONTROL + 'a')
        time.sleep(2)
        self.enter_text(Locators.R_MOM, "AMMA")
        time.sleep(2)
        self.click(Locators.R_MAR)
        time.sleep(2)
        self.click(Locators.D2)
        time.sleep(2)
        self.enter_text(Locators.R_SAPOUE, "1234%")
        time.sleep(2)
        self.send_keys(Locators.R_SAPOUE, Keys.CONTROL + 'a')
        time.sleep(2)
        self.enter_text(Locators.R_SAPOUE, "RaJesh")
        time.sleep(2)
        self.enter_text(Locators.R_DOM, "11112011")
        time.sleep(2)
        self.enter_text(Locators.R_IDEN, "1234*")
        time.sleep(2)
        self.send_keys(Locators.R_IDEN, Keys.CONTROL + 'a')
        time.sleep(2)
        self.enter_text(Locators.R_IDEN, "Mole")
        time.sleep(2)
        self.click(Locators.R_DIS)
        time.sleep(2)
        self.click(Locators.D1)
        time.sleep(2)
        self.enter_text(Locators.R_HE, "ASDFGHJK")
        time.sleep(2)
        self.send_keys(Locators.R_HE, Keys.CONTROL + 'a')
        time.sleep(2)
        self.enter_text(Locators.R_HE, "5")
        time.sleep(2)
        self.enter_text(Locators.R_WE, "SDFGHJ")
        time.sleep(2)
        self.send_keys(Locators.R_WE, Keys.CONTROL + 'a')
        time.sleep(2)
        self.enter_text(Locators.R_WE, "52")
        time.sleep(2)
        self.click(Locators.R_EX)
        time.sleep(2)
        self.click(Locators.D1)
        time.sleep(2)
        self.click(Locators.R_18)
        time.sleep(1)
        self.file_upload(Locators.IMG, "C:/Users/rajes/OneDrive/Pictures/hacker1.jpg")
        time.sleep(2)
        self.click(Locators.P_SUBMIT_BUTTON)
        time.sleep(5)
        # Empolyment
        self.click(Locators.T1)
        time.sleep(2)
        self.click(Locators.P_SUBMIT_BUTTON)
        time.sleep(2)
        self.enter_text(Locators.R_DOJ, "02062021")
        time.sleep(2)
        self.enter_text(Locators.R_ADOJ, "09062021")
        time.sleep(2)
        self.enter_text(Locators.R_LWD, "25122021")
        time.sleep(2)
        self.click(Locators.R_DEPDROP)
        time.sleep(2)
        self.click(Locators.D17)
        time.sleep(2)
        self.enter_text(Locators.R_DEPT, "Staff")
        time.sleep(2)
        self.enter_text(Locators.R_COSTCEN, "d")
        time.sleep(2)
        self.click(Locators.R_BAND)
        time.sleep(2)
        self.click(Locators.D1)
        time.sleep(2)
        self.click(Locators.R_PAY)
        time.sleep(2)
        self.click(Locators.D1)
        time.sleep(2)
        self.click(Locators.R_PAYTY)
        time.sleep(2)
        self.click(Locators.D1)
        time.sleep(2)
        self.click(Locators.R_DES)
        time.sleep(2)
        self.click(Locators.D1)
        time.sleep(2)
        self.enter_text(Locators.DESGCON, 'f')
        time.sleep(2)
        self.click(Locators.R_ACTIVE)
        time.sleep(2)
        self.click(Locators.D2)
        time.sleep(2)
        self.click(Locators.R_PF)
        time.sleep(2)
        self.click(Locators.D2)
        time.sleep(2)
        self.click(Locators.R_ESI)
        time.sleep(2)
        self.click(Locators.D1)
        time.sleep(2)
        self.click(Locators.R_CONTRAC)
        time.sleep(2)
        self.click(Locators.D2)
        time.sleep(2)
        self.click(Locators.R_SALARY)
        time.sleep(2)
        self.click(Locators.D1)
        time.sleep(2)
        self.click(Locators.R_SALA_TY)
        time.sleep(2)
        self.click(Locators.D1)
        time.sleep(2)
        self.click(Locators.R_MON)
        time.sleep(2)
        self.click(Locators.D2)
        time.sleep(2)
        self.enter_text(Locators.R_OLD, "85")
        time.sleep(2)
        self.click(Locators.R_TEMP)
        time.sleep(2)
        self.click(Locators.D2)
        time.sleep(2)
        self.click(Locators.R_HOS)
        time.sleep(2)
        self.click(Locators.D2)
        time.sleep(2)
        self.click(Locators.R_VEHICLE)
        time.sleep(2)
        self.click(Locators.D1)
        time.sleep(2)
        self.enter_text(Locators.R_LANG, "Tamil")
        time.sleep(2)
        self.click(Locators.P_SUBMIT_BUTTON)
        time.sleep(2)
        # Conatact
        # present Address
        self.click(Locators.T2)
        time.sleep(2)
        self.click(Locators.R_ADDR)
        time.sleep(2)
        self.enter_text(Locators.R_ADDR, "6/616,samypuram colony,Sivakasi")
        time.sleep(2)
        self.enter_text(Locators.R_TALUK, "Virudhunagar")
        time.sleep(2)
        self.enter_text(Locators.R_PIN, "626189")
        time.sleep(2)
        self.enter_text(Locators.R_CONTACT, "963875478")
        time.sleep(2)
        self.enter_text(Locators.R_DIST, "Virudhunagar")
        time.sleep(2)
        self.enter_text(Locators.R_TELE, "963857485")
        time.sleep(2)
        self.enter_text(Locators.R_EME, "96385748556")
        time.sleep(2)
        self.click(Locators.R_CITY)
        time.sleep(2)
        self.click(Locators.D8)
        time.sleep(2)
        self.click(Locators.R_STATE)
        time.sleep(2)
        self.click(Locators.D11)
        time.sleep(2)
        self.enter_text(Locators.R_MOBILE, "9638527410")
        time.sleep(2)
        self.enter_text(Locators.R_PERMAIL, "rajesh2512@gmail.com")
        time.sleep(2)
        self.click(Locators.R_VILLAGE)
        time.sleep(2)
        self.click(Locators.D11)
        time.sleep(2)
        self.click(Locators.R_COUNTRY)
        time.sleep(2)
        self.click(Locators.D11)
        time.sleep(2)
        self.enter_text(Locators.R_CONTACTPER, "7894561230")
        time.sleep(2)
        self.enter_text(Locators.R_OFFICAL, "rajesshdev@gmail.com")
        time.sleep(2)
        # parmanent
        self.click(Locators.R_PERMANANT1)
        time.sleep(2)
        # self.click(Locators.SAME)
        # time.sleep(2)
        self.click(Locators.R_ADDR1)
        time.sleep(2)
        self.enter_text(Locators.R_ADDR1, "6/616,samypuram colony,Sivakasi")
        time.sleep(2)
        self.enter_text(Locators.R_TALUK1, "Virudhunagar")
        time.sleep(2)
        self.enter_text(Locators.R_PIN1, "626189")
        time.sleep(2)
        self.enter_text(Locators.R_CONTACT, "963875478")
        time.sleep(2)
        self.enter_text(Locators.R_DIST1, "Virudhunagar")
        time.sleep(2)
        self.enter_text(Locators.R_TELE1, "963857485")
        time.sleep(2)
        self.enter_text(Locators.R_EME, "96385748556")
        time.sleep(2)
        self.click(Locators.R_CITY1)
        time.sleep(1)
        self.click(Locators.D11)
        time.sleep(2)
        self.click(Locators.R_STATE1)
        time.sleep(5)
        self.click(Locators.D11)
        time.sleep(2)
        self.enter_text(Locators.R_MOBILE1, "9638527410")
        time.sleep(2)
        self.enter_text(Locators.R_PERMAIL, "rajesh2512@gmail.com")
        time.sleep(2)
        self.click(Locators.R_VILLAGE1)
        time.sleep(2)
        self.click(Locators.D11)
        time.sleep(2)
        self.click(Locators.R_COUNTRY1)
        time.sleep(2)
        self.click(Locators.D11)
        time.sleep(2)
        self.enter_text(Locators.R_CONTACTPER, "7894561230")
        time.sleep(2)
        self.enter_text(Locators.R_OFFICAL, "rajesshdev@gmail.com")
        time.sleep(2)
        self.click(Locators.P_SUBMIT_BUTTON)
        time.sleep(2)
        # Identity
        self.click(Locators.T3)
        time.sleep(1)
        self.click(Locators.P_SUBMIT_BUTTON)
        time.sleep(2)
        self.click(Locators.R_AADHARNO)
        time.sleep(1)
        self.enter_text(Locators.R_AADHARNO, "63958574145238")
        time.sleep(2)
        self.enter_text(Locators.R_DRIVENO, "852496556")
        time.sleep(2)
        self.enter_text(Locators.R_PAN, "ZDF456646")
        time.sleep(2)
        self.enter_text(Locators.R_ADOB, "25122001")
        time.sleep(2)
        self.enter_text(Locators.R_PASSNO, "8565664644646")
        time.sleep(2)
        self.enter_text(Locators.R_ISSUEDATE, "10252020")
        time.sleep(2)
        self.enter_text(Locators.R_PLACE, 'Madurai')
        time.sleep(2)
        self.enter_text(Locators.R_EXPIRY, "10062018")
        time.sleep(2)
        self.click(Locators.R_ID)
        time.sleep(2)
        self.click(Locators.D8)
        time.sleep(2)
        self.click(Locators.R_AGE)
        time.sleep(2)
        self.click(Locators.D8)
        time.sleep(2)
        self.click(Locators.R_ADDPROOF)
        time.sleep(2)
        self.click(Locators.D8)
        time.sleep(2)
        self.enter_text(Locators.R_REF, "sdxfcgvhb")
        time.sleep(2)
        self.click(Locators.R_ADD1)
        time.sleep(2)
        self.click(Locators.D8)
        time.sleep(2)
        self.click(Locators.R_ADD2)
        time.sleep(2)
        self.click(Locators.D8)
        time.sleep(2)
        self.click(Locators.R_ADD3)
        time.sleep(2)
        self.click(Locators.D8)
        time.sleep(2)
        self.click(Locators.P_SUBMIT_BUTTON)
        time.sleep(2)
        # PF/ESI
        self.click(Locators.T4)
        time.sleep(2)
        self.click(Locators.R_PFNO)
        time.sleep(2)
        self.enter_text(Locators.R_PFNO, "8456546")
        time.sleep(2)
        self.enter_text(Locators.R_UAN, "4656464")
        time.sleep(2)
        self.enter_text(Locators.R_PFDATE, "25122010")
        time.sleep(2)
        self.enter_text(Locators.R_PFREL, "18102022")
        time.sleep(2)
        self.enter_text(Locators.R_REASON, "dxfcgvh")
        time.sleep(2)
        self.enter_text(Locators.R_ESINO, "565131")
        time.sleep(2)
        self.enter_text(Locators.R_ISSUEDATE, "10022015")
        time.sleep(2)
        self.enter_text(Locators.R_EXPIRY, "15122022")
        time.sleep(2)
        self.enter_text(Locators.R_ESIRELIV, "19112025")
        time.sleep(2)
        self.enter_text(Locators.R_INSUR, "xdfgh")
        time.sleep(2)
        self.enter_text(Locators.R_INSURNO, "5566644")
        time.sleep(2)
        self.click(Locators.P_SUBMIT_BUTTON)
        time.sleep(2)
        # Bankedetails
        self.click(Locators.T5)
        time.sleep(2)
        self.click(Locators.R_ADD_BUTTON)
        time.sleep(2)
        self.click(Locators.R_BANKCODE)
        time.sleep(2)
        self.enter_text(Locators.R_BANKCODE,"TMB")
        time.sleep(2)
        self.send_keys(Locators.R_BANKCODE,Keys.ARROW_DOWN)
        time.sleep(2)
        self.send_keys(Locators.R_BANKCODE,Keys.ENTER)
        time.sleep(2)
        self.click(Locators.R_BNAME)
        time.sleep(5)
        self.enter_text(Locators.R_BNAME,"TMB")
        time.sleep(2)
        self.send_keys(Locators.R_BNAME,Keys.ARROW_DOWN)
        time.sleep(2)
        self.send_keys(Locators.R_BNAME,Keys.ENTER)
        time.sleep(2)
        self.click(Locators.R_BIFSC)
        time.sleep(2)
        self.enter_text(Locators.R_BIFSC,"BKID0008225")
        time.sleep(2)
        self.send_keys(Locators.R_BIFSC, Keys.ARROW_DOWN)
        time.sleep(2)
        self.send_keys(Locators.R_BIFSC, Keys.ENTER)
        time.sleep(2)
        self.click(Locators.R_BRANCH)
        time.sleep(2)
        self.enter_text(Locators.R_BRANCH,"SIvakasi")
        time.sleep(2)
        self.send_keys(Locators.R_BRANCH, Keys.ARROW_DOWN)
        time.sleep(2)
        self.send_keys(Locators.R_BRANCH, Keys.ENTER)
        time.sleep(2)
        self.click(Locators.R_BTYPE)
        time.sleep(2)
        self.click(Locators.D1)
        time.sleep(2)
        self.enter_text(Locators.R_ACNO, "93458770135")
        time.sleep(2)
        self.click(Locators.R_SALAC)
        time.sleep(2)
        self.click(Locators.D1)
        time.sleep(2)
        self.click(Locators.R_SUBMIT)
        time.sleep(2)
        self.click(Locators.R_ADD_BUTTON)
        time.sleep(2)
        self.enter_text(Locators.R_ACNO, "15615")
        time.sleep(2)
        self.click(Locators.CANC)
        time.sleep(2)
        self.click(Locators.R_ADD_BUTTON)
        time.sleep(2)
        self.click(Locators.R_SUBMIT)
        time.sleep(2)
        # self.click(Locators.CANC)
        # time.sleep(2)
        self.click(Locators.R_DELETE)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)

        # Education details
        self.click(Locators.T6)
        time.sleep(2)
        self.click(Locators.R_ADD_BUTTON)
        time.sleep(2)
        self.enter_text(Locators.R_COURSE, 'B.E')
        time.sleep(2)
        self.enter_text(Locators.R_INSISTUTION, 'P.S.R')
        time.sleep(2)
        self.enter_text(Locators.R_YOP, '2022')
        time.sleep(2)
        self.enter_text(Locators.R_PERCENTAGE, '89%')
        time.sleep(2)
        self.click(Locators.R_SUBMIT)
        time.sleep(2)
        self.click(Locators.R_ADD_BUTTON)
        time.sleep(2)
        self.enter_text(Locators.R_COURSE, 'B.E')
        time.sleep(2)
        self.enter_text(Locators.R_INSISTUTION, 'P.S.R')
        time.sleep(2)
        self.enter_text(Locators.R_YOP, '2022')
        time.sleep(2)
        self.enter_text(Locators.R_PERCENTAGE, '89%')
        time.sleep(2)
        self.click(Locators.R_SUBMIT)
        time.sleep(2)
        self.click(Locators.R_ADD_BUTTON)
        time.sleep(2)
        self.enter_text(Locators.R_COURSE, 'B.E')
        time.sleep(2)
        self.enter_text(Locators.R_INSISTUTION, 'P.S.R')
        time.sleep(2)
        self.enter_text(Locators.R_YOP, '2022')
        time.sleep(2)
        self.enter_text(Locators.R_PERCENTAGE, '89%')
        time.sleep(2)
        self.click(Locators.CANC)
        time.sleep(2)
        self.click(Locators.R_ADD_BUTTON)
        time.sleep(2)
        self.click(Locators.R_SUBMIT)
        time.sleep(2)
        self.click(Locators.CANC)
        time.sleep(2)
        self.click(Locators.R_DELETE)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        self.click(Locators.ROW)
        time.sleep(2)
        self.click(Locators.R_DELETE)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        # Family details
        self.click(Locators.T7)
        time.sleep(2)
        self.click(Locators.R_ADD_BUTTON)
        time.sleep(2)
        self.enter_text(Locators.RNAME, 'Raj')
        time.sleep(2)
        self.enter_text(Locators.RDOB, '10091999')
        time.sleep(2)
        self.enter_text(Locators.RAGE, '23')
        time.sleep(2)
        self.click(Locators.RELEATION)
        time.sleep(5)
        self.click(Locators.D1)
        time.sleep(2)
        self.enter_text(Locators.R_OCCU, 'dfgyuh')
        time.sleep(2)
        self.click(Locators.R_NOMINEE)
        time.sleep(1)
        self.click(Locators.D1)
        time.sleep(2)
        self.enter_text(Locators.R_PER, '90')
        time.sleep(2)
        self.click(Locators.SUBMI)
        time.sleep(2)
        self.click(Locators.ADD_BUTTON)
        time.sleep(2)
        self.enter_text(Locators.RNAME,'Veera')
        time.sleep(2)
        self.enter_text(Locators.RDOB,'10091996')
        time.sleep(2)
        self.enter_text(Locators.RAGE,'26')
        time.sleep(2)
        self.click(Locators.RELEATION)
        time.sleep(1)
        self.click(Locators.D2)
        time.sleep(2)
        self.enter_text(Locators.R_OCCU,'dfgyuh')
        time.sleep(2)
        self.click(Locators.R_NOMINEE)
        time.sleep(1)
        self.click(Locators.D1)
        time.sleep(2)
        self.enter_text(Locators.R_PER,'90')
        time.sleep(2)
        self.click(Locators.R_SUBMIT)
        time.sleep(2)
        self.click(Locators.ADD_BUTTON)
        time.sleep(2)
        self.enter_text(Locators.RNAME,'Raj')
        time.sleep(2)
        self.enter_text(Locators.RDOB,'10091999')
        time.sleep(2)
        self.enter_text(Locators.RAGE,'23')
        time.sleep(2)
        self.click(Locators.RELEATION)
        time.sleep(1)
        self.click(Locators.D1)
        time.sleep(2)
        self.enter_text(Locators.R_OCCU,'dfgyuh')
        time.sleep(2)
        self.click(Locators.R_NOMINEE)
        time.sleep(1)
        self.click(Locators.D1)
        time.sleep(2)
        self.enter_text(Locators.R_PER,'90')
        time.sleep(2)
        self.click(Locators.CANC)
        time.sleep(2)
        self.click(Locators.ADD_BUTTON)
        self.click(Locators.SUBMI)
        self.click(Locators.CANC)
        self.click(Locators.R_DELETE)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        self.click(Locators.ROW)
        time.sleep(2)
        self.click(Locators.R_DELETE)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        # Previous Empolyee details
        self.click(Locators.T8)
        time.sleep(2)
        self.click(Locators.R_ADD_BUTTON)
        time.sleep(2)
        self.enter_text(Locators.R_DESG, "Software Testing")
        time.sleep(2)
        self.enter_text(Locators.R_EXPY, "5 Years")
        time.sleep(2)
        self.click(Locators.R_YEAR)
        time.sleep(2)
        self.click(Locators.D2)
        time.sleep(2)
        self.enter_text(Locators.R_SALARY, "30000")
        time.sleep(2)
        self.click(Locators.SUBMI)
        time.sleep(2)
        # self.click(Locators.PRADD)
        # time.sleep(2)
        # self.enter_text(Locators.R_DESG, "Software Testing")
        # time.sleep(2)
        # self.enter_text(Locators.R_EXPY, "5 Years")
        # time.sleep(2)
        # self.click(Locators.R_YEAR)
        # time.sleep(2)
        # self.click(Locators.D2)
        # time.sleep(2)
        # self.enter_text(Locators.R_SALARY, "30000")
        # time.sleep(2)
        # self.click(Locators.R_SUBMIT)
        # time.sleep(2)
        # self.click(Locators.R_ADD_BUTTON)
        # time.sleep(2)
        # self.enter_text(Locators.R_DESG, "Software Testing")
        # time.sleep(2)
        # self.enter_text(Locators.R_EXPY, "5 Years")
        # time.sleep(2)
        # self.click(Locators.R_YEAR)
        # time.sleep(2)
        # self.click(Locators.D2)
        # time.sleep(2)
        # self.enter_text(Locators.R_SALARY, "30000")
        # time.sleep(2)
        # self.click(Locators.R_CANCEL)
        # time.sleep(2)
        # self.click(Locators.R_ADD_BUTTON)
        # time.sleep(2)
        # self.click(Locators.RCANCEL)
        # time.sleep(2)
        self.click(Locators.DELETE_BUTTON)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        # self.click(Locators.ROW)
        # time.sleep(2)
        # self.click(Locators.DELETE_BUTTON)
        # time.sleep(2)
        # self.driver.switch_to.alert.accept()
        # time.sleep(2)
        # Training details
        self.click(Locators.T9)
        time.sleep(2)
        self.click(Locators.R_ADD_BUTTON)
        time.sleep(2)
        self.enter_text(Locators.R_DATE, "25062022")
        time.sleep(2)
        self.enter_text(Locators.R_TITLE, "Testing")
        time.sleep(2)
        self.enter_text(Locators.R_LOCATION, "Chennai")
        time.sleep(2)
        self.enter_text(Locators.R_DUR, "6 Months")
        time.sleep(2)
        self.enter_text(Locators.R_CONDUCT, "IBM")
        time.sleep(2)
        self.enter_text(Locators.REMARK, "dxfcghjk")
        time.sleep(2)
        self.click(Locators.R_SUBMIT)
        time.sleep(2)
        # self.click(Locators.R_ADD_BUTTON)
        # time.sleep(2)
        # self.enter_text(Locators.R_DATE, "25062022")
        # time.sleep(2)
        # self.enter_text(Locators.R_TITLE, "Testing")
        # time.sleep(2)
        # self.enter_text(Locators.R_LOCATION, "Chennai")
        # time.sleep(2)
        # self.enter_text(Locators.R_DUR, "6 Months")
        # time.sleep(2)
        # self.enter_text(Locators.R_CONDUCT, "IBM")
        # time.sleep(2)
        # self.enter_text(Locators.REMARK, "dxfcghjk")
        # time.sleep(2)
        # self.click(Locators.R_SUBMIT)
        # time.sleep(2)
        # self.click(Locators.R_ADD_BUTTON)
        # time.sleep(2)
        # self.enter_text(Locators.R_DATE, "25062022")
        # time.sleep(2)
        # self.enter_text(Locators.R_TITLE, "Testing")
        # time.sleep(2)
        # self.enter_text(Locators.R_LOCATION, "Chennai")
        # time.sleep(2)
        # self.enter_text(Locators.R_DUR, "6 Months")
        # time.sleep(2)
        # self.enter_text(Locators.R_CONDUCT, "IBM")
        # time.sleep(2)
        # self.enter_text(Locators.REMARK, "dxfcghjk")
        # time.sleep(2)
        # self.click(Locators.R_CANCEL)
        # time.sleep(2)
        self.click(Locators.DELETE_BUTTON)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        # self.click(Locators.ROW)
        # time.sleep(2)
        # self.click(Locators.DELETE_BUTTON)
        # time.sleep(2)
        # self.driver.switch_to.alert.accept()
        # time.sleep(2)
        # leave Type
        self.click(Locators.T10)
        time.sleep(2)
        self.click(Locators.R_ADD_BUTTON)
        time.sleep(2)
        self.enter_text(Locators.R_LEAVE, "SICK Leave")
        time.sleep(2)
        self.enter_text(Locators.R_TLEAVE, "5Days")
        time.sleep(2)
        self.enter_text(Locators.NOTES, "drfghu")
        time.sleep(2)
        self.click(Locators.R_SUBMIT)
        time.sleep(2)
        # self.click(Locators.R_ADD_BUTTON)
        # time.sleep(2)
        # self.enter_text(Locators.R_LEAVE, "SICK Leave")
        # time.sleep(2)
        # self.enter_text(Locators.R_TLEAVE, "5Days")
        # time.sleep(2)
        # self.enter_text(Locators.NOTES, "drfghu")
        # time.sleep(2)
        # self.click(Locators.R_SUBMIT)
        # time.sleep(2)
        # self.click(Locators.R_ADD_BUTTON)
        # time.sleep(2)
        # self.enter_text(Locators.R_LEAVE, "SICK Leave")
        # time.sleep(2)
        # self.enter_text(Locators.R_TLEAVE, "5Days")
        # time.sleep(2)
        # self.enter_text(Locators.NOTES, "drfghu")
        # time.sleep(2)
        # self.click(Locators.R_CANCEL)
        # time.sleep(2)
        self.click(Locators.DELETE_BUTTON)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        # self.click(Locators.ROW)
        # time.sleep(2)
        # self.click(Locators.DELETE_BUTTON)
        # time.sleep(2)
        self.click(Locators.BACK)
        time.sleep(5)


# EDit empolyee details

        self.click(Locators.ROW)
        time.sleep(2)
        self.click(Locators.ROW1)
        time.sleep(2)
        self.click(Locators.EDIT_BUTTON)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        self.click(Locators.ROW1)
        time.sleep(2)
        self.click(Locators.EDIT_BUTTON)
        time.sleep(2)
        self.click(Locators.R_FIRSTE)
        time.sleep(2)
        self.send_keys(Locators.R_FIRSTE, Keys.CONTROL + 'a')
        time.sleep(2)
        self.send_keys(Locators.R_FIRSTE, Keys.DELETE)
        time.sleep(2)
        self.enter_text(Locators.R_FIRSTE, "Rajesh")
        time.sleep(2)
        self.click(Locators.R_SAVE)
        time.sleep(2)
        # edit Empolyement
        self.click(Locators.T1)
        time.sleep(2)
        self.click(Locators.R_OLD)
        time.sleep(2)
        self.send_keys(Locators.R_OLD, Keys.CONTROL + 'a')
        time.sleep(2)
        self.send_keys(Locators.R_OLD, Keys.DELETE)
        time.sleep(2)
        self.enter_text(Locators.R_OLD, "251")
        time.sleep(2)
        self.click(Locators.R_SAVE)
        time.sleep(2)
        # Contact
        self.click(Locators.T2)
        time.sleep(2)
        self.click(Locators.R_AADRESS)
        time.sleep(2)
        self.send_keys(Locators.R_AADRESS, Keys.CONTROL + 'a')
        time.sleep(2)
        self.send_keys(Locators.R_AADRESS, Keys.DELETE)
        time.sleep(2)
        self.enter_text(Locators.R_AADRESS, "6/612,Samy puram colony,Sivakasi,Virudhunagar")
        time.sleep(2)
        self.click(Locators.R_PERMANANT)
        time.sleep(2)
        self.click(Locators.SAME)
        time.sleep(2)
        self.click(Locators.R_SAVE)
        time.sleep(2)
        # edit Identity
        self.click(Locators.T3)
        time.sleep(2)
        self.click(Locators.R_AADHARNO)
        time.sleep(2)
        self.send_keys(Locators.R_AADHARNO, Keys.CONTROL + 'a')
        time.sleep(2)
        self.send_keys(Locators.R_AADHARNO, Keys.DELETE)
        time.sleep(2)
        self.enter_text(Locators.R_AADHARNO, "6335934753563")
        time.sleep(2)
        self.click(Locators.SAVE)
        time.sleep(2)
        # edit PF/esi
        self.click(Locators.T4)
        time.sleep(2)
        self.click(Locators.R_PFNO)
        time.sleep(2)
        self.send_keys(Locators.R_PFNO, Keys.CONTROL + 'a')
        time.sleep(2)
        self.send_keys(Locators.R_PFNO, Keys.DELETE)
        time.sleep(2)
        self.enter_text(Locators.R_PFNO, "9345870")
        time.sleep(2)
        self.click(Locators.SAVE)
        time.sleep(2)
        # Edit bank details
        self.click(Locators.T5)
        time.sleep(2)
        self.click(Locators.R_EDIT_BUTTON)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        self.click(Locators.ROW)
        time.sleep(2)
        # self.click(Locators.ROW1)
        # time.sleep(2)
        # self.click(Locators.R_EDIT_BUTTON)
        # time.sleep(2)
        # self.driver.switch_to.alert.accept()
        # time.sleep(2)
        # self.click(Locators.ROW1)
        # time.sleep(2)
        self.click(Locators.R_EDIT_BUTTON)
        time.sleep(2)
        self.click(Locators.R_ACNO)
        time.sleep(2)
        self.send_keys(Locators.R_ACNO, Keys.CONTROL + 'a')
        time.sleep(2)
        self.send_keys(Locators.R_ACNO, Keys.DELETE)
        time.sleep(2)
        self.enter_text(Locators.R_ACNO, "566468653546865")
        time.sleep(2)
        self.click(Locators.R_SUBMIT)
        time.sleep(2)
        self.click(Locators.R_ADD_BUTTON)
        time.sleep(2)
        self.click(Locators.R_BANKCODE)
        time.sleep(2)
        self.click(Locators.D8)
        time.sleep(2)
        self.click(Locators.R_BNAME)
        time.sleep(5)
        self.click(Locators.D8)
        time.sleep(2)
        self.click(Locators.R_BIFSC)
        time.sleep(2)
        self.click(Locators.D8)
        time.sleep(2)
        self.click(Locators.R_BRANCH)
        time.sleep(2)
        self.click(Locators.D8)
        time.sleep(2)
        self.click(Locators.R_BTYPE)
        time.sleep(2)
        self.click(Locators.D2)
        time.sleep(2)
        self.enter_text(Locators.R_ACNO, "12324354657")
        time.sleep(2)
        self.click(Locators.R_SALAC)
        time.sleep(2)
        self.click(Locators.D1)
        time.sleep(2)
        self.click(Locators.R_SUBMIT)
        time.sleep(2)
        # edit Educational details
        self.click(Locators.T6)
        time.sleep(2)
        self.click(Locators.ROW)
        time.sleep(2)
        self.click(Locators.R_EDIT_BUTTON)
        time.sleep(2)
        self.click(Locators.R_YOP)
        time.sleep(2)
        self.send_keys(Locators.R_YOP, Keys.CONTROL + 'a')
        time.sleep(2)
        self.send_keys(Locators.R_YOP, Keys.DELETE)
        time.sleep(2)
        self.enter_text(Locators.R_YOP, "2021")
        time.sleep(2)
        self.click(Locators.R_SUBMIT)
        time.sleep(2)
        # edit Family details
        self.click(Locators.T7)
        time.sleep(2)
        self.click(Locators.ROW)
        time.sleep(2)
        self.click(Locators.R_EDIT_BUTTON)
        time.sleep(2)
        self.click(Locators.RDOB)
        time.sleep(2)
        self.send_keys(Locators.RDOB, Keys.CONTROL + 'a')
        time.sleep(2)
        self.send_keys(Locators.RDOB, Keys.DELETE)
        time.sleep(2)
        self.click(Locators.R_SUBMIT)
