
class SessionHelper:

    def __init__(self, app):
        self.app = app

    def logout(self):
        wd = self.app.wb
        wd.find_element_by_link_text("Logout").click()

    def login(self, username, password):
        self.app.open_group_page()
        wd = self.app.wb
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()