import unittest
from selenium import webdriver
from pages.nbai_page import TestNbaiPage
from maincase.main_case import MainCase
from testcase.test_login import TestLogin
from time import sleep
import re

class TestCns(MainCase):
    # def setUp(self):
    #     self.driver = webdriver.Chrome()
    #     self.url = "https://nbai.io"
    #
    # def tearDown(self):
    #     self.driver.quit()

    def test_cns(self):
        TestLogin.test_Login(self)
        page = TestNbaiPage(self.driver)
        # page.get(url)
        # page.login_item.click()
        # page.username = "guoecho@hotmail.com"
        # page.password = "nbai123"
        # page.login_btn.click()
        sleep(3)
        page.cns.click()
        self.assertEqual((re.search(r'container', self.driver.current_url, re.M | re.I)).group(), "container")
        print((re.search(r'container', self.driver.current_url, re.M | re.I)).group())