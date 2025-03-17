###If you want an object you need to create a class
##Defining a class
#In a class you can set your attribute(variables) and behaviour(Functions/methods)
class Computer:
  def config(self):#config is the method and self just appears. Self is the object which your passing
    print("I5, 16GB, 1TB")

class Computer2:
  def config(self):#config is the method and self just appears. Self is the object which your passing
    print("I4, 6GB, 500gB")

COM1 = Computer()#This...() is a constructor    
COM2 = Computer2()

#Calling the function/method... Mention the name of the class then .config. If yuo want to use a method this what you do.
Computer.config(COM1)
Computer2.config(COM2)

#Call method2(Its better) It is the one we normally use
#You can use the object itself to call the function
COM1.config()
COM2.config()
#X=5

#print(type(X))#The answer is X is an integer
#print(type(COM1)) #The answer will be <class '__main__.Computer'> meaning this is a class of Computer
