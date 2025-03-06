###Types of Methods
### Instance methods, Class methods and static methods

class Student:

    school = "Jack Mofart"
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def ave(self):##Because we are passing self it is an instance method
        return(self.m1+ self.m2+ self.m3)/3


#Objects(m1, m2 and m3 are instance variables)
s1 =  Student(34, 67, 43)    
s2 =  Student(87, 56, 90)  

##When passing self (instance methods)
s1.avg


