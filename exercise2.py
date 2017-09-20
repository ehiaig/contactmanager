"""
-Create a ContactManager that manages a list of Contacts.
- Create a loop that prompts to either add a contact, delete a contact or search for contact by name.
- Commit Early + Often; push your code to Github.

- what do you want to do?
    - Press 1 to add name
    - Press 2 to delete
    - Press 3 to search
- If user press 1, bring up the delete function
"""
import csv
import os.path

class ContactBox:
    def __init__(self, contacts=[]):
        self.contacts = contacts

    def read_contact(self):
        with open('contacts.csv', 'r') as file:
            for con in file:
                print(con) #This reads from the file

    def create_csv(self, contact):
        file_exist = os.path.isfile('contacts.csv')
        with open('contacts.csv', 'a') as my_file:
            fieldnames = ['name', 'phone', 'email', 'address', 'gender']
            writer = csv.DictWriter(my_file, fieldnames=fieldnames)

            if not file_exist:
                writer.writeheader()
            writer.writerow({'name':contact.name, 'phone':contact.phone, 'email':contact.email, 'address':contact.postal_address, 'gender':contact.gender})

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact has been successfully added")

    def remove_contact(self, name=''):
        name = input('Enter name to remove: ')
        for con in self.contacts:
            if con.name == name:
                self.contacts.remove(con)
                return print("Contact successfully deleted")
            else:
                return print("Contact not found")

    def search_contact(self, name=''):
        name = input('Enter name to search: ')
        for con in self.contacts:
            if con.name == name:
                print(con.name, con.phone)
            else:
                print("Sorry {} is not found in contacts".format(name))

    def show_contact(self):
        for show in self.contacts:
            print(show.name)

class Contact:
    def __init__(self, name='', phone='', gender='', email='', postal_address=''):
        self.name = input("Enter name: ")
        self.phone = input("Enter Phone: ")
        self.gender = input("Enter Gender: ")
        self.email = input("Enter Email: ")
        self.postal_address = input("Enter Postal Address: ")

def logic():
    while True:
        new_contact = ContactBox()
        option = int(input('Enter 1 to add, 2 to delete and 3 to search and 4 to show contacts: '))

        if option == 1:
            contact = Contact()
            new_contact.add_contact(contact)
            new_contact.create_csv(contact)
        elif option == 2:
            new_contact.remove_contact()
        elif option == 3:
            new_contact.search_contact()
        elif option == 4:
            new_contact.show_contact()
            new_contact.read_contact()

logic()