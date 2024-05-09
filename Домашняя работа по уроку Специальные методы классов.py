class House:
    def __init__(self, floors):
        self.numberOfFloors = floors

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors

    pass


chield_1 = House(0)
print(f"Текущий этаж: {chield_1.numberOfFloors}")

chield_1.setNewNumberOfFloors(int(input("Введите новый этаж: ")))
print(f"Текущий этаж: {chield_1.numberOfFloors}")
