class Person:
     def __init__ (self,name, age):  
      self.name=name 
      self.age = age
     def get_info(self): 
        print("Name:",self.name) 
        print("Age:",self.age)

Person1= Person ("John", 30) 
Person1.get_info()        