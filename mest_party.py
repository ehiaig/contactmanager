import smtplib
dicti = {}
"""
Mest is throwing a a crazy party. They need us to write software to register guests.
A. Store guest(name, email) in a dictionary
B. Given a name, output an email
c. Send an email to all guest thanking them for showing up
D. If the guest has an odd of number of letters in their name, send them a different email telling them they are
unwelcome to future events.
"""
class MestParty:
    def __init__(self, name, email):
        # name = input('Enter your name:')
        # email = input('Enter your email:')
        self.name = name
        self.email = email

        dicti[name] = email
        print("****Guest added to the list****")
        print (dicti)

    def search_name(self, na):
        print('====== search for name =======')
        print (dicti)
        if na in dicti.keys():
            return dicti[na]
        else:
            return ("Guest not found in list")

    def send_email(self, name):
        sender = "ehiagheaigg@gmail.com"
        receiver = dicti[name]
        # receiver = ['div82340@posdz.com']
        message = """Thank you for showing up at the party today."""

        try:
            mailObj = smtplib.SMTP("smtp.gmail.com", 587)
            mailObj.starttls()
            mailObj.login('ehiagheaigg@gmail.com', 'hjjhj')
            mailObj.sendmail(sender, receiver, message)
            print("Mail sent")
        except Exception as e:
            print ("Error: unable to send email", e)

    def unwelcome(self):
        pass

def logic():
    while True:
        choice = int(input('Type 1 to add guest \n Type 2 to search name \n Enter 3 to send mail \n Enter 4 to send unwelcome mail'))
        if choice == 1:
            name = input("Enter name: ")
            email = input("Enter email: ")
            party = MestParty(name, email)
        elif choice == 2:
            name = input('Enter name:')
            print(party.search_name(name))
        elif choice == 3:
            party.send_email(name)
        elif choice == 4:
            party.unwelcome()

logic()

# party = MestParty()
# party.add_guest()
# party.send_email()
