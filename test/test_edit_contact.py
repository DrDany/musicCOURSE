import time

from model.contact import Contact


def test_edit_contact(app):
    app.open_home_page()
    app.contact.open_edit_form()
    app.contact.fill_form(Contact(firstname="test_edit", middle_name="name", last_name="name",
                               nickname="nickname", company="company", home="home", mobile_phone="321",
                               work="work",
                               fax="fax", homepage="homepage", bday="4", bmonth="January", byear="1990",
                               title="title", adr="adr", email1="email1@ads.com", email2="email2@ads.com",
                               email3="email3@ads.com",
                               aday="5", amonth="January", ayear="1990", adr2="123", phone2="123", note="note",
                               photo=None))
    app.contact.submit_edit()
    time.sleep(3)
