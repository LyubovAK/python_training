from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test1", header="test11", footer="test111"))
    app.group.delete_first_group()
