class House:
    def __init__(self, floors):
        self.numberOfFloors = floors

    def setNewNumberOfFloors(self):
        print(f"В этом доме: {self.numberOfFloors} этажей")

    pass

my_hause = [House(floors=13), House(floors=25), House(floors=65)]
my_home= House(my_hause)
for home_obj in my_hause:
    home_obj.setNewNumberOfFloors()
