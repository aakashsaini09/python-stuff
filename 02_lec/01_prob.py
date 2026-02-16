# Create car class with attributes like model and brand. Then create an instance of this class
class Car:
    def __init__(self, userbrand, usermodel):
        self.model = usermodel
        self.brand = userbrand
    def fullName(self):
        return f"Brought a car of {self.brand} company and {self.model} model"


class Electric_car(Car):
    def __init__(self, userbrand, usermodel, battery_size):
        super().__init__(userbrand, usermodel)
        self.battery_size = battery_size



my_car = Car("toyota", "Corolla")
print(my_car.model)

my_new_car = Car("Tata", "Safari")
print(my_new_car.brand)
print(my_new_car.fullName())

electric_c = Electric_car("Tesla", "Monster", "10000mh")
print(electric_c.brand, electric_c.fullName(), electric_c.battery_size)