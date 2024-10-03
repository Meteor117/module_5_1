class House:
    def __init__(self, name, floors):
        self.name = name
        self.number_of_floor = floors
    def go_to(self, new_floor):
        if 0 < new_floor <= self.number_of_floor:
            for floor in range (1, new_floor + 1):
                print(floor)
        else:
            print('Такого этажа не существует!')


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

h1.go_to(5)
h2.go_to(10)