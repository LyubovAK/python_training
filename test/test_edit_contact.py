from model.contact import Contact


def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test1", lastname="test2", address="test3", phone="test4", email="test5"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(firstname="Jack", lastname="London", address="USA", phone="+19870002525", email="london@gmail.com"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)