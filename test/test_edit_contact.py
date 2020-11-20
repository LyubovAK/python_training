from model.contact import Contact
import random
import allure


def test_edit_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test1", lastname="test2", address="test3", homephone="test4", email="test5"))
    with allure.step("Given a non-empty contact list"):
        old_contacts = db.get_contact_list()
    with allure.step("Given a random contact from the list"):
        edit_contact = random.choice(old_contacts)
    with allure.step("Given a new data for edited contact"):
        contact = Contact(firstname="Jack", lastname="London", address="USA", homephone="+19870002525", email="london@gmail.com")
        contact.id = edit_contact.id
    with allure.step("When I edit the contact %s from list" % contact):
        app.contact.edit_contact_by_id(edit_contact.id, contact)
    with allure.step("Then the new contact list is equal to the old with the edit contact"):
        new_contacts = db.get_contact_list()
        assert len(old_contacts) == len(new_contacts)
        old_contacts.remove(edit_contact)
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
