class Car:

    wheels = 4
    def __init__(self):
        self.mil = 10
        self.com = "BMW"


c1 = Car()
c2 = Car()

c1.mil = 8
###Note: Outside the init function you have class variables and inside you have instance variables

print(c1.mil, c1.com)
print(c2.mil, c2.com)