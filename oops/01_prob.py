# Create car class with attributes like model and brand. Then create an instance of this class
class Car:
    def __init__(self, userbrand, usermodel):
        self.model = usermodel
        self.brand = userbrand

my_car = Car("toyota", "Corolla")
print(my_car.brand)
print(my_car.model)

my_new_car = Car("Tata", "Safari")
print(my_new_car.brand)