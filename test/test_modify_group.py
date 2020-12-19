import time

from model.group import Group


def test_modify_name_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(group_name="test_name"))
    app.session.logout()


def test_modify_header_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(group_header="test_header"))
    app.session.logout()
