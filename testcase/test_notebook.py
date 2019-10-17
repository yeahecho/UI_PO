from pages.nbai_page import TestNbaiPage
from maincase.main_case import MainCase
from testcase.test_login import TestLogin
from time import sleep
import re


class TestNotebook(MainCase):

    def test_notebook(self):
        url = "https://nbai.io"
        TestLogin.test_Login(self)
        page = TestNbaiPage(self.driver)
        # page.get(self.url)
        # page.login_item.click()
        # page.username = "guoecho@hotmail.com"
        # page.password = "nbai123"
        # page.login_btn.click()
        page.notebook.click()
        print(self.driver.current_window_handle)
        handles = self.driver.window_handles
        print(self.driver.window_handles)
        for handle in handles:
            if handle != self.driver.current_window_handle:
                print("switch to", handle)
                self.driver.switch_to_window(handle)
                break
        # self.driver.close()
        # self.driver.switch_to_window(handles[0])
        self.assertEqual((re.search(r'notebook', self.driver.current_url, re.M | re.I)).group(), "notebook")