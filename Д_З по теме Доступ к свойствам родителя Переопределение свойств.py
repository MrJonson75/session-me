class Vehicle:
    __COLOR_VARIANTS = ['red', 'blue', 'orange', 'black', 'white', 'green']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__color = color
        self.__engine_power = engine_power

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет:\033[32m {self.__color}\033[34m"

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f"\033[35mНельзя сменить цвет на {new_color}\033[0m")

    def print_info(self):
        print(f"\033[34m{self.get_model()}")
        print(f"{self.get_horsepower()}")
        print(f"{self.get_color()}")
        print(f"Владелец: \033[32m{self.owner}\033[0m")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'Blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
