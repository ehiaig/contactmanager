import csv
import os.path
"""
- Mest is a School that contains EITs and Fellows.
- Create classes to represent all three entities.
    - EITs have names, nationalities and the ability to recite fun facts about tech class
    - Fellows have name, nationality, happiness_level and abilities to eat (increase happiness) and teach (decreases happiness)
    - School has EITs and Fellows

class School:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

name = input("Enter name:")
nationality = input("Enter country:")

class EITs(School):
    def __init__(self, name, nationality):
        School.__init__(self, name, nationality)

    def fun_facts(self):
        print("My fun fact")


class Fellows(School):
    def __init__(self, name, nationality, happiness_level, teach):
        School.__init__(self, name, nationality)
        self.happiness_level = happiness_level
        self.teach = teach

    def tell(self):
        print(self.name)

happiness_level = input("Enter happiness levee:")
teach = input("Do you teach?")
fe = Fellows(name, nationality, happiness_level, teach)
fe.tell()
"""

class EITs:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

    def fun_facts(self):
        print("Recite fun fact")


    def read_eit(self):
        with open('eits.csv', 'r') as file:
            countries = ['Ghana', 'Nigeria', 'Kenya', 'South Africa', 'Ivory Coast']
            for con in file:
                # if con.nationality in countries:
                #     print(con)
                # else:
                #     return "Country not found"
                print(con)
    def write_eit(self):
        file_exist = os.path.isfile('eits.csv')
        with open('eits.csv', 'a') as my_file:
            fieldnames = ['name', 'nationality']
            writer = csv.DictWriter(my_file, fieldnames=fieldnames)

            if not file_exist:
                writer.writeheader()
            writer.writerow({'name': self.name, 'nationality': self.nationality})

class Fellows:
    def __init__(self, name, nationality, happiness_level):
        self.name = name
        self.nationality = nationality
        self.happiness_level = happiness_level

    def f_eat(self):
        self.happiness_level +=1
        print(self.happiness_level)

    def f_teach(self):
        self.happiness_level -=1
        print(self.happiness_level)

class School(EITs, Fellows):
    def __init__(self, name, nationality, happiness_level, teach):
        print("Nothing")


"""
- Take in EIT from file
- Throw an error if EIT is not from: Ghana, Kenya, Nigeria, South Africa, Ivory coast
"""
name = input("Enter name:")
nationality = input("Enter Country:")
happiness_level = 0
my_eit = EITs(name, nationality)
my_eit.write_eit()
my_eit.read_eit()

