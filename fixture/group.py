class GroupHelper:

    def __init__(self, app):
        self.app = app

    def check_added(self, group):
        wd = self.app.wb
        self.app.open_group_page()
        wd.find_element_by_xpath("//input[@title='Select ({})']".format(group.group_name))

    def create(self, group):
        wd = self.app.wb
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.group_name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.group_header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.group_footer)
        wd.find_element_by_name("submit").click()
