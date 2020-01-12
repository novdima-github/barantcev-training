from selenium import webdriver

class Application:

    def __init__(self):
        self.driver = webdriver.Chrome('f:/Дима/tmp/chromedriver.exe')
        # Optional argument, if not specified will search path.
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.visit_login_page()

    def visit_login_page(self):
        driver = self.driver
        driver.get('https://hub.feefo.com/login')

    def login_to_feefo(self, email, password):
        driver = self.driver
        driver.find_element_by_name('email').send_keys(email)
        driver.find_element_by_name('password').send_keys(password)
        driver.find_element_by_css_selector("button[type='submit']").click()

    def check_menu_items(self):
        driver = self.driver
        driver.find_element_by_partial_link_text('Dashboard').click()
        driver.find_element_by_partial_link_text('Feedback').click()
        driver.find_element_by_partial_link_text('Sales').click()

    def create_sale(self, sale):
        driver = self.driver
        driver.find_element_by_partial_link_text('Sales').click()
        driver.find_element_by_partial_link_text('Submit Individual Sale').click()
        driver.find_element_by_name('consumerName').send_keys(sale.name)
        driver.find_element_by_name('consumerEmail').send_keys(sale.email)
        driver.find_element_by_name('mobileNumber').send_keys(sale.mobile)
        driver.find_element_by_name('orderRef').send_keys(sale.order_ref)

    def log_out(self):
        driver = self.driver
        driver.find_element_by_css_selector("div[class='header-user-dropdown-button-content-desktop']").click()
        driver.find_element_by_partial_link_text('Log Out').click()

    def destroy(self):
        self.driver.quit()