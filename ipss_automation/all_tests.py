import unittest
from fileinput import filename

import HtmlTestRunner
import logging

from ipss_automation.ipss_test_cases.Attendance.on_duty_entry_master import Duty
from ipss_automation.ipss_test_cases.Attendance.security_buyer_attendance import Security_buyer
from ipss_automation.ipss_test_cases.General.Dashboard import Dashboard
from ipss_automation.ipss_test_cases.General.EmpolyeeMaster import Empolyee
from ipss_automation.ipss_test_cases.Master_data.Vechile_page import Vec
from ipss_automation.ipss_test_cases.Master_data.Village import Village
from ipss_automation.ipss_test_cases.Master_data.individual_pay import Individual_pay
from ipss_automation.ipss_test_cases.Master_data.pay_transaction import Transaction
from ipss_automation.ipss_test_cases.Payroll_master.pay_strc import Payroll
from ipss_automation.ipss_test_cases.Payroll_master.pf import PF
from ipss_automation.ipss_test_cases.Payroll_master.production import Pro
from ipss_automation.ipss_test_cases.authentication.login import Login

from ipss_automation.ipss_test_cases.Attendance.Attendance_entry import Attendanceentry
from ipss_automation.ipss_test_cases.Attendance.Manual_OT_Entry import Manual_OT_Entry
from ipss_automation.ipss_test_cases.Master_data.bank import Banking
from ipss_automation.ipss_test_cases.authentication.logout import Logout

from ipss_automation.test_base import TestBase


class AllTests(TestBase, unittest.TestCase):
    """
    Run all test cases here
    """

    def setUp(self) -> None:
        """
        Chrome driver setup from Base class
        :return:
        """

        super().setUp()

    def test_login_again(self):
        # Initiate Login
        self.login = Login(self.driver)
        self.login.do_login()
        # self.logout = Logout(self.driver)
        # self.logout.do_logout()

    def test_log(self):
        logging.basicConfig(level=logging.INFO, filename="D:/Ipss/ipss_automation/test.log", filemode='a',
                            format='Date and Time : %(asctime)s -%(created)f- Line number : %(lineno)d - %(message)s',
                            datefmt='%d-%b-%y %H:%M:%S')

    def test_empolye(self):
        self.login = Login(self.driver)
        self.login.do_login()
        self.emp = Empolyee(self.driver)
        self.emp.empolyee()

    def test_a_dashboard(self):
        self.login = Login(self.driver)
        self.login.do_login()
        self.dash = Dashboard(self.driver)
        self.dash.dashboard()

    def test_b_attendance_entry(self):
        self.login = Login(self.driver)
        self.login.do_login()
        self.entry = Attendanceentry(self.driver)
        self.entry.Attendance()

    def test_c_manual_entry(self):
        self.login = Login(self.driver)
        self.login.do_login()
        self.ot = Manual_OT_Entry(self.driver)
        self.ot.Manual()

    def test_on_duty(self):
        self.login = Login(self.driver)
        self.login.do_login()
        self.od = Duty(self.driver)
        self.od.dutymaster()

    def test_d_security_buyer(self):
        self.login = Login(self.driver)
        self.login.do_login()
        self.attendance = Security_buyer(self.driver)
        self.attendance.security()

    def test_e_banking(self):
        self.login = Login(self.driver)
        self.login.do_login()
        self.bank = Banking(self.driver)
        self.bank.banking()

    """def test_f_individual_pay(self):
        self.login = Login(self.driver)
        self.login.do_login()
        self.pay = Individual_pay(self.driver)
        self.pay.individual()

    def test_g_master_data(self):
        self.login = Login(self.driver)
        self.login.do_login()
        self.paym = Transaction(self.driver)
        self.paym.pay()"""

    def test_h_vehchile(self):
        self.login = Login(self.driver)
        self.login.do_login()
        self.Vechile = Vec(self.driver)
        self.Vechile.master()

    """def test_i_villagem(self):
        # Initiate Login
        self.login = Login(self.driver)
        self.login.do_login()
        self.master = Village(self.driver)
        self.master.masterdata()

    def test_j_payroll(self):
        self.login = Login(self.driver)
        self.login.do_login()
        self.master = Payroll(self.driver)
        self.master.Payrollp()

    def test_k_esipf(self):
        self.login = Login(self.driver)
        self.login.do_login()

        self.esipf = PF(self.driver)
        self.esipf.pfesi()

    def test_l_production(self):
        self.login = Login(self.driver)
        self.login.do_login()

        self.pro = Pro(self.driver)
        self.pro.pim()"""


if __name__ == '__main__':
    # Run test cases
    test_suite = unittest.TestSuite()
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        title='Ipss', description='Result of tests', open_in_browser=True, tested_by='Testing Team'))

    test_suite.addTest(AllTests('test_login_again'))
    test_suite.addTest(AllTests('test_log'))
    # # test_suite.addTest(AllTests('test_empolye'))
    test_suite.addTest(AllTests('test_a_dashboard'))
    test_suite.addTest(AllTests('test_b_attendance_entry'))
    test_suite.addTest(AllTests('test_c_manual_entry'))
    test_suite.addTest(AllTests('test_d_security_buyer'))
    test_suite.addTest(AllTests('test_e_banking'))
    # # test_suite.addTest(AllTests('test_f_individual_pay'))
    # test_suite.addTest(AllTests('test_g_master_data'))
    test_suite.addTest(AllTests('test_h_vehchile'))
    # # test_suite.addTest(AllTests('test_i_villagem'))
    # # test_suite.addTest(AllTests('test_j_payroll'))
    # # test_suite.addTest(AllTests('test_k_esipf'))
    # # test_suite.addTest(AllTests('test_l_production'))

    unittest.TextTestRunner().run(test_suite)
