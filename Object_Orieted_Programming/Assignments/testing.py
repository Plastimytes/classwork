class Person:
 def __init__ (self, name, placce):
    self.name=name
    self.place=placce

 def give(self):
    print(f"I am {self.name} from {self.place}")   

person1=Person("Martha","Mukono")   

#Printing object
person1.give()
