import unittest
from selenium import webdriver
from pages.nbai_page import TestNbaiPage
from poium import Page, PageElement, PageElements



class TestNbai(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        self.driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe", options= chrome_options)
        self.base_url = "https://nbai.io"

    def tearDown(self):
        self.driver.quit()

    def test_click_login_item(self):
        page = TestNbaiPage(self.driver)
        page.get(self.base_url)

if __name__ == '__main__':
    unittest.main()

