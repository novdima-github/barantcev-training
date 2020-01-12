# "f:/Дима/tmp/chromedriver.exe"
import unittest
import time
import create_sale_class
from create_sale_class import Sale
from selenium import webdriver
from login_class import Login

class testClass(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('f:/Дима/tmp/chromedriver.exe')  # Optional argument, if not specified will search path.
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        driver = self.driver
        self.visit_login_page(driver)
        self.login_to_feefo(driver, Login('testmailnd@gmail.com', 'Dima!qa2ws1'))

    def tearDown(self):
        driver = self.driver
        self.log_out(driver)
        self.driver.quit()

    def visit_login_page(self, driver):
        driver.get('https://hub.feefo.com/login');

    def login_to_feefo(self, driver, login):
        driver.find_element_by_name('email').send_keys(login.email)
        driver.find_element_by_name('password').send_keys(login.password)
        driver.find_element_by_css_selector("button[type='submit']").click()

    def check_menu_items(self, driver):
        driver.find_element_by_partial_link_text('Dashboard').click()
        driver.find_element_by_partial_link_text('Feedback').click()
        driver.find_element_by_partial_link_text('Sales').click()

    def create_sale(self, driver, sale):
        driver.find_element_by_partial_link_text('Sales').click()
        driver.find_element_by_partial_link_text('Submit Individual Sale').click()
        driver.find_element_by_name('consumerName').send_keys(sale.name)
        driver.find_element_by_name('consumerEmail').send_keys(sale.email)
        driver.find_element_by_name('mobileNumber').send_keys(sale.mobile)
        driver.find_element_by_name('orderRef').send_keys(sale.order_ref)

    def log_out(self, driver):
        driver.find_element_by_css_selector("div[class='header-user-dropdown-button-content-desktop']").click()
        driver.find_element_by_partial_link_text('Log Out').click()


    def test_check_menu_items(self):
        success = True
        driver = self.driver
        self.check_menu_items(driver)
        time.sleep(1)  # Let the user actually see something!
        self.assertTrue(success)

    def test_crate_sale(self):
        success = True
        driver = self.driver
        self.create_sale(driver, Sale(name='test name', email='testemail@gmail.com',order_ref='or_001', mobile='11111111111'))
        # Тут объект класса передается в качестве одного параметра
        # Но в конструкторе определяется множество параметров этого класс
        time.sleep(3)  # Let the user actually see something!
        self.assertTrue(success)


if __name__ == '__main__':
    unittest.main(testClass.test_crate_sale())


