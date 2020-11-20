from model.group import Group
import allure


def test_group_list(app, db):
    with allure.step("Given a group list from ui"):
        ui_list = app.group.get_group_list()
    with allure.step("Given a group list from db"):
        def clean(group):
            return Group(id=group.id, name=group.name.strip())
        db_list = map(clean, db.get_group_list())
    with allure.step("Then the group list from ui is equal to the group list from db"):
        assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)
