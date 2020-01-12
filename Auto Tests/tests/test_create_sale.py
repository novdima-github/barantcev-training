import pytest
from model.create_sale_class import Sale
from fixture.application import Application

@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_check_menu_items(app):
    app.login_to_feefo('testmailnd@gmail.com', 'Dima!qa2ws1')
    app.check_menu_items()
    app.log_out()

def test_crate_sale(app):
    app.login_to_feefo('testmailnd@gmail.com', 'Dima!qa2ws1')
    app.create_sale(Sale(name='test name', email='testemail@gmail.com',order_ref='or_001', mobile='11111111111'))
    # Тут объект класса передается в качестве одного параметра
    # Но в конструкторе определяется множество параметров этого класс
    app.log_out()

