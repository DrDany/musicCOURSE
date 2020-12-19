class GroupHelper:

    def __init__(self, app):
        self.app = app

    def check_added(self, group):
        wd = self.app.wb
        self.app.open_group_page()
        wd.find_element_by_xpath("//input[@title='Select ({})']".format(group.group_name))

    def open_create_form(self):
        wd = self.app.wb
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()

    def fill_form(self, group):
        wd = self.app.wb
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.group_name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.group_header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.group_footer)

    def submit_create(self):
        wd = self.app.wb
        wd.find_element_by_name("submit").click()

    def submit_edit(self):
        wd = self.app.wb
        wd.find_element_by_name("update").click()


    def delete_first_group(self):
        wd = self.app.wb
        self.app.open_group_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("delete").click()

    def open_edit_form_for_first(self):
        wd = self.app.wb
        self.app.open_group_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()