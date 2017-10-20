class Apple:
    price = 5
    
    def __init__(self, color):
        self.color = color
        self.price = Apple.price
        print ('A {} cedi {} Apple'.format(self.price, self.color))

    @classmethod
    def set_price(cls, num):
        cls.price = num
        return cls.price

    # The above classmethod block can also be written as a static method block below
    @staticmethod
    def sp(n):
        Apple.price = n
        return Apple.price

first = Apple("red")
second = Apple('blue')

Apple.sp(6)
third = Apple('red')

Apple.set_price(6)
t = Apple('pink')