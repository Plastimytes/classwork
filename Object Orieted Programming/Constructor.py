#Self and constructor

class computer: #If the class is empty it will not work
   pass

c1 = computer()
#creating another object(it will create different addresses)
c2 = computer()

#Creating an id function to print the address of c1
print(id(c1)) 
print(id(c2)) 