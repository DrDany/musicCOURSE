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
        self.change_field_value(field_name="group_name", text=group.group_name)
        self.change_field_value(field_name="group_header", text=group.group_header)
        self.change_field_value(field_name="group_footer", text=group.group_footer)


    def change_field_value(self, field_name, text):
        wd = self.app.wb
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def submit_create(self):
        wd = self.app.wb
        wd.find_element_by_name("submit").click()

    def submit_edit(self):
        wd = self.app.wb
        wd.find_element_by_name("update").click()

    def modify_first_group(self, new_group_data):
        wd = self.app.wb
        self.app.open_group_page()
        self.select_first_group()
        # open group
        wd.find_element_by_name("edit").click()
        self.fill_form(new_group_data)
        self.submit_edit()

    def delete_first_group(self):
        wd = self.app.wb
        self.app.open_group_page()
        self.select_first_group()
        wd.find_element_by_name("delete").click()

    def select_first_group(self):
        wd = self.app.wb
        wd.find_element_by_name("selected[]").click()
