 ##Its exactly what you think it is
#Example
class A:
    def feature1(self):
        print("Feature One is working...")

    def feature2(self):
        print("Feature Two is working...")

#Inheritance
#Creating a new class which will be the child class
class B(A):#This shows that B is inheriting the features of A
    def feature3(self):
        print("Feature Three is working...")

    def feature4(self):
        print("Feature Four is working...")
    

#Objects for class A
a1 =A()    

#Calling the methods (feature1, feature2)
a1.feature1()
a1.feature2()

#Objects for class B
b1 =B()   


b1.feature1()
b1.feature4()

#A is the super/Parent class and B is the child/Sub class
