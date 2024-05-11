class Car:
    """ Автомобили """
    price = 1000000

    def horse_powers(self):
        self.horse_powers = None
        return horse_powers

    def __str__(self):
        return '{}:   Цена {} Мощность двигателя {}'.format(self.__class__.__name__, self.price, self.horse_powers)

class Nissan(Car):

    def __init__(self):
        self.price = 1100000
        self.horse_powers=200

class Kia(Car):
    price = 900000
    horse_powers = 120
    print('Цена Kia:', price, '      Мощность двигателя Kia:', horse_powers)


car_Nissan = Nissan()
print(car_Nissan)
car_Kia = Kia()