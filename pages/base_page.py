# 定义页面基础类，用于所有页面的基础，封装所有测试页面的公共方法


class BasePage(object):
    '''
    This is a base page class for Page Object
    '''

    def __init__(self, driver):
        self.driver = driver
