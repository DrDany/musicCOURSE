# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.open_create_form()
    app.group.fill_form(Group(group_name="tttttt", group_header="ttttt", group_footer="tttt"))
    app.group.submit_create()
    app.group.check_added(Group(group_name="tttttt", group_header="ttttt", group_footer="tttt"))

