from customer import Customer
from product import Product

class Order:
    def __init__(self, order_id, customer: Customer):
        self.order_id = order_id
        self.customer = customer
        self.products = []

    def add_product(self, product: Product):
        self.products.append(product)

    def display_order_summary(self):
        print(f"Order D: {self.order_id}")
        self.customer.display_info()
        print("Products in Order:")
        for product in self.products:
            product.display_info()
        total_price = sum(product.price for product in self.products)
        print(f"Total Price: ${total_price}")
