class Person:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

class EITs(Person):
    def __init__(self, name, nationality):
        super().__init__(name, nationality)

    def fun_facts(self):
        print("My fun fact")

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


name = input("Enter name:")
nationality = input("Enter country:")
happiness_level = 5
fe = Fellows(name, nationality, happiness_level)
fe.teach()