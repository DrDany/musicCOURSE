# -*- coding: utf-8 -*-
import os
import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.open_contact_page()
    app.add_contact(Contact(firstname="firstname", middle_name="Middle_name", last_name="Last name",
                                 nickname="nickname", company="company", home="home", mobile_phone="321",
                                 work="work",
                                 fax="fax", homepage="homepage", bday="4", bmonth="January", byear="1990",
                                 title="title", adr="adr", email1="email1@ads.com", email2="email2@ads.com", email3="email3@ads.com",
                                 aday="5", amonth="January", ayear="1990", adr2="123", phone2="123", note="note", photo=os.getcwd()+"/photo.jpeg"))
    app.submit_contact()
    app.go_to_home_page()
    app.check_added_contact()
    app.session.logout()


