from model.group import Group
import random


def test_edit_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test1", header="test11", footer="test111"))
    old_groups = db.get_group_list()
    edit_group = random.choice(old_groups)
    group = Group(name="group2", header="group22", footer="group222")
    group.id = edit_group.id
    app.group.edit_group_by_id(edit_group.id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups.remove(edit_group)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)