import re
from model.contact import Contact
import allure


def test_contact_on_home_page(app, db):
    with allure.step("Given a sorted contact list from home page"):
        contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    with allure.step("Given a sorted contact list from home db"):
        contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    with allure.step("Then the contact list from home page is equal to the contact list from db"):
        assert len(contacts_from_home_page) == len(contacts_from_db)
        for i in range(len(contacts_from_home_page)):
            contact_from_home_page = contacts_from_home_page[i]
            contact_from_db = contacts_from_db[i]
            assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_db)
            assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_db)
            assert contact_from_home_page.firstname == contact_from_db.firstname
            assert contact_from_home_page.lastname == contact_from_db.lastname
            assert contact_from_home_page.address == contact_from_db.address



def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear (x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: (x != "") and (x is not None), [contact.email, contact.email2,contact.email3]))