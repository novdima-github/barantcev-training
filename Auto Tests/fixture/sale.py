class SaleHelper:

    def __init__(self, app):
        self.app = app

    def create_sale(self, sale):
        driver = self.app.driver
        driver.find_element_by_partial_link_text('Sales').click()
        driver.find_element_by_partial_link_text('Submit Individual Sale').click()
        driver.find_element_by_name('consumerName').send_keys(sale.name)
        driver.find_element_by_name('consumerEmail').send_keys(sale.email)
        driver.find_element_by_name('mobileNumber').send_keys(sale.mobile)
        driver.find_element_by_name('orderRef').send_keys(sale.order_ref)

    def delete_sale(self, sale):
        driver = self.app.driver
        driver.find_element_by_partial_link_text('Sales').click()
        driver.find_element_by_partial_link_text('Submit Individual Sale').click()
        driver.find_element_by_name('consumerName').send_keys(sale.name)
        driver.find_element_by_name('consumerEmail').send_keys(sale.email)
        driver.find_element_by_name('mobileNumber').send_keys(sale.mobile)
        driver.find_element_by_name('orderRef').send_keys(sale.order_ref)