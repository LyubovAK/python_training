from model.contact import Contact
from model.group import Group
import random


def test_add_contact(app, db, orm):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test1", lastname="test2", address="test3", homephone="test4", email="test5"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test1", header="test11", footer="test111"))
    contacts = db.get_contact_list()
    contact = random.choice(contacts)
    groups = db.get_group_list()
    group = random.choice(groups)
    list1 = orm.get_contacts_not_in_group(Group(id=group.id))
    if contact in list1: #проверяем, что контакт уже не состоит в выбранной группе
        app.contact.add_contact_to_group(contact.id, group.id)
    else:
        contact = random.choice(list1) #выбираем другой контакт, который не состоит в группе. Но если все список пустой, тест упадет
        app.contact.add_contact_to_group(contact.id, group.id)
    list2 = orm.get_contacts_in_group(Group(id=group.id))
    assert contact in list2
