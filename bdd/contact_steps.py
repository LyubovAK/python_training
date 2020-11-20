from pytest_bdd import given, when, then
from model.contact import Contact
import random


@given('a contact list', target_fixture="contact_list")
def contact_list(db):
    return db.get_contact_list()


@given('a contact with <firstname>, <lastname>, <address>, <homephone> and <email>', target_fixture="new_contact")
def new_contact(firstname, lastname, address, homephone, email):
    return Contact(firstname=firstname, lastname=lastname, address=address, homephone=homephone, email=email)


@when('I add the contact to the list')
def add_new_contact(app, new_contact):
    app.contact.create(new_contact)


@then('the new contact list is equal to the old list with the added contact')
def verify_contact_added(app, db, check_ui, contact_list, new_contact):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


@given('a non-empty contact list', target_fixture="non_empty_contact_list")
def non_empty_contact_list(db, app):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Firstname_test", lastname="Lastname_test"))
    return db.get_contact_list()


@given('a random contact from the list', target_fixture="random_contact")
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)


@when('I delete the contact from list')
def delete_contact(app, random_contact):
    app.contact.delete_contact_by_id(random_contact.id)


@then('the new contact list is equal to the old list without the deleted contact')
def verify_contact_deleted(db, non_empty_contact_list, random_contact, app, check_ui):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(random_contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


@given('a new firstname and lastname for edited contact', target_fixture="new_contact_data")
def new_contact_data(random_contact):
    contact = Contact(firstname="Edited_firstname", lastname="Edited lastname")
    contact.id = random_contact.id
    return contact


@when('I edit the contact from list')
def edit_contact(app, new_contact_data):
    app.contact.edit_contact_by_id(new_contact_data.id, new_contact_data)


@then('the new contact list is equal to the old with the edit contact')
def verify_contact_edited(db, app, check_ui, non_empty_contact_list, random_contact, new_contact_data):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts.remove(random_contact)
    old_contacts.append(new_contact_data)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)

