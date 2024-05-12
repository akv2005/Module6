class Vehicle:
     vehicle_type = None

class Car:
    """ Автомобили """
    price = 1000000

    def __init__(self):
        self.horse_powers()

    def horse_powers(self):
        self.horse_powers_ = 33

    def __str__(self):
        return '  Цена {}    Мощность двигателя {}'.format(self.price, self.horse_powers_)


class Nissan(Car, Vehicle):
    vehicle_type = 'NISSAN'

    def __init__(self):
        super().__init__()
        self.price = 1100000


    def horse_powers(self):
        self.horse_powers_= 220


car_Nissan = Nissan()
print(car_Nissan.vehicle_type,':  ', car_Nissan)
print()

print(Vehicle.vehicle_type,Car())
