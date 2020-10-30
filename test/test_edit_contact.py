from model.contact import Contact
import random


def test_edit_contact(app,db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test1", lastname="test2", address="test3", homephone="test4", email="test5"))
    old_contacts = db.get_contact_list()
    edit_contact = random.choice(old_contacts)
    contact = Contact(firstname="Jack", lastname="London", address="USA", homephone="+19870002525", email="london@gmail.com")
    contact.id = edit_contact.id
    app.contact.edit_contact_by_id(edit_contact.id, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts.remove(edit_contact)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)