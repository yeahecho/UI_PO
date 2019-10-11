from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PublicMethod(object):
    """
    the web automation test framework based on selenium
    """

    def __init__(self, browser='firefox'):
        """
        Run class initialization method, the default driver is chrome
        Also you can pass the parameter to other browser
        :param browser:
        """
        if browser == 'firefox' or browser == 'ff':
            driver = webdriver.Firefox()
        elif browser == 'chrome':
            driver = webdriver.Chrome('util/chromedriver')
        elif browser == 'safari':
            driver = webdriver.Safari()
        try:
            self.driver = driver
        except Exception:
            raise NameError("Not found %s browser, you should enter 'firefox','ff','chrome','safari'." % browser)

    def get_element(self, selector):
        """
        find the element, and return the element
        usage:
        driver.get_element("id>>>username")
        """
        self._wait_element_localed(self.driver, selector)
        element = self.driver.find_element(*self._selector_to_by(selector))

        return element

    def get_elements(self, selector):
        """
        find the element, and return the element
        """
        self._wait_element_localed(self.driver, selector)
        elements = self.driver.find_elements(*self._selector_to_by(selector))

        return elements

    def open_link(self, url):
        """
        usage:
        driver.open_link("nbai.io")
        """
        self.driver.get(url)

    def max_window(self):
        """
        usage:
        driver.max_window
        :return:
        """
        self.driver.maximize_window()

    def set_window(self, wide, high):
        """
        usage:
        driver.set_window(wide, high)
        """
        self.driver.set_window_size(wide, high)

    def enter(self, selector, text):
        """
        type text into the selected element
        usage:
        driver.type("id>>>username", "test")
        """
        try:
            self._wait_element_localed(self.driver, selector)
            element = self.get_element(selector)
            element.send_keys(text)
        except:
            raise NoSuchElementException("no such element found")

    def clear(self, selector):
        """
        usage:
        driver.clear("id>>>username")
        """
        self._wait_element_localed(self.driver, selector)
        element = self.get_element(selector)
        element.clear()

    def clear_enter(self, selector, text):
        """
        clear text and enter new text into element
        usage:
        driver.clear_enter("id>>>username", "test")
        """
        self._wait_element_localed(self.driver, selector)
        element = self.get_element(selector)
        element.clear()
        element.click()
        element.send_keys(text)

    def click(self, selector):
        """
        click the ang element can be clicked, like: text, image, check box, button, radio button...
        usage:
        driver.click("id>>>username")
        """
        self._wait_element_localed(self.driver, selector)
        element = self.get_element(selector)
        element.click()

    def right_click(self, selector):
        """
        usage:
        driver.right_click("id>>>username")
        """
        self._wait_element_localed(self.driver, selector)
        element = self.get_element(selector)
        ActionChains(self.driver).context_click(element).perform()

    def double_click(self, selector):
        """
        userage:
        driver.double_click("id>>>username")
        """
        self._wait_element_localed(self.driver, selector)
        element = self.get_element(selector)
        ActionChains(self.driver).double_click(element)

    def click_text(self, text):
        """
        usage:
        driver.click_text("test")
        """
        self.driver.find_element_by_partial_link_text(text)

    def drag_and_drop(self, source_selector, target_selector):
        """
        Drags the source_selector element a certain distance and then drop it
        """
        self._wait_element_localed(self.driver, source_selector)
        source = self.get_element(source_selector)
        self._wait_element_localed(self.driver, target_selector)
        target = self.get_element(target_selector)
        ActionChains(self.driver).drag_and_drop(source, target)

    def close(self):
        """
        usage:
        driver.close()
        """
        self.driver.close()

    def quit(self):
        """
        quit the driver and close all the windows
        usage:
        driver.quit()
        """
        self.driver.quit()

    def submit(self, selector):
        """
        usage:
        driver.submit("class>>>submit")
        :param selector:
        :return:
        """
        self._wait_element_localed(self.driver, selector)
        element = self.get_element(selector)
        element.submit()

    def f5(self):
        """
        usage:
        driver.F5()
        """
        self.driver.refresh()

    def execute_js(self, script):
        """
        Execute JavaScript script in the current window/frame
        """
        self.driver.execute_script(script)

    def get_attribute(self, selector, attribute):
        """
        get the value of an element attribute
        usage:
        driver.get_attribute("id>>>username", "class")
        """
        self._wait_element_localed(self.driver, selector)
        element = self.get_element(selector)
        attr = element.get_attribute(attribute)

        return attr

    def get_text(self, selector):
        """
        get the text information of the element
        usage:
        driver.get_text("id>>>username")
        """
        self._wait_element_localed(self.driver, selector)
        element = self.get_element(selector)
        text = element.text

        return text

    def get_title(self):
        """
        get current window title
        usage:
        driver.get_title()
        """
        title = self.driver.title
        return title

    def get_url(self):
        """
        get the url address of the current page
        usage:
        driver.get_url()
        """
        url = self.driver.current_url
        return url

    def is_element_display(self, selector):
        """
        check the element whether the element is visible to a user.
        usage:
        driver.is_element_display("id>>>username")
        """
        return True if self.get_element(selector).is_displayed() else False

    def wait(self, seconds):
        """
        Implicitly wait. All elements on the page.
        usage:
        driver.wait(10)
        """
        self.driver.implicitly_wait(seconds)

    def accept_alert(self):
        """
        Accept warning box
        usage:
        driver.accpet_alert()
        """
        self.driver.switch_to.alert().accept()

    def dismiss_alert(self):
        """
        Dismiss the alert
        usage:
        driver.dismiss_alert()
        """
        self.driver.switch_to.alert().dismiss()

    def switch_to_frame(self, selector):
        """
        switch to the specified frame
        usage:
        driver.switch_to_frame("id>>>username")
        """
        self._wait_element_localed(self.driver, selector)
        iframe_element = self.get_element(selector)
        self.driver.switch_to.frame(iframe_element)

    def switch_to_frame_out(self):
        """
        Returns the current form machine form at the next higher level.
        Corresponding relationship with switch_to_frame () method.
        usage:
        driver.switch_to.frame.out()
        """
        self.driver.switch_to.default_content()

    def open_new_window(self, selector):
        """
        open the new window and switch to the newly opened windows
        usage:
        driver.open_new_window("id>>>username")
        """
        current_window = self.driver.current_window_handle
        element = self.get_element(selector)
        element.click()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != current_window:
                self.driver.switch_to.window(handle)

    def open_new_tab_for_Windows(self, url):
        """
        For Windows system method, open a new tab to open new url and switch to the newly tab.
        usage:
        driver.open_new_tab_for_Windows("https://google.ca/")
        """
        ActionChains(self.driver).send_keys(Keys.CONTROL + 't').perform()
        self.driver.get(url)

    def open_new_table_for_Mac(self, url):
        """
        For MacOS method , open a new tab to open new url and switch to the newly tab.
        usage:
        driver.open_new_tab_for_Mac("https://www.google.ca/")
        """
        ActionChains(self.driver).send_keys(Keys.COMMAND + 't').perform()
        self.driver.get(url)

    def take_screenshot(self, filepath):
        """
        Get the current window screenshot.
        usage:
        driver.take_screenshot('../test.png')
        """
        self.driver.get_screenshot_as_file(filepath)

    @property
    def wd(self):
        """
        Return the original driver, Can use webdriver API.
        usage:
        driver.wd
        :return:
        """
        return self.driver

    def _selector_to_by(selector):
        """
        change the selector to ('by', 'value')mode
        :param selector: "id>>>username"
        :return: ('by','value')
        """
        if ">>>" not in selector:
            return NameError("selector syntax errors, lack of '>>>'")

        by = selector.split('>>>')[0]
        value = selector.split('>>>')[1]

        if by == "id":
            by = By.ID
        elif by == "name":
            by = By.NAME
        elif by == "link_text":
            by = By.LINK_TEXT
        elif by == "css" or by == "css_selector":
            by = By.CSS_SELECTOR
        elif by == "xpath":
            by = By.XPATH
        elif by == "tag" or by == "tag_name":
            by = By.TAG_NAME
        elif by == "class" or by == "class_name":
            by = By.CLASS_NAME
        elif by == "text" or by == "partial_link_text":
            by = By.PARTIAL_LINK_TEXT
        else:
            raise NameError(
                "please enter correct element attribute, 'id','name','xpath','css','tag','class','text','link_text'.")

        return by, value

    def _wait_element_localed(driver, selector, time_out=5, interval=0.2):
        """
        wait for an element localed on DOM
        """
        WebDriverWait(driver, time_out, interval).until(
            EC.presence_of_element_located(driver._selector_to_by(selector))
        )


if __name__ == "__main__":
    driver = PublicMethod('chrome')
