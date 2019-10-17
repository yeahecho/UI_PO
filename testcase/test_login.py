import unittest
from selenium import webdriver
from pages.nbai_page import TestNbaiPage
from maincase.main_case import MainCase
from poium import Page, PageElement, PageElements
import re
from time import sleep

class TestLogin(MainCase):

    def test_Login(self):
        url = "https://nbai.io"
        page = TestNbaiPage(self.driver)
        page.get(url)
        page.login_item.click()
        page.username = "guoecho@hotmail.com"
        page.password = "nbai123"
        page.login_btn.click()
        print(self.driver.current_url)
        #通过url中的关键字判断
        self.assertEqual((re.search(r'profile', self.driver.current_url, re.M|re.I)).group(), "profile")
        # print((re.search(r'profile', self.driver.current_url, re.M|re.I)).group())


