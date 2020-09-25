# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Lev", lastname="Tolstoy", address="Russia", phone="+79310002345", email="lev@mail.ru"))
    app.session.logout()
