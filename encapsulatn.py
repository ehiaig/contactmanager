import hashlib
"""
Encapsulation: is restricting how fields are accessed and modified outside a class

Example below:
- Create a method that lets you change the current password
- hash the password when a secret is created.
"""

class Secret:

    def __init__(self, secret, password):
        self.__secret = secret
        self.__password = password

    def get_secret(self, passwrd):
        if passwrd == self.__password:
            hash_passwrd = hashlib.md5(passwrd.encode()).hexdigest() #This hashs the password
            print(hash_passwrd)
            return self.__secret


    def change_passwrd(self):
        print("===You want to change your password?")
        np = input('Supply old password:')
        if self.__password == np:
            new_password = input("Enter new password:")
            self.__password = new_password
            print('Your new password is {}'.format(self.__password))
        else:
            return ('Invalid password. Please enter your old password')

andrew_secret = Secret('I am beautiful', 'thetruth')
andrew_secret.get_secret('thetruth')
# andrew_secret.change_passwrd()


