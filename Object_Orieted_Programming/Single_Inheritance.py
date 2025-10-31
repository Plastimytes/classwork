class Person:
   def __init__(self, name):
    self.name=name
   def introduce(self):
        print(f"My name is {self.name}")

class Student(Person):
    def student_id(self):
        print(f"My student Id is valid")

Student1=Student("Martha")  
Student1.introduce() 
Student1.student_id()    


#Example 2: Vehicle
class Vehicle:
   def __init__(self, action):
      self.action=action
   def move(self):
      print(f"The car is moving: {self.action}")

class Car(Vehicle):
   def sound(self):
      print("Honk!!")   

car1=Car("Foward")
car1.move()
car1.sound()         

#Example 3: Money
class Account:
   def __init__(self, balance):
    self.balance=balance
   def deposit(self, amount):
      self.balance=self.balance+amount
      print(f"The amount deposited is : {self.balance}")

class SavingsAccount(Account):
   def add_interest(self, rate):
       self.balance=self.balance*(1+rate)
       print(f"The amount with interest is {self.balance}") 

M1=SavingsAccount(1000)#iN THIS TYPE THE CHILD CLASS APPEARS HERE NOT THE PARENT CLASS!!
M1.deposit(500) 
M1.add_interest(5)     

#Overriding
class Shape:
   def __init__(self, areaa):
      self.areaa=areaa
   def orig_area(self):
      print("Area is currently 0 (It is Undefined)")   

class Rectangle(Shape):
   def area(self, width, height):
      self.area= width*height
      print(f"The area is now {self.area}") 

s1=Rectangle(300)
s1.area(32, 21)
