import pytest
from model.sale_class import Sale
from fixture.application import Application

@pytest.fixture() # scope="session"
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_check_menu_items(app):
    app.session.login_to_feefo('testmailnd@gmail.com', 'Dima!qa2ws1')
    app.menu.check_menu_items()
    app.session.log_out()

def test_crate_sale(app):
    app.session.login_to_feefo('testmailnd@gmail.com', 'Dima!qa2ws1')
    app.sale.create_sale(Sale(name='test name', email='testemail@gmail.com',order_ref='or_001', mobile='11111111111'))
    # Тут объект класса передается в качестве одного параметра
    # Но в конструкторе определяется множество параметров этого класс
    app.session.log_out()

