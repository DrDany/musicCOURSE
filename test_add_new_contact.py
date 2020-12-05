# -*- coding: utf-8 -*-
import os
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from contact import Contact

class TestAddNewContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_new_contact(self):
        wd = self.wd
        # open home page
        wd.get("http://localhost/addressbook/index.php")
        self.login(wd, username="admin", password="secret")
        self.add_contact(wd, Contact(firstname="firstname", middle_name="Middle_name", last_name="Last name",
                         nickname="nickname", company="company", home="home", mobile_phone="mobile_phone", work="work",
                         fax="fax", homepage="homepage", bday="4", bmotnh="January", byear="1990"))
        self.submit_contact(wd)
        self.go_to_home_page(wd)
        self.check_added_contact(wd)
        self.logout(wd)

    def logout(self, wd):
        # logout
        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")

    def check_added_contact(self, wd):
        # check added contact
        wd.find_element_by_xpath("//td[contains(text(), 'firstname')]")

    def go_to_home_page(self, wd):
        # go home page
        wd.find_element_by_link_text("home").click()

    def submit_contact(self, wd):
        # submit add contact
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        wd.find_element_by_xpath("//div[contains(text(), 'Information entered into address book.')]")

    def add_contact(self, wd, contact):
        # open add contact page
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middle_name)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("photo").send_keys(os.getcwd() + "/photo.jpeg")
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("title")
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("address")
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile_phone)
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work)
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("email@email.com")
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys("email2@email.com")
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys("email2@email")
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        wd.find_element_by_xpath("//option[@value='4']").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmotnh)
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.byear)
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

    def login(self, wd, username, password):
        #  login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

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
