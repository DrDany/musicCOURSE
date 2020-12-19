
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

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wb
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wb
        text = wd.find_element_by_xpath("//div/div[1]/form/b").text
        return text == "("+username+")"

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)
