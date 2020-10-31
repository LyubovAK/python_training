from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("email", contact.email)

    def open_home_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("addressbook/"):
            wd.find_element_by_link_text("home").click()

    def create(self,contact):
        wd = self.app.wd
        self.open_home_page()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_name("submit").click()
        self.return_to_main_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        # select first contact
        wd.find_elements_by_name("selected[]")[index].click()
        #submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_to_main_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        # select first contact
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
        #submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_to_main_page()
        self.contact_cache = None

    def edit_first_contact(self):
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_home_page()
        # open for editing
        self.open_contact_to_edit_by_index(index)
        # edit contact
        self.fill_contact_form(contact)
        # submit update
        wd.find_element_by_name("update").click()
        self.return_to_main_page()
        self.contact_cache = None

    def edit_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.open_home_page()
        # open for editing
        self.open_contact_to_edit_by_id(id)
        # edit contact
        self.fill_contact_form(contact)
        # submit update
        wd.find_element_by_name("update").click()
        self.return_to_main_page()
        self.contact_cache = None

    def return_to_main_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                lastname = element.find_element_by_xpath(".//td[2]").text
                firstname = element.find_element_by_xpath(".//td[3]").text
                address = element.find_element_by_xpath(".//td[4]").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_phones = element.find_element_by_xpath(".//td[6]").text
                all_emails = element.find_element_by_xpath(".//td[5]").text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, address=address,
                                                  id=id, all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self,index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def open_contact_to_edit_by_id(self,id):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_xpath("//a[@href='edit.php?id=%s']" % id).click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_xpath("//img[@alt='Details']")[index].click()

    def get_contact_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").text
        id = wd.find_element_by_name("id").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, address=address, id=id,
                       email=email, email2=email2, email3=email3,homephone=homephone,
                       workphone=workphone, mobilephone=mobilephone, secondaryphone=secondaryphone)

    def add_contact_to_group(self, contact_id, group_id):
        wd = self.app.wd
        self.open_home_page()
        self.visible_all_contact()
        wd.find_element_by_css_selector("input[value='%s']" % contact_id).click()
        self.choice_group(group_id)
        self.return_to_main_page()
        self.visible_all_contact()

    def visible_all_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("group")
        if not wd.find_element_by_xpath("//option[@value='']"):
            wd.find_element_by_xpath("//option[@value='']").click()

    def choice_group(self, group_id):
        wd = self.app.wd
        wd.find_element_by_name("to_group").click()
        wd.find_element_by_xpath("(//option[@value='%s'])[2]" % group_id).click()
        wd.find_element_by_name("add").click()

    def remove_contact_from_group(self, contact_id, group_id):
        wd = self.app.wd
        self.open_home_page()
        self.open_group_page(group_id)
        wd.find_element_by_css_selector("input[value='%s']" % contact_id).click()
        wd.find_element_by_name("remove").click()
        self.return_to_main_page()
        self.visible_all_contact()

    def open_group_page(self, group_id):
        wd = self.app.wd
        wd.find_element_by_name("group")
        wd.find_element_by_xpath("//option[@value='%s']" % group_id).click()


