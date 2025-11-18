import logging

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(levelname)s -%(message)s')

# COLLECTIONS AND DATA STRUCTURES
# Creation of main class to manage the other objects
class Courier_Lite_Engine:
    def __init__(self):
        self.couriers = {}  # Dictionary used here because changes are not required
        self.locations = {}
        self.pending_orders = []  # This can change since these orders are yet to be picked up
        self.moving_orders = {}  # Not used in this version, but kept for potential expansion

    # Method to make sure new locations are added properly without repetition
    def add_loc(self, location):
        if location.name in self.locations:
            raise ValueError(f"Location {location.name} exists!!")
        self.locations[location.name] = location  # In case the location does not exist, this adds the location there

    # ITERATORS AND GENERATORS
    # Generator to yield couriers carrying orders
    def get_cours_by_load(self):
        for courier in self.couriers.values():
            if courier.current_load:
                yield courier

    # Iterator
    def __iter__(self):
        return iter(self.pending_orders)

# Class for pickup and drop off points
class Location:
    def __init__(self, name):
        self.name = name

    def motion(self):
        print(f"The pick up was from {self.name}")
        print(f"The drop off was from {self.name}")  # Adjusted for single location name

# Class for Order Request
class Order:
    def __init__(self, order_id, pickup_loc, dropoff_loc):
        self.order_id = order_id
        self.pickup_loc = pickup_loc
        self.dropoff_loc = dropoff_loc
        self.status = "PENDING"  # This will feature once more in the output section

    def ordReq(self):
        print(f"The order is {self.order_id}, and it is {self.status}")

    def __str__(self):
        return f"Order {self.order_id} from {self.pickup_loc.name} to {self.dropoff_loc.name}, status: {self.status}"

# MIXINS (Mixin is a class that provides extra methods/attributes for other classes without being intended as a standalone base class)
# Logging mixin to provide methods for logging events for a specific object
class LogMixn:
    def log_event(self, message, level='INFO'):
        log_data = {
            'Level': level,
            'Source': self.__class__.__name__,
            'id': getattr(self, 'courier_id', 'N/A'),
            'message': message
        }
        print(f"<{level}> {self.__class__.__name__} {log_data.get('id', '')}: {message}")

# Creating a class for the courier
class Courier:
    def __init__(self, courier_id, max_carry_cap, current_load=None):
        self.courier_id = courier_id
        self.max_carry_cap = max_carry_cap
        self.current_load = current_load if current_load is not None else []

    def asgn_order(self, order: Order):
        if len(self.current_load) < self.max_carry_cap:
            self.current_load.append(order)
            order.status = "IS_BEING_MOVED"
            return True
        return False

# MULTIPLE INHERITANCE
class BikeCourier(Courier, LogMixn):
    def __init__(self, courier_id):
        super().__init__(courier_id, max_carry_cap=1, current_load=[])
        self.log_event("Bike Courier starts")

    def deliver_next(self):
        if not self.current_load:
            self.log_event("Nothing to move", level='WARNING')
            return None

        delivered_order = self.current_load.pop(0)
        delivered_order.status = "DELIVERED"
        self.log_event(f"Order {delivered_order.order_id} delivered to {delivered_order.dropoff_loc.name}.", level='INFO')
        print(f"{delivered_order}")

# EXCEPTIONS AND STRUCTURED LOGGING
# Base Exception for errors
class Courier_Lite_Error(Exception):
    pass

# When no courier is found
class Courier_Unavailable_Error(Courier_Lite_Error):
    pass

# SIMPLE CLI WORKFLOW (Modified to simulate commands for automatic output)
def main_Loop():
    engine = Courier_Lite_Engine()  # Create an instance of the engine
    # Initial setup
    loc_A = Location("Main Entrance")
    loc_B = Location("Hostel A")
    engine.add_loc(loc_A)
    engine.add_loc(loc_B)

    courier_1 = BikeCourier(205)
    engine.couriers[courier_1.courier_id] = courier_1

    print("============================")
    print("============================")
    print("============Courier Lite Starting ================")

    # Simulate a sequence of commands to produce output
    commands = ['order', 'status', 'deliver', 'status', 'order', 'status', 'exit']

    for command in commands:
        print(f"\nSimulating command: {command}")
        try:
            if command == 'order':
                new_ord = Order(
                    order_id=len(engine.pending_orders) + 1,
                    pickup_loc=loc_A,
                    dropoff_loc=loc_B
                )
                engine.pending_orders.append(new_ord)
                print(f"New Order: {new_ord.order_id} created")
                if courier_1.asgn_order(new_ord):
                    print(f"Order {new_ord.order_id} assigned to Courier")
                    engine.pending_orders.remove(new_ord)  # Remove from pending once assigned
                else:
                    raise Courier_Unavailable_Error("No courier available")

            elif command == 'deliver':
                courier_1.deliver_next()

            elif command == 'status':
                print(f"Pending Orders: {len(engine.pending_orders)}")
                for courier in engine.get_cours_by_load():
                    print(f"Courier {courier.courier_id} has {len(courier.current_load)} items")

            elif command == 'exit':
                print("Exiting Courier Lite.")
                break

            else:
                print("Invalid! Try again")

        except Courier_Lite_Error as e:
            print(f"SYS ERROR !!: {e}")
            courier_1.log_event(f"Command Line Error: {e}", level='ERROR')

        except Exception as e:
            print(f"Unexpected Error: {e}")
            logging.critical(f"Unhandled error in Command line: {e}")

if __name__ == "__main__":
    main_Loop()
