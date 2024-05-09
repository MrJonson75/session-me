class Buiding:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return (self.numberOfFloors == other.numberOfFloors,
                self.buildingType == other.buildingType)

    pass

human1 = Buiding(1, "Первый")
human2 = Buiding(5, "Пятый")
my_floor = human1 == human2
print(my_floor)
if all(my_floor):
    print("Люди на одном этаже")
else:
    print("Люди на разных этажах")

