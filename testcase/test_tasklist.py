from pages.nbai_page import TestNbaiPage
from maincase.main_case import MainCase
from testcase.test_login import TestLogin
from time import sleep

class TestTasklist(MainCase):

    def test_tasklist(self):
        TestLogin.test_Login(self)
        page = TestNbaiPage(self.driver)
        page.tasklist.click()
        sleep(5)
        result = "history" in self.driver.current_url
        # print(result)
        self.assertEqual(result, True)