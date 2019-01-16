# -*- coding: utf-8 -*-
from seleniumbase import BaseCase


class SignIn(BaseCase):

    def test_sign_in(self):
        self.open('http://nodegoat.herokuapp.com/login')
        self.update_text('#userName', 'user1')
        self.update_text('#password', 'User1_123')
        self.click("//button[@type='submit']")
        self.open('http://nodegoat.herokuapp.com/contributions')
        self.click("//button[@type='submit']")
        self.open('http://nodegoat.herokuapp.com/contributions')
        self.open('http://nodegoat.herokuapp.com/allocations/2')
        self.open('http://nodegoat.herokuapp.com/memos')
        self.open('http://nodegoat.herokuapp.com/profile')
