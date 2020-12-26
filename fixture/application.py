from selenium import webdriver

from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:

    def __init__(self):
        self.wb = webdriver.Chrome()
        self.wb.maximize_window()
        self.wb.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)


    def is_valid(self):
        try:
            print(self.wb.current_url)
            return True
        except:
            return False


    def open_group_page(self):
        wd = self.wb
        wd.get("http://localhost/addressbook/group.php")

    def open_contact_page(self):
        wd = self.wb
        wd.get("http://localhost/addressbook/edit.php")

    def open_home_page(self):
        wd = self.wb
        wd.get("http://localhost/addressbook/index.php")

    def go_to_home_page(self):
        # go home page
        wd = self.wb
        wd.find_element_by_link_text("home").click()

    def destroy(self):
        self.wb.quit()
