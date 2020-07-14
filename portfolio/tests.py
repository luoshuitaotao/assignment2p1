import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class assignment2p1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox ()

    def test_add_new_investment(self):
        user = "instructor"
        pwd = "maverick1a"
        driver = self.driver
        #driver.maximize_window ()
        driver.get ("http://127.0.0.1:8000/admin")
        elem = driver.find_element_by_id ("id_username")
        elem.send_keys (user)
        time.sleep(8)
        elem = driver.find_element_by_id ("id_password")
        elem.send_keys (pwd)
        time.sleep(8)
        elem.send_keys (Keys.RETURN)
        assert "Logged In"
        time.sleep (8)

        def tearDown(self):
            self.driver.close ()
