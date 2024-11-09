# Define a base Shape class to demonstrate inheritance with area and perimeter calculations

# Step 1: Define the Shape class
class Shape:
    def __init__(self, name):
        self.name = name

    # Method to display the name of the shape
    def display_name(self):
        print(f"This is a {self.name}")

    # Placeholder method for calculating area
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

    # Placeholder method for calculating perimeter
    def perimeter(self):
        raise NotImplementedError("Subclasses must implement this method")

# Step 2: Define the Rectangle class inheriting from Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    # Method to calculate the area of the rectangle
    def area(self):
        return self.width * self.height

    # Method to calculate the perimeter of the rectangle
    def perimeter(self):
        return 2 * (self.width + self.height)

# Step 3: Define the Circle class inheriting from Shape
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    # Method to calculate the area of the circle
    def area(self):
        return 3.14 * self.radius ** 2

    # Method to calculate the perimeter (circumference) of the circle
    def perimeter(self):
        return 2 * 3.14 * self.radius

# Step 4: Define the Triangle class inheriting from Shape
class Triangle(Shape):
    def __init__(self, side_a, side_b, side_c):
        super().__init__("Triangle")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    # Method to calculate the perimeter of the triangle
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    # Method to calculate the area using Heron's formula
    def area(self):
        s = self.perimeter() / 2
        return (s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c)) ** 0.5

# Step 5: Create instances of Rectangle, Circle, and Triangle
rectangle = Rectangle(5, 10)
circle = Circle(7)
triangle = Triangle(3, 4, 5)

# Step 6: Call methods for each instance
# Rectangle methods
rectangle.display_name()          # Output: This is a Rectangle
print(f"Area: {rectangle.area()}")      # Output: Area: 50
print(f"Perimeter: {rectangle.perimeter()}")  # Output: Perimeter: 30

# Circle methods
circle.display_name()             # Output: This is a Circle
print(f"Area: {circle.area()}")           # Output: Area: 153.86
print(f"Perimeter: {circle.perimeter()}") # Output: Perimeter: 43.96

# Triangle methods
triangle.display_name()           # Output: This is a Triangle
print(f"Area: {triangle.area()}")         # Output: Area: 6.0
print(f"Perimeter: {triangle.perimeter()}") # Output: Perimeter: 12