class Vehicle:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model
    def show_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors
    def show_info(self):
    
        print(f"Brand: {self.brand}, Model: {self.model}, Doors: {self.doors}")
class Motorcycle(Vehicle):
    def __init__(self, brand, model, engine_size):
        super().__init__(brand, model)
        self.engine_size = engine_size
    def show_info(self):
        
        print(f"Brand: {self.brand}, Model: {self.model}, Engine Size: {self.engine_size}cc")


vehicles=[
    Car("Toyota", "Corolla", 4),
    Motorcycle("Yamaha", "MT-07", 689),
    Car("Honda", "Civic", 4),
]

for vehicle in vehicles:
    vehicle.show_info()