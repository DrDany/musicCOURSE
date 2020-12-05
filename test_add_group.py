# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from group import Group

class AddGroupTest(unittest.TestCase):
    def setUp(self):
        self.wb = webdriver.Firefox()
        self.wb.implicitly_wait(30)
    
    def test_add_group(self):
        wd = self.wb
        self.open_page(wd)
        self.login(wd, username="admin", password="secret")
        self.add_group(wd, Group(group_name="999", group_header="333", group_footer="333"))
        self.open_page(wd)
        self.check_added_group(wd, Group(group_name="999", group_header="333", group_footer="333"))
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def check_added_group(self, wd, group):
        wd.find_element_by_xpath("//input[@title='Select ({})']".format(group.group_name))

    def add_group(self, wd, group):
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

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_page(self, wd):
        wd.get("http://localhost/addressbook/group.php")

    def is_element_present(self, how, what):
        try: self.wb.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wb.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def tearDown(self):
        self.wb.quit()

if __name__ == "__main__":
    unittest.main()
