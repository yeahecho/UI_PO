import unittest
from selenium import webdriver
from pages.nbai_page import TestNbaiPage


class TestNbai(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "https://nbai.io"

    def tearDown(self):
        self.driver.quit()

    def test_click_login_item(self):
        page = TestNbaiPage(Page)
        page.get(self.base_url)


