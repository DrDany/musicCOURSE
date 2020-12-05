# -*- coding: utf-8 -*-
import os
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select


class AddNewContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_new_contact(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("firstname")
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("Middle name")
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("Last mae")
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("nick")
        wd.find_element_by_name("photo").send_keys(os.getcwd() + "/photo.jpeg")
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("title")
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("comp")
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("address")
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("tel")
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("mob")
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("work")
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys("fax")
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("email@email.com")
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys("email2@email.com")
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys("email2@email")
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("pagehome")
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("4")
        wd.find_element_by_xpath("//option[@value='4']").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("January")
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1990")
        Select(wd.find_element_by_name("aday")).select_by_visible_text("5")
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("January")
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("1990")
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys("address")
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys("home")
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys("note")
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        wd.find_element_by_xpath("//div[contains(text(), 'Information entered into address book.')]")
        wd.find_element_by_link_text("home").click()
        wd.find_element_by_xpath("//td[contains(text(), 'firstname')]")
        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
