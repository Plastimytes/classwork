###INTRODUCING VARIABLES (__init__)
class Computer:
  def __init__(self):
    print("This is init")
  def config(self):#config is the method and self just appears. Self is the object which your passing
    print("I5, 16GB, 1TB")

COM1 = Computer()
COM2 = Computer()

COM1.config()
COM2.config()