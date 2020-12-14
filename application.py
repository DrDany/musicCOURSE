from selenium import webdriver

class Application:

    def __init__(self):
        self.wb = webdriver.Firefox()
        self.wb.implicitly_wait(30)

    def logout(self):
        wd = self.wb
        wd.find_element_by_link_text("Logout").click()

    def check_added_group(self, group):
        wd = self.wb
        self.open_page()
        wd.find_element_by_xpath("//input[@title='Select ({})']".format(group.group_name))

    def add_group(self, group):
        wd = self.wb
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

    def login(self, username, password):
        self.open_page()
        wd = self.wb
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_page(self):
        wd = self.wb
        wd.get("http://localhost/addressbook/group.php")

    def destroy(self):
        self.wb.quit()
