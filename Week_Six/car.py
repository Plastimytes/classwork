class Car:
    def __init__(self, model, horsepower, Category,speed, color):
        print(speed)
        print(color)

        self.speed = speed
        self.color = color
        self.model = model
        self.horsepower = horsepower
        self.Category = Category

        print("The __init__ is called")

ford = Car("GT40",481, "Stock",200,"Gray")
honda = Car("Civic Type R",590, "Custom",250, "Blue")
audi = Car("Quttaro Group B",895, "cUSTOM",300, "Black")

print(ford.speed)
print(audi.color)

