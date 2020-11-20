from model.group import Group
import random
import allure


def test_edit_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test1", header="test11", footer="test111"))
    with allure.step("Given a non-empty group list"):
        old_groups = db.get_group_list()
    with allure.step("Given a random group from the list"):
        edit_group = random.choice(old_groups)
    with allure.step("Given a new data for edited group"):
        group = Group(name="group2", header="group22", footer="group222")
        group.id = edit_group.id
    with allure.step("When I edit the group %s from list" % group):
        app.group.edit_group_by_id(edit_group.id, group)
    with allure.step("Then the new group list is equal to the old with the edit group"):
        new_groups = db.get_group_list()
        assert len(old_groups) == len(new_groups)
        old_groups.remove(edit_group)
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)