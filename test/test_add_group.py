# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(group_name="123", group_header="333", group_footer="333"))
    app.group.check_added(Group(group_name="999", group_header="333", group_footer="333"))
    app.session.logout()
