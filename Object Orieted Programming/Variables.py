class Car:
    ##Class namespace
    wheels = 4

    def __init__(self):
        ##Instance namespace
        self.mil = 10
        self.com = "BMW"


c1 = Car()
c2 = Car()

c1.mil = 8
###Note: Outside the init function you have class variables and inside you have instance variables

Car.wheels =5
print(c1.mil, c1.com, c1.wheels)
print(c2.mil, c2.com, c1.wheels)