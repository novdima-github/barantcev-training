class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login_to_feefo(self, email, password):
        driver = self.app.driver

        driver.find_element_by_name('email').send_keys(email)
        driver.find_element_by_name('password').send_keys(password)
        driver.find_element_by_css_selector("button[type='submit']").click()

    def log_out(self):
        driver = self.app.driver
        driver.find_element_by_css_selector("div[class='header-user-dropdown-button-content-desktop']").click()
        driver.find_element_by_partial_link_text('Log Out').click()
