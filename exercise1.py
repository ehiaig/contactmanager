class Contact:
    def __init__(self, name, phone, gender, email, postal_address):
        self.name = name
        self.phone = phone
        self.gender = gender
        self.email = email
        self.postal_address = postal_address

    def new_contact(self):
        print('Name is: "{}"  Phone Number is: "{}" Gender is: "{}" Email is: "{}" Address is:"{}"'.format(self.name, self.phone, self.gender, self.email, self.postal_address))

name = input("Enter name: ")
phone = input("Enter Phone: ")
gender = input("Enter Gender: ")
email = input("Enter Email: ")
postal_address = input("Enter Postal Address: ")
my_contact = Contact(name, phone, gender, email, postal_address)
my_contact.new_contact()

