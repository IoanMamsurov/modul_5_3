class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor):
        if new_floor < 1:
            print("Такого этажа не существует")
        elif new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        print(f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')

    def __eq__(self, other):
        isinstance(other, int)
        isinstance(other, House)
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        isinstance(other, int)
        isinstance(other, House)
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        isinstance(other, int)
        isinstance(other, House)
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        isinstance(other, int)
        isinstance(other, House)
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        isinstance(other, int)
        isinstance(other, House)
        return self.number_of_floors <= other.number_of_floors

    def __ne__(self, other):
        isinstance(other, int)
        isinstance(other, House)
        return self.number_of_floors != other.number_of_floors

    def __add__(self, __value):
        isinstance(__value, int)
        isinstance(__value, House)
        self.number_of_floors += __value
        return self

    def __radd__(self, __value):
        isinstance(__value, int)
        isinstance(__value, House)
        return self

    def __iadd__(self, __value):
        isinstance(__value, int)
        isinstance(__value, House)
        return self


house_1 = House('Ленина_1', 10)
house_2 = House('Ленина_2', 20)
house_1.__str__()
house_2.__str__()
print(house_1 == house_2)  # __eq__
house_1.__str__()
house_1 = house_1 + 10  # __add__

print(house_1 == house_2)

house_1 += 10  # __iadd__
house_1.__str__()
house_2 = 10 + house_2  # __radd__
house_2.__str__()

print(house_1 > house_2)  # __gt__
print(house_1 >= house_2)  # __ge__
print(house_1 < house_2)  # __lt__
print(house_1 <= house_2)  # __le__
print(house_1 != house_2)  # __ne__
