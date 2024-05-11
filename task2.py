class Vehicle:
     vehicle_type = None

class Car:
    """ Автомобили """
    price = 1000000

    def horse_powers(self):
        self.horse_powers = None
        return horse_powers

    def __str__(self):
        return 'Цена {} Мощность двигателя {}'.format(self.price, self.horse_powers)

class Nissan(Car, Vehicle):
    vehicle_type = 'Nissan'
    print(vehicle_type)

    def __init__(self):
        self.price = 1100000
        self.horse_powers=200


car_Nissan = Nissan()
print(car_Nissan)

