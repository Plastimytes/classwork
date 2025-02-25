#Self and constructor

class computer: #If the class is empty it will not work
   def __init__(self):
     self.name = " Richard"
     self.age = 21

   def update(self):
      self.name = "Jane"
      self.age = 22

   def compare(self, other):
      if self.age ==  other.age:
         return True 
      else:
         return False 

c1 = computer()#computer() is the constructor
#creating another object(it will create different addresses)
c2 = computer()

#changing the name and age
c1.name="Elijah"
c2.age=23

#Updating the object values
c1.update()

 

#Comparing a value n the object
if c1.compare(c2):
   print("Same")

#Creating an id function to print the address of c1
print(c1.name) 
print(c2.name ) 
print("......")
print(c1.age) 
print(c2.age ) 

#Self is a pointer / director
#Comparing
if c1 == c2:
   print("Same")
else:
   print("Different")  