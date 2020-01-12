# "f:/Дима/tmp/chromedriver.exe"
import pytest
from create_sale_class import Sale
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_check_menu_items(app):
    app.check_menu_items()

def test_crate_sale(app):
    app.create_sale(Sale(name='test name', email='testemail@gmail.com',order_ref='or_001', mobile='11111111111'))
    # Тут объект класса передается в качестве одного параметра
    # Но в конструкторе определяется множество параметров этого класс


