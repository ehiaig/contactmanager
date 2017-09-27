class Apple:
    num = 5
    def __init__(self, color):
        self.color = color
        print ('A {} cedi {} Apple'.format(self.num, self.color))
        # self.set_price += 1

    # @staticmethod
    def set_price():
        print('A {} cedi {} Apple'.format(num, self.color))


first = Apple("red")
# print(first)
#Output: A 5 cedi red Apple

second = Apple('blue')
# print(second)
# #Output: A 5 cedi blue Apple
#
Apple.set_price()
third=Apple('red')
# print(third)
# #Output: A 6 cedi red Apple
#
# print(first)
# #Output: A 5 cedi red Apple
#
#
