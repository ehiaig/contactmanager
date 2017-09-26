class ElectricSocket:
    pass
class USSocket(ElectricSocket):
    pass

class UKSocket(ElectricSocket):
    pass

andrew = USSocket()
edem = UKSocket()

print(isinstance(andrew, ElectricSocket)) #isinstance checks if the object 'andrew' is an instance of the class ElectricSocket
print(isinstance(edem, ElectricSocket))

class Cat:
    pass
class Person:
    def __init__(self, complaint='No internet'):
        self.complaint = complaint

    def complain(self):
        print(self.complaint)

class Eits(Person):
    pass
class Fellow(Person):
    pass
people = list() #is same as people = []
for _ in range(7): #The _ implies that we don't care about the values the range prints out
    people.append(Fellow())

for _ in range(58):
    people.append(Eits())
people.append(Cat())

for person in people:
    if isinstance(person, Person) is True: #This line checks if the person is an instance of the class Person
        person.complain()