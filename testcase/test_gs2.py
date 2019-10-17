import unittest
from selenium import webdriver
from pages.nbai_page import TestNbaiPage
from maincase.main_case import MainCase
from testcase.test_login import TestLogin
from time import sleep

class TestGs2(MainCase):

    def test_gs2(self):
        url = "https://nbai.io"
        TestLogin.test_Login(self,url)
        page = TestNbaiPage(self.driver)
        # page.get(self.url)
        # page.login_item.click()
        # page.username = "guoecho@hotmail.com"
        # page.password = "nbai123"
        # page.login_btn.click()
        page.gs2.click()
        page.gs2_refresh.click()
        sleep(5)
        page.gs2_prompt.click()
        sleep(8)
        page.gs2_prompt_dismiss.click()

