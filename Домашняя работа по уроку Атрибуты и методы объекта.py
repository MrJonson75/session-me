class House:
    def __init__(self, numberOfFloors):
        self.my_Floors = numberOfFloors
    def lift(self):
        for i in range(self.my_Floors):
            print("Текущий этаж равен", i + 1)
        print("Вы прибыли на этаж: ", self.my_Floors)

    pass


chield_1 = House(10)
chield_1.lift()

chield_2 = House(int(input("Введите номер этажа: ")))
chield_2.lift()
