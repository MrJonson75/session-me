class Buiding:

    total = 0
    def __init__(self):
        Buiding.total += 1

    pass


for i in range(40):
    new_obj = Buiding()
    print(new_obj)
    print(Buiding.total)

