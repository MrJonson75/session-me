from random import randint

# from termcolor import cprint


# Реализуем модель человека.
# Человек может есть, работать, играть, ходить в магазин.
# У человека есть степень сытости, немного еды и денег.
# Если сытость < 0 единиц, человек умирает.
# Человеку надо прожить 365 дней.


class Man:
    """Формируем клас человек"""

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.food = 50
        self.money = 0

    def __str__(self):
        return ('Я - {}, сытость - {}, еды осталось - {}, денег осталось - {}'
                .format(self.name, self.fullness, self.food, self.money))

    '''Вывод информации о человеке'''

    def eat(self):
        if self.food >= 10:
            print('\033[36m {} поел \033[0m'.format(self.name))
            self.fullness += 10
            self.food -= 10
        else:
            print('{} нет еды'.format(self.name))

    """Покормить человека"""

    def work(self):
        print('\033[35m {} сходил на работу \033[0m'.format(self.name))
        self.money += 50
        self.fullness -= 10

    '''Сходил на работу'''

    def play_DOTA(self):
        print('\033[34m {} играл в ДОТУ \033[0m'.format(self.name))
        self.fullness -= 10

    """Играл в игры"""

    def shoping(self):
        if self.money >= 50:
            print('\033[31m {} Сходил в магазин \033[0m'.format(self.name))
            self.money -= 50
            self.food += 50
        else:
            print('\033[31m {} деньги закончились \033[0m'.format(self.name))
        """Сходил в магазин за продуктами"""

    def act(self):
        if self.fullness <= 0:
            print('\033[31m {} умер .... \033[0m'.format(self.name))
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.food < 10:
            self.shoping()
        elif self.money <= 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.play_DOTA()


vasya = Man(name='Вася')
for day in range(1, 21):
    print("\033[33m ==========День {} ============\033[0m".format(day))
    vasya.act()
    print("\033[32m {} \033[0m".format(vasya))




# print(vasya)
# vasya.eat()
# print(vasya)
# vasya.work()
# print(vasya)
# vasya.play_DOTA()
# print(vasya)

# Создадим двух людей, живущих в одном доме - Бивиса и Батхеда
# Нужен класс Дом, в нем должн быть холодильник с едой и тумбочка с деньгами
# Еда пусть хранится в холодильнике в доме, а деньги - в тумбочке.
