from pages.nbai_page import TestNbaiPage
from maincase.main_case import MainCase
from testcase.test_login import TestLogin
from time import sleep
import re

class TestDashboard(MainCase):

    def test_dashboard(self):
        url = "https://nbai.io"
        TestLogin.test_Login(self)
        page = TestNbaiPage(self.driver)
        # page.side_bar_btn.click()
        # sleep(1)
        # page.side_bar_btn.click()

        page.dashboard.click()
        sleep(5)
        result = "index" in self.driver.current_url
        # print(result)
        self.assertEqual(result, True)