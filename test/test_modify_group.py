import time

from model.group import Group


def test_modify_name_group(app):
    app.group.modify_first_group(Group(group_name="test_name"))



def test_modify_header_group(app):
    app.group.modify_first_group(Group(group_header="test_header"))

