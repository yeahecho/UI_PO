from pages.base_page import BasePage
from poium import Page, PageElement
from selenium import webdriver


class Nbai_Page(BasePage):
    search_element = "loginUserLog" #通过id定位login按钮

    def click_login_button(self):
        self.driver.get_element(self.search_element).click()

