import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit = True)

    def get_group_list(self):
        group_list = []
        with self.connection.cursor() as group_cursor:
            group_cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for group_row in group_cursor:
                (gr_id, name, header, footer) = group_row
                group_list.append(Group(id=str(gr_id), name=name, header=header, footer=footer))
        return group_list

    def get_contact_list(self):
        contact_list = []
        with self.connection.cursor() as contact_cursor:
            contact_cursor.execute("select id, firstname, lastname, address, home, mobile, work, email, email2, email3, phone2 from addressbook where deprecated='0000-00-00 00:00:00'")
            for contact_row in contact_cursor:
                (contact_id, firstname, lastname, address, home, mobile, work, email, email2, email3, phone2) = contact_row
                contact_list.append(Contact(id=str(contact_id), firstname=firstname, lastname=lastname, address=address,
                                            homephone=home, mobilephone=mobile, workphone=work, secondaryphone=phone2,
                                            email=email, email2=email2, email3=email3))
        return contact_list

    def destroy(self):
        self.connection.close()