from selenium import webdriver
import unittest
import platform


class MainCase(unittest.TestCase):
    # 声明一个webdriver
    # driver = webdriver.Chrome()

    def setUp(self):
        # 测试前，启动浏览器，打开一个设定好的网址
        self.url = "https://nbai.io"
        # 用隐身窗口
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        current_sys = platform.system()
        # self.driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe", options=chrome_options)

        self.driver = webdriver.Chrome()

        # 非隐身窗口
        # self.driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
        self.driver.get("https://nbai.io")
        # 最大化窗口
        self.driver.maximize_window()
        # # 传入webdriver，实例化这个类
        # self.base_operate = BaseOperate(self.driver)

    def tearDown(self):
        """
        测试完毕，关闭浏览器, close tab
        self.driver.close()
        :return: 
        """


if __name__ == '__main__':
    unittest.main()
