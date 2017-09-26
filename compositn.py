class egg:
    def __init__(self, color, is_broken):
        self.__color = color
        self.__is_broken = is_broken

    def drop_egg(self):
        self.__is_broken = True

class EggCarton:
    def __init__(self):
        self.egg_list = []

    def add_egg(self, egg):
        self.egg_list.append(egg)

    def remove_from_carton(self):
        removed_egg = self.egg_list.pop() #.pop() removes objects in a list. .pop(3) removes the fourth object in a list
        removed_egg.drop_egg()
        return removed_egg


