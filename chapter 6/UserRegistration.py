# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UserRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_user_registration(self):
        driver = self.driver
        driver.get("http://hackazon.webscantest.com/")
        driver.find_element_by_link_text("Sign In / Sign Up").click()
        driver.find_element_by_id("username").click()
        driver.find_element_by_link_text("New user?").click()
        driver.find_element_by_id("first_name").click()
        driver.find_element_by_id("first_name").clear()
        driver.find_element_by_id("first_name").send_keys("FirstName")
        driver.find_element_by_id("last_name").clear()
        driver.find_element_by_id("last_name").send_keys("LastName")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("UserName1")
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("abc@a.com")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("pass1234")
        driver.find_element_by_id("password_confirmation").clear()
        driver.find_element_by_id("password_confirmation").send_keys("pass1234")
        driver.find_element_by_xpath("//input[@value='Register']").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
