import configparser
import unittest

from selenium import webdriver

config = configparser.ConfigParser()
config.read("./settings.conf")


class TestBase(unittest.TestCase):
    """
    Base test class to initiate web driver in one place and reuse it everywhere.
    """
    def setUp(self) -> None:
        """
        Setup google driver
        :return:
        """
        chrome_options = webdriver.ChromeOptions()

        self.driver = webdriver.Chrome(executable_path=config['ipss']['CHROME_DRIVER_LOCATION'],
                                       options=chrome_options)
        self.driver.get(config['ipss']['TEST_URL'])

    def tearDown(self):
        # Cleanup driver to solve memory issues
        self.driver.close()
        self.driver.quit()
