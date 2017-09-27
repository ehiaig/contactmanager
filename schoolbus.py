"""
There is a school bus that contains upto 1 driver and 10 students.
The school bus can drive ONLY IF there are 10 students and 1 driver

Solution:
class SchoolBus:

    def __init__(self):
        self.peoplelist = []
        self.driverlist = []

    def add_student(self):
        stu_name = input('Enter student name:')
        if len(self.peoplelist) < 10:
            self.peoplelist.append(stu_name)
        else:
            print('You cannot add more student')

    def add_driver(self):
        dri_name = input('Enter driver name:')
        if len(self.driverlist) < 1:
            self.driverlist.append(dri_name)
        else:
            print("you need only one driver")

    def drive(self):
        if (len(self.peoplelist) == 10 and len(self.driverlist) == 1 ):
            print('Bus full, we can go now')
        else:
            print('There are {} students and {} driver in the bus, you can\'t drive off'.format(len(self.peoplelist), len(self.driverlist)))

s = SchoolBus()

quit = True
while quit:
    request = input(" 1. to enter student \n 2. to enter driver \n 3. to drive off \n 4. to Quit \n Answer: ")
    if request == '1':
        s.add_student()
    elif request == '2':
        s.add_driver()
    elif request == '3':
        s.drive()
    elif request == '4':
        quit = False
"""


#Using Polymorphism, this can be achieved by:
class Driver:
    def __init__(self, name, liscense_check):
        self.name = name
        self.liscense_check = liscense_check

class Student:
    def __init__(self, name):
        self.name = name

class SchoolBus:
    def __init__(self):
        self.studentlist = []
        self.driverlist = []

    def add_student(self, stu):
        self.studentlist.append(stu)

    def add_driver(self, dri):
        self.driverlist.append(dri)

    def drive(self):
        if len(self.studentlist) == 10 and len(self.driverlist)==1:
            print('Drive on baby!')
        else:
            print('Number of passengers not allowed')

if __name__ == '__main__':
    sb = SchoolBus()
    for _ in range(10):
        sb.add_student(Student('Tom'))
    sb.add_driver(Driver('Nana', True))
    sb.drive()




