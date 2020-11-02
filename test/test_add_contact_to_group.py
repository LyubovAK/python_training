from model.contact import Contact
from model.group import Group
import random


def test_add_contact(app, db, orm):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test1", lastname="test2", address="test3", homephone="test4", email="test5"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test1", header="test11", footer="test111"))
    groups = db.get_group_list()
    for group in groups:
        list_group = orm.get_contacts_not_in_group(Group(id=group.id))
        if len(list_group) > 0: # если есть контакты, не состоящие в группе, выбираем любой и добавляем его в группу
            contact = random.choice(list_group)
            app.contact.add_contact_to_group(contact.id, group.id)
            break
        elif len(list_group) == 0:
            if group != groups[-1]: # если элемент не последний в списке, то берем следующую группу
                continue
            else: # если это была последняя группа, то создаем новую и добавляем в нее любой существующий контакт
                app.group.create(Group(name="test_name", header="test_header", footer="test_footer"))
                groups = sorted(db.get_group_list(), key=Group.id_or_max)
                group = groups[-1]
                contact = random.choice(db.get_contact_list())
                app.contact.add_contact_to_group(contact.id, group.id)
    list_in_group = orm.get_contacts_in_group(Group(id=group.id))
    assert contact in list_in_group

