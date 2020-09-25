# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_address(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Lev", lastname="Tolstoy", address="Russia", phone="+79310002345", email="lev@mail.ru"))
    app.session.logout()
