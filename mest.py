class Person:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

class EITs(Person):
    def __init__(self, name, nationality, fun_fact):
        super().__init__(name, nationality)
        self.fun_fact = fun_fact

    def fun_facts(self):
        print(self.fun_fact)

class Fellows(Person):
    def __init__(self, name, nationality, happiness_level):
        super().__init__(name, nationality)
        self.happiness_level = happiness_level

    def eat(self):
        self.happiness_level +=1
        print(self.happiness_level)

    def teach(self):
        self.happiness_level -=1
        print(self.happiness_level)

# def check_logic():
#     while True:
#         choice = input("Enter 1 to check for EITs or 2 to check for Fellows")
#         if choice ==1:

name = input("Enter name:")
nationality = input("Enter country:")
happiness_level = 5
fun_fact = input("What'\s your fun fact? ")
fe = Fellows(name, nationality, happiness_level)
fe.teach()

eit = EITs(name, nationality, fun_fact)
eit.fun_facts()