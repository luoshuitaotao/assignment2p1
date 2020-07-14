import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class assignment2p1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome ()

    def test_investment(self):
        user = "instructor"
        pwd = "maverick1a"
        driver = self.driver
        driver.maximize_window ()
        driver.get ("http://127.0.0.1:8000/admin")
        elem = driver.find_element_by_id ("id_username")
        elem.send_keys (user)
        time.sleep(0)
        elem = driver.find_element_by_id ("id_password")
        elem.send_keys (pwd)
        time.sleep(0)
        elem.send_keys (Keys.RETURN)
        assert "Logged In"
        time.sleep (0)

        #test add a new investment
        driver.get ("http://127.0.0.1:8000/investment/create/")
        select = Select (driver.find_element_by_name ('customer'))
        select.select_by_visible_text ('50712')
        time.sleep(3)
        elem = driver.find_element_by_id ("id_category")
        elem.send_keys ('fund')
        time.sleep (3)
        elem = driver.find_element_by_id ("id_description")
        elem.send_keys ('fund1')
        time.sleep (3)
        elem = driver.find_element_by_id ("id_acquired_value")
        elem.send_keys ('10')
        time.sleep (3)
        elem = driver.find_element_by_id ("id_acquired_date")
        elem.clear()
        elem.send_keys ('2020-07-12')
        time.sleep (3)
        elem = driver.find_element_by_id ("id_recent_value")
        elem.send_keys ('20')
        time.sleep (3)
        elem = driver.find_element_by_id ("id_recent_date")
        elem.clear()
        elem.send_keys ('2020-07-13')
        time.sleep (3)
        driver.find_element_by_xpath ("html/body/div/div/div/form/button").click ()
        time.sleep(5)

        #test edit investment
        driver.get ("http://127.0.0.1:8000/investment/15/edit/")
        select = Select (driver.find_element_by_id('id_customer'))
        select.select_by_visible_text ('50712')
        time.sleep(3)
        elem = driver.find_element_by_id ("id_category")
        elem.clear()
        elem.send_keys ('test')
        time.sleep (3)
        elem = driver.find_element_by_id ("id_description")
        elem.clear()
        elem.send_keys ('test')
        time.sleep (3)
        elem = driver.find_element_by_id ("id_acquired_value")
        elem.clear()
        elem.send_keys ('3')
        time.sleep (3)
        elem = driver.find_element_by_id ("id_acquired_date")
        elem.clear()
        elem.send_keys ('2020-07-10')
        time.sleep (3)
        elem = driver.find_element_by_id ("id_recent_value")
        elem.clear()
        elem.send_keys ('1')
        time.sleep (3)
        elem = driver.find_element_by_id ("id_recent_date")
        elem.clear()
        elem.send_keys ('2020-07-12')
        time.sleep (3)
        driver.find_element_by_xpath ("html/body/div/div/div/form/button").click ()
        time.sleep (3)

        # test delete investment
        driver.get("http://127.0.0.1:8000/investment_list")
        driver.find_element_by_xpath ("/html/body/div/div/div/div[2]/table/tbody/tr[10]/td[9]/a").click ()
        time.sleep (6)
        driver.switch_to.alert.accept ()


    def tearDown(self):
        self.driver.close ()
