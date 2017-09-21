"""
Mr. Todd has bought Andrew a new weave, so now MEST is on a hiring freeze. We can only afford to pay for 4 fellows at a time.
Use a static field to keep track of how many Fellows have been created
If  a user tries to construct a fifth Fellow, raise an exception
"""
# class Fellow:

class Mest:
    fellows_created = 0

    def __init__(self, name, country):
        self.name = name
        self.country = country

        if Mest.fellows_created < 4:
            Mest.fellows_created += 1
        else:
            print("Exception: We cannot afford to hire {} from {}".format(self.name, self.country))
            # raise Exception ("We cannot afford to hire {} from {}".format(self.name, self.country))


my_mest = Mest("Pascal", "Congo")
my_mest = Mest("Francis", "Ghana")
my_mest = Mest("Andrew", "PHP")
my_mest = Mest("Edem", "Ghana")
my_mest = Mest("Tomi", "Nig")
my_mest = Mest("Francis", "Ghana")

my_mest = Mest("Miishe", "Ghana")
print(Mest.fellows_created)
my_mest = Mest("Simi", "Ghana")