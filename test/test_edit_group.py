import time

from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.open_edit_form_for_first()
    app.group.fill_form(Group(group_name="test_edit", group_header="tst_edit", group_footer="test_edit"))
    app.group.submit_edit()
    time.sleep(5)
    # app.group.check_added(Group(group_name="test_edit", group_header="tst_edit", group_footer="test_edit"))
    app.session.logout()
