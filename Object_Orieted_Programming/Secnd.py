class A:
    def greet(self):
        return "Hello from A"

class B(A):
    def greet(self):
        return "Hello from B"

class C(A):
    def greet(self):
        return "Hello from C"        
    
class D(B, C):
    pass    

D1= D()
print(D1.greet())#iF WE HAVE CLASS INHERITING FROM TWO CLASSES IT CHOOSES FROM THE FIRST CLASS IN THE BRACKET.