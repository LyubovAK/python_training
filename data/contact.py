from model.contact import Contact
import random
import string


constant = [
    Contact(firstname="Firstname1", lastname="Lastname2", address="Address1", homephone="123", email="123@mail.ru")
]

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", lastname="", address="", homephone="", email="")] + [
    Contact(firstname=random_string("firstname", 5), lastname=random_string("lastname", 10),
            address=random_string("address", 20), homephone=(random_string("homephone", 10)), email=(random_string("email", 7)))
    for i in range(5)
]