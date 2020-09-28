from model.contact import Contact


def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="Jack", lastname="London", address="USA", phone="+19870002525", email="london@gmail.com"))
    app.session.logout()