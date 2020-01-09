# "f:/Дима/tmp/chromedriver.exe"
import unittest
import time
from selenium import webdriver
from login import GroupLogin

class testClass(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('f:/Дима/tmp/chromedriver.exe')  # Optional argument, if not specified will search path.
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def visit_login_page(self, driver):
        driver.get('https://hub.feefo.com/login');

    def login_to_feefo(self, driver, log):
        driver.find_element_by_name('email').send_keys(log.email)
        driver.find_element_by_name('password').send_keys(log.password)
        driver.find_element_by_css_selector("button[type='submit']").click()

    def check_menu_items(self, driver):
        driver.find_element_by_partial_link_text('Dashboard').click()
        driver.find_element_by_partial_link_text('Feedback').click()
        driver.find_element_by_partial_link_text('Sales').click()
        driver.find_element_by_css_selector("div[class='header-user-dropdown-button-content-desktop']").click()

    def log_out(self, driver):
        driver.find_element_by_partial_link_text('Log Out').click()

    def test(self):
        success = True
        driver = self.driver
        self.visit_login_page(driver)
        self.login_to_feefo(driver, GroupLogin('testmailnd@gmail.com', 'Dima!qa2ws1'))
        self.check_menu_items(driver)
        time.sleep(1)  # Let the user actually see something!
        self.log_out(driver)
        self.assertTrue(success)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


