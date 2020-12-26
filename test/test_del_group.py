from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.open_create_form()
        app.group.fill_form(Group(group_name="tttttt", group_header="ttttt", group_footer="tttt"))
        app.group.submit_create()
    app.group.delete_first_group()
