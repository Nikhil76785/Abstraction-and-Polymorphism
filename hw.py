class BMW:

    def fuel_type(self):
        print("BMW uses petrol for the cars.")

    def max_speed(self):
        print("BMW's maximum speed is 200km/h.")


class Ferrari:

    def fuel_type(self):
        print("Ferrari uses petrol for the cars.")

    def max_speed(self):
        print("Ferrari's maximum speed is 300km/h.")


obj = BMW()
obj2 = Ferrari()

for car in (obj, obj2):
    car.fuel_type()
    car.max_speed()