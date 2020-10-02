from model.contact import Contact


def test_del_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test1", lastname="test2", address="test3", phone="test4", email="test5"))
    app.contact.delete_first_contact()
