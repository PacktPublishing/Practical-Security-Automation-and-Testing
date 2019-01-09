# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class SignIn(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
   
    def test_sign_in(self):
        driver = self.driver
        driver.get("http://nodegoat.herokuapp.com/login")
        driver.find_element_by_id("userName").clear()
        driver.find_element_by_id("userName").send_keys("user1")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("User1_123")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.get("http://nodegoat.herokuapp.com/contributions")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.get("http://nodegoat.herokuapp.com/contributions")
        driver.get("http://nodegoat.herokuapp.com/allocations/2")
        driver.get("http://nodegoat.herokuapp.com/memos")
        driver.get("http://nodegoat.herokuapp.com/profile")
    
    
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()