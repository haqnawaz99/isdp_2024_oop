# Define separate classes for Dog, Cat, and Mouse without using inheritance

# Step 1: Define the Dog class
class Dog:
    def __init__(self, name):
        self.name = name

    # Method for eating
    def eat(self):
        print(f"{self.name} is eating")
    
    # Method for sleeping
    def sleep(self):
        print(f"{self.name} is sleeping")
    
    # Method for barking
    def bark(self):
        print(f"{self.name} is barking")

# Step 2: Define the Cat class
class Cat:
    def __init__(self, name):
        self.name = name

    # Method for eating
    def eat(self):
        print(f"{self.name} is eating")
    
    # Method for sleeping
    def sleep(self):
        print(f"{self.name} is sleeping")
    
    # Method for meowing
    def meow(self):
        print(f"{self.name} is meowing")

# Step 3: Define the Mouse class
class Mouse:
    def __init__(self, name):
        self.name = name

    # Method for eating
    def eat(self):
        print(f"{self.name} is eating")
    
    # Method for sleeping
    def sleep(self):
        print(f"{self.name} is sleeping")
    
    # Method for squeaking
    def squeak(self):
        print(f"{self.name} is squeaking")

# Step 4: Create instances of Dog, Cat, and Mouse
dog = Dog("Buddy")
cat = Cat("Whiskers")
mouse = Mouse("Jerry")

# Step 5: Call methods for each instance
# Dog methods
dog.eat()        # Output: Buddy is eating
dog.sleep()      # Output: Buddy is sleeping
dog.bark()       # Output: Buddy is barking

# Cat methods
cat.eat()        # Output: Whiskers is eating
cat.sleep()      # Output: Whiskers is sleeping
cat.meow()       # Output: Whiskers is meowing

# Mouse methods
mouse.eat()      # Output: Jerry is eating
mouse.sleep()    # Output: Jerry is sleeping
mouse.squeak()   # Output: Jerry is squeaking
