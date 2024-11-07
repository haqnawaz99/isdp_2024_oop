class Mobile:
    brand_count = 0  # Class variable to count the number of Mobile brands

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        Mobile.brand_count += 1  # Increment the brand counter when a new instance is created

    # Method to display mobile information
    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Price: ${self.price}")

# Create instances of Mobile and call the methods
mobile1 = Mobile("Apple", "iPhone 14", 999)
mobile2 = Mobile("Samsung", "Galaxy S22", 799)

# Accessing instance variables
mobile1.display_info()  # Output: Brand: Apple, Model: iPhone 14, Price: $999
mobile2.display_info()  # Output: Brand: Samsung, Model: Galaxy S22, Price: $799

# Display the total number of Mobile brands created
print(f"Total number of mobile brands created: {Mobile.brand_count}")
