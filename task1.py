class Car:
    """ Автомобили """
    price = 1000000

    def horse_powers(self):
        self.horse_powers_ = None
        return horse_powers_

    def __str__(self):
        return '{}:   Цена {}    Мощность двигателя {}'.format(self.__class__.__name__, self.price, self.horse_powers_)

class Nissan(Car):

    def __init__(self):
        self.price = 1100000
        self.horse_powers_= self.horse_powers()

    def horse_powers(self):
        self.horse_powers_= 200
        return self.horse_powers_

class Kia(Car):
    def __init__(self):
        self.price = 900000
        self.horse_powers_= self.horse_powers()

    def horse_powers(self):
        self.horse_powers_= 150
        return self.horse_powers_


    # price = 900000
    # horse_powers = 120
    # print('Цена Kia:', price, '      Мощность двигателя Kia:', horse_powers)


car_Nissan = Nissan()
print(car_Nissan)
car_Kia = Kia()
print(Kia())