class House:
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self , floors):
        self.numberOfFloors = floors
        print(f"В этом доме: {self.numberOfFloors} этажей")



my_hause = [13, 25, 65]
my_home = House()
for home_obj in my_hause:
    House.setNewNumberOfFloors(self=my_home, floors=home_obj)
