from model.sale_class import Sale

def test_delete_sale(app):
    app.session.login_to_feefo('testmailnd@gmail.com', 'Dima!qa2ws1')
    app.sale.delete_sale(Sale(name='delete test name', email='testemail@gmail.com',order_ref='or_001', mobile='11111111111'))
    app.session.log_out()

