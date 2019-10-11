import unittest, time, sys

sys.path.append("..")
from util.publicmethod import PublicMethod
from util.read_conf import ReadConfig
from pages import nbai_page
from util.config import env_info


class nbaitest(unittest.TestCase):

    def setUp(self):
        # 实例化util下PublicMethod类
        self.driver = PublicMethod(env_info['browser'])
        self.driver.wd.implicitly_wait(30)
        self.driver.max_window()

    def test_01_click_login_button(self):
