###1.Define a class car
class car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
        #Encapsulation
        class bank_account:
           def __init__(self, account_number, balance):
               self.account_number = account_number
               self.balance = balance
        
           def config(self):
             print("The account number", self.account_number, "has", self.balance)

           def deposit(self, amount):
                 if amount > 0:
                     self.balance += amount
                     print(f"Deosited {amount}. New balance is {self.balance}")
                 else:
                     print("Invalid deposit amount")

           def withdraw(self, amount):
                if amount > 0 and amount <= self.balance:
                     self.balance -= amount
                     print(f"Withdrew {amount}. New balance is {self.balance}")
                else:
                     print("Invalid withdrawal amount or insufficient funds")             
        Call3=bank_account("qdgfr242353", 2300000)
        Call3.config()

        
    def config(self):
        print("The car make is ",self.make, "of the model",self.model, "and year", self.year)

Call2=car("Toyota Supra", "MK4", 2002)

Call2.config()