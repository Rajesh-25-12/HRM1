import time

from selenium.webdriver.common.keys import Keys

from ipss_automation.base import BasePage
from selenium.webdriver.common.by import By
from ipss_automation.locators import Locators
from ipss_automation.utils import get_otp_value


class Pro(BasePage):
    """
    Login common module for all user roles.
    """
    def __init__(self, driver):
        super().__init__(driver)

    def pim(self):
        self.click(Locators.DRAW)
        time.sleep(2)
        self.click(Locators.PAY)
        time.sleep(2)
        self.click(Locators.PRODUCTIVE)
        time.sleep(2)
        self.click(Locators.ROUTE)
        self.driver.switch_to.alert.accept()
        time.sleep(5)
        self.click(Locators.EDII1)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(5)
        self.click(Locators.DELE1)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(5)
        self.click(Locators.SLET)
        self.click((Locators.SLECT))
        time.sleep(2)
        self.click(Locators.ROUTE)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(5)

        self.click(Locators.ADD)
        time.sleep(2)
        # self.enter_text(Locators.CODE, "2112")
        # time.sleep(2)
        # self.enter_text(Locators.CNA, "vnna")
        # time.sleep(2)
        # self.enter_text(Locators.FYE, "2022-04-04")
        # time.sleep(2)
        # self.enter_text(Locators.PCAT, "123")
        # time.sleep(2)
        # self.enter_text(Locators.PCO, "Y132")
        # time.sleep(2)
        # self.enter_text(Locators.PPE, "July2022")
        # time.sleep(2)
        # self.enter_text(Locators.PDES, "Voice")
        # time.sleep(2)
        # self.enter_text(Locators.TOT, "14500")
        # time.sleep(2)
        #
        self.click(Locators.CAN1)
        time.sleep(2)


        self.click(Locators.ADD)
        time.sleep(2)
        self.enter_text(Locators.CODE,"2112")
        time.sleep(2)
        self.enter_text(Locators.CNA,"123")
        time.sleep(2)
        self.enter_text(Locators.FYE,"2022")
        time.sleep(2)
        self.enter_text(Locators.PCAT,"123")
        time.sleep(2)
        self.enter_text(Locators.PCO,"132")
        time.sleep(2)
        self.enter_text(Locators.PPE,"2022")
        time.sleep(2)
        self.enter_text(Locators.PDES,"123")
        time.sleep(2)
        self.enter_text(Locators.TOT,"14500")
        time.sleep(2)
        self.click(Locators.SUB2)
        time.sleep(2)

        self.click(Locators.SELECT)
        time.sleep(2)
        self.click(Locators.EDII1)
        time.sleep(2)
        self.enter_text(Locators.CNA, "vnr")
        time.sleep(2)
        self.send_keys(Locators.CNA, Keys.CONTROL +"a")
        self.send_keys(Locators.CNA, Keys.DELETE)
        self.enter_text(Locators.CNA, "vnr")
        self.click(Locators.SUB1)
        time.sleep(2)
        self.click(Locators.DELE1)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(5)
        self.click(Locators.DOWN1)
        time.sleep(5)

        self.click(Locators.CELL)
        time.sleep(2)
        self.enter_text(Locators.CELL,"RK")
        time.sleep(2)
        self.send_keys(Locators.CELL,Keys.ENTER)
        time.sleep(2)
        self.click(Locators.SAVE)
        time.sleep(2)

        self.click(Locators.ROUTE)
        time.sleep(2)

        self.click(Locators.ADDTE)
        time.sleep(2)
        self.click(Locators.CAN1)
        time.sleep(2)

        self.click(Locators.ADDTE)
        time.sleep(2)
        self.enter_text(Locators.EMPNAME, "vnr")
        time.sleep(2)
        self.enter_text(Locators.EMPID, "vnr11")
        time.sleep(2)
        self.enter_text(Locators.DAT, "12/01/2000")
        time.sleep(2)
        self.enter_text(Locators.AMP, "2000")
        time.sleep(2)
        self.enter_text(Locators.NOT,"ASAP")
        time.sleep(2)
        self.click(Locators.SUB1)
        time.sleep(2)
        self.click(Locators.SLET)
        time.sleep(2)
        self.click(Locators.DELE2)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(5)
        self.click(Locators.DOWN2)
        time.sleep(2)

        self.driver.back()
        time.sleep(2)

