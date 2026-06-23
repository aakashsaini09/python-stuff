class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def fullName(self):
        return f"Brand name: {self.brand} and model: {self.model}"
    def fuelType(self):
        return f"Petrol or disel"


# inheritance
class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        self.batterySize = batterySize
        super().__init__(brand, model)
    def fuelType(self):
        return f"Electric charge"


myCar = Car("Tata", "safari");
print(myCar.brand)
print(myCar.fullName())
print(myCar.fuelType())

electric = ElectricCar("Tesla", "ModelS-S", "85KWH");
print(electric.batterySize)
print(electric.fullName())
print(electric.fuelType())