#ATM START!

class ATM:
    def __init__(self, name, pin, balance=0):
         self.name = name
         self.pin = pin
         self.balance = balance

    def balance(self, amount):
         self.balance = amount
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print (f"Deposit successful! New balance: {self.__balance}")
        else:
            print(f"Deposit amount must be a positive value") 

    def withdraw(self, amount):               
         self.balance -=amount

acc= ATM("Rogue",12345,1000)

acc.balance
print(acc.balance)

ATM.deposit(100)
print(ATM.deposit)



