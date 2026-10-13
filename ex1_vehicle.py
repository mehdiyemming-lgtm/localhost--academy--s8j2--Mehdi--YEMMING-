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
class Motorcycle(Vehicle):
    def __init__(self, brand, model, engine_size):
        super().__init__(brand, model)
        self.engine_size = engine_size


car = Car("Toyota", "Corolla", 4)
motorcycle = Motorcycle("Yamaha", "MT-07", 689) 

car.show_info()  # Output: Brand: Toyota, Model: Corolla
motorcycle.show_info()  # Output: Brand: Yamaha, Model: MT-07