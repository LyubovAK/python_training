from model.group import Group

def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test1", header="test11", footer="test111"))
    app.group.edit_first_group(Group(name="group2", header="group22", footer="group222"))
