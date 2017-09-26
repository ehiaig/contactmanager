class Person:
    def __init__(self, name, gender):
        if (name == "Francis"):
            raise ValueError("What kind of parents would name their child Francis?")
        else:
            self.__name = name #this implies that the variable name is private
            self.__gender = gender

    def __repr__(self): #the double undescore means that this method is private so cannot be changed.
        return "This person is a {} named {}".format(self.__gender, self.__name)

total_not_francis = Person("Frank", "M")
total_not_francis.__repr__
print(total_not_francis.__dict__)#the __dict__ method makes it possible to change the value in the private methods.

