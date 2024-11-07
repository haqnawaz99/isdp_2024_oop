# Step 1: Define the Car class with additional methods and a counter for instances
class Car:
    wheels = 4  # Class variable - shared by all Car instances
    car_count = 0  # Class variable to count the number of Car instances

    def __init__(self, make, model, forsale):
        self.make = make
        self.model = model
        self.forsale = forsale
        Car.car_count += 1  # Increment the car counter when a new instance is created
    
    # Method to display car information
    def display_info(self):
        status = "for sale" if self.forsale else "not for sale"
        print(f"Make: {self.make}, Model: {self.model}, Status: {status}")
    
    # Method to change the sale status of the car
    def change_sale_status(self, new_status):
        self.forsale = new_status
        print(f"Sale status updated for {self.make} {self.model}: {'for sale' if self.forsale else 'not for sale'}")

# Step 2: Create instances of Car and call the methods
car1 = Car("Toyota Corolla", 2022, True)
car2 = Car("Honda Civic", 2023, False)

# Step 3: Accessing instance variables
print(car1.model)  
print(car2.make) 

# Step 4: Accessing class variable
print(car1.wheels)  # Output: 4 (shared by all cars)
print(car2.wheels)  # Output: 4

# Step 5: Accessing class variable using class name
print(Car.wheels)  # Output: 4

# Step 6: Display the total number of Car instances created
print(f"Total number of cars created: {Car.car_count}")
