 ##Multiple class inheritance/accessing which is different from multi level
#Example
class A:
    def feature1(self):
        print("Feature One is working...")

    def feature2(self):
        print("Feature Two is working...\n")


class B:
    def feature3(self):
        print("Feature Three is working...")

    def feature4(self):
        print("Feature Four is working...\n")

#Accesssing from multiple classes at once   
class C(A,B):#This shows that C is inheriting the features of B and since B is a child of A, C can also inhertance from its grandparent A.
    def feature5(self):
        print("Feature Five is working...")

    def feature8(self):
        print("Feature Eight is working...")
    

#Objects for class A
a1 =A()    

#Calling the methods (feature1, feature2)
a1.feature1()
a1.feature2()

#Objects for class B
b1 =B()   

b1.feature3()
b1.feature4()

#Objects  class C
c1=C() 

c1.feature1()
c1.feature4()
