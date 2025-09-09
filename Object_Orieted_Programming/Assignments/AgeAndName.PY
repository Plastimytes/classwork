#Class is Person
class Person:
     def __init__ (self,name, age):  
      self.name=name 
      self.age = age
     def get_info(self): #This is the method
        #Print Statements
        print("Name:",self.name) 
        print("Age:",self.age)

Person1= Person ("John", 30) #Person1 is the object
Person1.get_info()# This accesses the method get_info in the class        