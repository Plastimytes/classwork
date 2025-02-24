###INTRODUCING VARIABLES (__init__)
class Computer:
  def __init__(self, CPU, RAM):#For the arguements
    self.CPU = CPU
    self.RAM = RAM #RAM is an attribute of the class, it's a property of the object. It's a variable that belongs to an object.
  def config(self):#config is the method and self just appears. Self is the object which your passing
    print("Config is", self.CPU, "and ",self.RAM, "GB")#yOU HAVE TO COME AND WRITE THIS IN THE CONFIG. Its just how you should do it

#Passing arguements
COM1 = Computer('I5', 16)
COM2 = Computer('rYZEN 3', 8)

COM1.config()
COM2.config()