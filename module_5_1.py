class House:
    def __init__(self, name, number_of_floors, floor):
        self.name = name
        self.number_of_floors = number_of_floors
        self.floor = floor
        self.go_to()

    def go_to(self):
        if self.floor < 1:
            print('В подвале квартир нет.')
        elif self.floor > self.number_of_floors:
            print('Зачем Вам на крышу?')
        else:
            for i in range(1, self.floor + 1):
                print(i)


first_house = House('ЖК Горский', 18, 5)
second_house = House('Домик в деревне', 2, 10)
third_house = House('ООО Кривые ручки', 45, 0)
