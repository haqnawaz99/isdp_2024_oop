class Car:
    def __init__(self, make, model, forsale):
        self.make = make
        self.model = model
        self.forsale = forsale
    
    # Method to display car information
    def display_info(self):
        status = "for sale" if self.forsale else "not for sale"
        print(f"Make: {self.make}, Model: {self.model}, Status: {status}")
    
    # Method to change the sale status of the car
    def change_sale_status(self, new_status):
        self.forsale = new_status
        print(f"Sale status updated for {self.make} {self.model}: {'for sale' if self.forsale else 'not for sale'}")

# Step 6: Create instances of Car and call the methods
mycar = Car("Toyota", 2024, True)
yourcar = Car("Honda", 2023, False)

# Step 7: Call the display_info method to show car details
mycar.display_info()
yourcar.display_info()

# Step 8: Change the sale status of a car and call display_info again
mycar.change_sale_status(False)  # Change sale status of mycar to not for sale
mycar.display_info()