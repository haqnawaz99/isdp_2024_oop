class Car:
    def __init__(self, make, model, forsale):
        self.make = make
        self.model = model
        self.forsale = forsale

mycar = Car("Toyoya",2024, True)
print(mycar.make)

yourcar = Car("Honda",2023, False)  
print(yourcar.model)