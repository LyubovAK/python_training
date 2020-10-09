class Contact:
    def __init__(self, firstname=None, lastname=None, address=None, phone=None, email=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.phone = phone
        self.email = email
        self.id = id

    def __repr__(self):
        return "%s:%s %s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return self.id == other.id and self.lastname == other.lastname and self.firstname == other.firstname