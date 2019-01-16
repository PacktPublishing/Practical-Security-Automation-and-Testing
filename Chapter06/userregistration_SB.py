# -*- coding: utf-8 -*-
from seleniumbase import BaseCase
class UserRegistration(BaseCase):

    def test_user_registration(self):
        self.open('http://hackazon.webscantest.com/')
        self.click("link=Sign In / Sign Up")
        self.click('#username')
        self.click("link=New user?")
        self.click('#first_name')
        self.update_text('#first_name', 'myFirstName')
        self.update_text('#last_name', 'myLastName')
        self.update_text('#username', 'myUserName1')
        self.update_text('#email', 'abc@a.com')
        self.update_text('#password', 'pass1234')
        self.update_text('#password_confirmation', 'pass1234')
        self.click("//input[@value='Register']")
   
