##Inhertinance Consructors
class A:
    def feature1(self):
        print("Print in A Init...")

    def feature2(self):
        print("Feature Two is working...\n")

#Inheritance
#Creating a new class which will be the child class

class B(A):#This shows that B is inheriting the features of A
    def __init__(self):
        #How to access features of the parent class
        super().__init__()#constructor
        print("Print in B iNIT")


class C(A,B):

  def __init__(self):
    print("Printing c")

a1 =C()    

#Calling the methods (feature1, feature2)
#a1.feature1()
#a1.feature2()

#Objects for class B
#b1 =B()   

#b1.feature3()
#b1.feature4()        
