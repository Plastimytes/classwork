###Concept is use din Loose coupling, dependency injection, interfaces
##Four ways of implementaing polymoriphism: Duck Typing, Operator overloading, Method overloading, Method overriding
##Duck Typing Example:

#Create class Duck
class Duck:
    def quack(self):
        return "Quack!"

    def walk(self):
        return "Waddle waddle!"
class RobotDuck:
    def quack(self):
        return "Beep beep quack!"

    def walk(self):
        return "Rolling forward!"

def make_it_quack_and_walk(duck_like_thing):
    print(duck_like_thing.quack())
    print(duck_like_thing.walk())

# Create instances of Duck and RobotDuck
real_duck = Duck()
robot_duck = RobotDuck()

# Both can be passed to the same function
make_it_quack_and_walk(real_duck)   # This is a real duck
make_it_quack_and_walk(robot_duck)  # This is a robot duck