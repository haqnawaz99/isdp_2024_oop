# Define a base Vehicle class to demonstrate inheritance

# Step 1: Define the Vehicle class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # Method for starting the vehicle
    def start(self):
        print(f"{self.brand} {self.model} is starting")
    
    # Method for stopping the vehicle
    def stop(self):
        print(f"{self.brand} {self.model} is stopping")

# Step 2: Define the Car class inheriting from Vehicle
class Car(Vehicle):
    # Method for honking
    def honk(self):
        print(f"{self.brand} {self.model} is honking")

# Step 3: Define the Motorcycle class inheriting from Vehicle
class Motorcycle(Vehicle):
    # Method for revving the engine
    def rev_engine(self):
        print(f"{self.brand} {self.model} is revving its engine")

# Step 4: Define the Truck class inheriting from Vehicle
class Truck(Vehicle):
    # Method for loading cargo
    def load_cargo(self):
        print(f"{self.brand} {self.model} is loading cargo")

# Step 5: Create instances of Car, Motorcycle, and Truck
car = Car("Toyota", "Camry")
motorcycle = Motorcycle("Harley-Davidson", "Street 750")
truck = Truck("Volvo", "FH16")

# Step 6: Call methods for each instance
# Car methods
car.start()       # Output: Toyota Camry is starting
car.honk()        # Output: Toyota Camry is honking
car.stop()        # Output: Toyota Camry is stopping

# Motorcycle methods
motorcycle.start()    # Output: Harley-Davidson Street 750 is starting
motorcycle.rev_engine()  # Output: Harley-Davidson Street 750 is revving its engine
motorcycle.stop()     # Output: Harley-Davidson Street 750 is stopping

# Truck methods
truck.start()        # Output: Volvo FH16 is starting
truck.load_cargo()   # Output: Volvo FH16 is loading cargo
truck.stop()         # Output: Volvo FH16 is stopping
