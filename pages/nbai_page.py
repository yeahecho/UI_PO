from poium import Page, PageElement, PageElements
from time import sleep
from selenium import webdriver
import unittest


class TestNbaiPage(Page):
    # define all elements on the page
    login_item = PageElement(id_="loginUserLog", describe="Homepage login item")  # 通过id定位login按钮
    username = PageElement(id_="username", describe="username")
    password = PageElement(id_="password", describe="password")
    login_btn = PageElement(id_="kc-login", describe="submit button")
    side_bar_btn = PageElement(xpath='//*[@id="m_aside_left_minimize_toggle"]', describe="sidebar button")
    dashboard = PageElement(xpath='//*[@id="m_ver_menu"]/ul/li[1]/a', describe="dashboard item")
    notebook = PageElement(xpath='//*[@id="m_ver_menu"]/ul/li[2]/a', describe="notebook")
    gs2 = PageElement(xpath='//*[@id="m_ver_menu"]/ul/li[3]/a', describe="GS2")
    gs2_refresh = PageElement(css="div.modal-header>i")
    gs2_prompt = PageElement(class_name="close", describe="关闭gs2弹出框")
    gs2_prompt_dismiss = PageElement(
        xpath='/html/body/ngb-modal-window[2]/div/div/ngbd-modal-close-confirm/div[2]/button[1]', describe="确定关闭gs2弹出框")

    cns = PageElement(xpath='//*[@id="m_ver_menu"]/ul/li[4]/a', describe="CNS")
    mls = PageElement(xpath='//*[@id="m_ver_menu"]/ul/li[5]/a', describe="MLS")
    tasklist = PageElement(xpath='//*[@id="m_ver_menu"]/ul/li[6]/a', describe="Task List")
    myprofile = PageElement(xpath='//*[@id="m_ver_menu"]/ul/li[7]/a', describe="My Profile")
    myprofile_payment = PageElement(
        xpath='//*[@id="fb-root"]/div[2]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/ul/li[2]/a',
        describe="payment method tab")
    myprofile_bills = PageElement(
        xpath='//*[@id="fb-root"]/div[2]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/ul/li[3]/a', describe="bills")
    myprofile_security = PageElement(
        xpath='//*[@id="fb-root"]/div[2]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/ul/li[4]/a')
    myprofile_refferal = PageElement(
        xpath='//*[@id="fb-root"]/div[2]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/ul/li[5]/a')

    def test_login(self, url):
        page = TestNbaiPage(browser)
        page.get(url)
        page.login_item.click()

        page.username = "guoecho@hotmail.com"
        page.password = "nbai123"
        page.login_btn.click()

        page.side_bar_btn.click()
        sleep(1)
        page.side_bar_btn.click()

        page.dashboard.click()
        sleep(3)
        # page.notebook.click()

        page.gs2.click()
        page.gs2_refresh.click()
        page.gs2_prompt.click()
        sleep(3)
        page.gs2_prompt_dismiss.click()

        page.cns.click()

        page.mls.click()
        sleep(2)
        page.tasklist.click()
        sleep(2)
        page.myprofile.click()
        page.myprofile_payment.click()
        sleep(1)
        page.myprofile_bills.click()
        sleep(1)
        page.myprofile_security.click()
        sleep(1)
        page.myprofile_refferal.click()

        browser.quit()


if __name__ == '__main__':
    browser = webdriver.Chrome()
    TestNbaiPage.test_login(browser)
