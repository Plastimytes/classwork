class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno =rollno
        self.lap =self.Laptop()#For the inner class

    def show(self):#Goes to s1.show
        print(self.name, self.rollno) 
        self.lap.show()

    #INNER CLASS
    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.model = 'Pavilion' 
            self.cpu = "i5"
            self.ram = '8GB' 

        def show(self): 
            print(self.brand, self.model, self.cpu, self.ram)     

s1 =Student('Richie',2)  
s2 =Student('Jane', 3)

print(s1.name, s1.rollno)

#s1.show()#To give all the values of s1

lap1= Student.Laptop()
lap2= Student.Laptop()

#print(id(lap1))
#print(id(lap2))

s1.show()