# Step 11: Define the Animal class and demonstrate inheritance
class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    # Method for eating
    def eat(self):
        print(f"{self.name} is eating")
    
    # Method for sleeping
    def sleep(self):
        print(f"{self.name} is sleeping")

# Step 12: Define subclasses Dog, Cat, and Mouse inheriting from Animal
class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} is meowing")

class Mouse(Animal):
    def squeak(self):
        print(f"{self.name} is squeaking")

# Step 13: Create instances of Dog, Cat, and Mouse
dog = Dog("Buddy")
cat = Cat("Whiskers")
mouse = Mouse("Jerry")

# Step 14: Call methods from the Animal class and their own methods
dog.eat()        # Output: Buddy is eating
dog.sleep()      # Output: Buddy is sleeping
dog.bark()       # Output: Buddy is barking

cat.eat()        # Output: Whiskers is eating
cat.sleep()      # Output: Whiskers is sleeping
cat.meow()       # Output: Whiskers is meowing

mouse.eat()      # Output: Jerry is eating
mouse.sleep()    # Output: Jerry is sleeping
mouse.squeak()   # Output: Jerry is squeaking