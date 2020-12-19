# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.open_create_form()
    app.group.fill_form(Group(group_name="123", group_header="333", group_footer="333"))
    app.group.submit_create()
    app.group.check_added(Group(group_name="999", group_header="333", group_footer="333"))
    app.session.logout()
