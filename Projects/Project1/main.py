from customer import Customer
from product import Product
from order import Order

# Create a customer
customer1 = Customer(1, "John Doe", "john.doe@example.com")

# Create some products
product1 = Product(101, "Laptop", 1200)
product2 = Product(102, "Mouse", 25)
product3 = Product(103, "Keyboard", 45)

# Create an order for the customer
order1 = Order(1001, customer1)

# Add products to the order
order1.add_product(product1)
order1.add_product(product2)
order1.add_product(product3)

# Display the order summary
order1.display_order_summary()