class Car:
    price = 1000000
    def __init__(self, model):
        self.model = model

    def horse_powers(self):
        horsepower = 100
        return ('Модель: {}, Л/с: {}, Цена: {}'
        .format(self.model, horsepower, self.price))

class Nissan(Car):
    price = 1200000

    def horse_powers(self):
        horsepower = 169
        return ('Модель: {}, Л/с: {}, Цена: {}'
        .format(self.model, horsepower, self.price))


class Kia(Car):
    price = 900000

    def horse_powers(self):
        horsepower = 90
        return ('Модель: {}, Л/с: {}, Цена: {}'
        .format(self.model, horsepower, self.price))

ob0 = Car(model='Lada Vesta')
ob1 = Nissan(model='Primera')
ob2 = Kia(model='Seed')

print(ob0.horse_powers())
print(ob1.horse_powers())
print(ob2.horse_powers())
