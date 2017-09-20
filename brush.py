import time

class ToothBrush:
    def __init__(self,color,toothpaste=None):
        self.color=color

    def add_toothpaste(self,toothpaste):
        self.toothpaste=toothpaste

    def brush(self,teeth,seconds):
        time.sleep(seconds)
        print("finished brushing")


class ElectricBrush(ToothBrush):
    def __init__(self,color):
        super().__init__(color)
        self.__is_on=False  # private cannot be changed thus __is_on

    def turn_on(self):
        self.__is_on=True

    def turn_off(self):
        self.__is_on=False

e = ElectricBrush("Blue")
print(e.color)