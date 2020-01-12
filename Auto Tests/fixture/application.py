from selenium import webdriver
from fixture.session import SessionHelper
from fixture.menu import MenuHelper
from fixture.sale import SaleHelper
class Application:

    def __init__(self):
        self.driver = webdriver.Chrome('f:/Дима/tmp/chromedriver.exe')
        # Optional argument, if not specified will search path.
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.session = SessionHelper(self)
        self.menu = MenuHelper(self)
        self.sale = SaleHelper(self)

    def destroy(self):
        self.driver.quit()