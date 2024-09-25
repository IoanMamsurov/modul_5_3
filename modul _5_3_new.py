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
        return f'Название: {self.name}, кол-во этажей: + {str(self.number_of_floors)}'

    def __eq__(self, other):
        if type(other) is int or type(other) is House:
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if type(other) is int or type(other) is House:
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if type(other) is int or type(other) is House:
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if type(other) is int or type(other) is House:
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if type(other) is int or type(other) is House:
            return self.number_of_floors <= other.number_of_floors

    def __ne__(self, other):
        if type(other) is int or type(other) is House:
            return self.number_of_floors != other.number_of_floors

    def __add__(self, __value):
        if type(__value) is int or type(__value) is House:
            self.number_of_floors += __value
            return self

    def __radd__(self, __value):
        if type(__value) is int or type(__value) is House:
            return self

    def __iadd__(self, __value):
        if type(__value) is int or type(__value) is House:
            return self


house_1 = House('Ленина_1', 10)
house_2 = House('Ленина_2', 20)
print(house_1)
print(house_2)
print(house_1 == house_2)  # __eq__
print(house_2)
house_1 = house_1 + 10  # __add__

print(house_1 == house_2)

house_1 += 10  # __iadd__
print(house_2)
house_2 = 10 + house_2  # __radd__
print(house_1)

print(house_1 > house_2)  # __gt__
print(house_1 >= house_2)  # __ge__
print(house_1 < house_2)  # __lt__
print(house_1 <= house_2)  # __le__
print(house_1 != house_2)  # __ne__
