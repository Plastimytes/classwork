### MINI PROJECT TEST: COURIER_LITE
##The project is an engine for campus delivery with the followings concepts: Collections, Iterators, Generators, Multiple Inheritance, Exceptions and a simple CLI workflow
##Python 3.13 used
import logging

#Logging configuration
logging.basicConfig(level=logging.INFO, format= '%(levelname)s -%(message)s')


##COLLECTIONS AND DATA STRUCTURES
#Creation of main class to manage the other objects
class Courier_Lite_Engine:
    def __init__(self):
        self.couriers = {}# Dictionary used here because changes are not required
        self.locations = {}
        self.pending_orders = []#This can change since these orders are yet to be picked up 
        self.moving_orders = {}

#Method to make sure new locations are added properly without repitition
    def add_loc(self,location):
        if location.name in self.locations:
                raise ValueError(f"Location {location.name} exists!!")
        self.locations[location.name]=location#Incase the location doe not exist this adds the location there

##ITERATORS AND GENERATORS  
#Generator to yeild couriers carrying orders
    def get_cours_by_load(self):
         for courier in self.couriers.values():
              if courier.current_load:
                   yield courier

#Iterator
    def __iter__(self):
         return iter(self.pending_orders)                   


##Class for pickup and drop off points
class Location:
     def __init__(self, pickup_name, dropoff_name):
          self.pickup_name = pickup_name
          self.dropoff_name = dropoff_name

     def motion(self):
          print(f"The pick up was from {self.pickup_name}") 
          print(f"The drop off was from {self.dropoff_name}")

##Class for Order Request  
class Order:
     def __init__(self, order_id, status): 
          self.order_id=order_id
          self.status = status#This will feature once more in the output section

     def ordReq(self):
          print(f"The order is {self.order_id}, and it is {self.status}")


##MIXINS(Mixin is a class that provides extra methods/attributes for other classes without being intended as a standalone base class)   
#Logging mixin to provide methods for logging events for a specific object


#Class and methods for logging events
class LogMixn:
     def log_event(self, message, level='INFO'):
          log_data = {
               'Level': level,
               'Source': self.__class__.__name__,
               'id':getattr(self,'courier_id','N/A'),
               'message': message
          }

          print(f"<{level}> {self.__class__.__name__} {log_data.get('id','')}: {message}")

#Creating a class for the courier
class Courier:
     def __init__(self, courier_id, max_carry_cap, current_load):
          self.courier_id = courier_id
          self.max_carry_cap = max_carry_cap
          self.current_load = current_load

     def asgn_order(self, order: Order):
          if len(self.current_load) < self.max_carry_cap:
               self.current_load.append(order)
               order.status = "IS_BEING_MOVED" 
               return True
          return False 

##MULTIPLE INHERITANCE
class BikeCourier(Courier, LogMixn):
     def __init__(self, courier_id):
          super().__init__(courier_id, max_carry_cap=1) 
          self.log_event("Bike Courier starts")

     def deliver_next(self):
          if not self.current_load:
               self.log_event("Nothing to move", level='WARNING')
               return None 

          delivered_order = self.current_load.pop(0)
          delivered_order.status = "DELIVERED"
          self.log_event(f"Order {delivered_order.order_id} delivered to {delivered_order.dropoff_name}.", level='INFO')
          print(f"{delivered_order}")


#EXCEPTIONS AND STRUCTURED LOGGING
#Base Exception for errors
class Courier_Lite_Error(Exception):
     pass  

#When no courier is found
class Courier_Unavailable_Error(Courier_Lite_Error):
     pass  

##SIMPLE CLI WORKFLOW
def main_Loop():
     engine = Courier_Lite_Engine
     #Inital
     loc_A = Location("Main Entrance")
     loc_B = Location("Hostel A")
     engine.add_loc(loc_A)
     engine.add_loc(loc_B)

     courier_1 = BikeCourier(205)
     engine.couriers[205] = courier_1

     print("============================")
     print("============================")
     print("============Courier Lite Starting ================")

     while True:
          try:
               command =input("Enter Command (Order, Deliver, Status, Exit):").lower()

               if command == 'order':
                    new_ord = Order(
                         order_id=len(engine.pending_orders) + 1,
                         pickup_loc=loc_A,
                         dropoff_loc=loc_B
                    )
                    engine.pending_orders.append(new_ord)
                    print(f"New Order; {new_ord.order_id} created")
                    if courier_1.assign_order(new_ord):
                         print(f"Order {new_ord.order_id} assigned to Courier")
                    else:
                         raise Courier_Unavailable_Error("No courier available")
               
               elif command ==  'deliver':
                    courier_1.deliver_next()

               elif command == 'status':
                    print(f"Pending Orders: {len(engine.pending_orders)}")
                    for courier in engine.get_cours_by_load():
                         print(f"Courier {courier.courier_id} has {len(courier.current_load)} items")

               elif command == 'exit':
                    break

               else:
                    print("Invalid! Try again")                

          except Courier_Lite_Error as e:
               print(f"SYS ERROR !!: {e}")
               courier_1.log_event(f"Command Line Error: {e}", level='ERROR')

          except Exception as e:
               print(f"Unexpected Error: {e}")
               logging.critical("Unhandled error in Command line: {e}")  


if __name__ == "__main__":
     pass               


C1=Courier_Lite_Engine.main_Loop()
C1.add_loc("Home")



