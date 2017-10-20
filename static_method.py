import random
"""
Static Method: A method that can be called without a class instance 
- A static method has @staticmethod above it. 
    - @staticmethod is Known as Decorator: Decorator is a function that manipulates another function before calling it
- It doesn't take (self)
It has 
"""
class StringHelper:
    @staticmethod
    def scramble(string):
        temp_str = ""
        for char in string:
            temp_str += char.upper() if random.randint(0,1) else char.lower()
        return (temp_str)

# print(StringHelper.scramble('Andrew'))

    def abbreviate(text, num):
        if num < len(text):
            print(text[0:num]+"...")
        elif num == len(text):
            print(""+str(text))

StringHelper.abbreviate('Hello', 2)
StringHelper.abbreviate('I am late for class because I h8 tech', 9)
StringHelper.abbreviate('moo', 3)




