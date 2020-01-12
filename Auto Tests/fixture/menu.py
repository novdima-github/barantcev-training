class MenuHelper:
    def __init__(self, app):
        self.app = app

    def check_menu_items(self):
        driver = self.app.driver
        driver.find_element_by_partial_link_text('Dashboard').click()
        driver.find_element_by_partial_link_text('Feedback').click()
        driver.find_element_by_partial_link_text('Sales').click()
